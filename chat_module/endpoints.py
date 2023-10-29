from fastapi import APIRouter, Depends, WebSocket, WebSocketDisconnect
from fastapi.responses import HTMLResponse
from sqlalchemy.orm import Session
from typing import List

from core.db import db_setup
from core.jwt_authentication.jwt_bearer import jwt_scheme

from chat_module.connection_manager import connection_manager
from chat_module.crud import chat_message_crud
from chat_module.schemas.chat_message import ChatMessageCreate, ChatMessage

# Imports from bud_finder_module
from bud_finder_module.crud import bud_match_association_crud

# Imports from user_profile_module
from user_profile_module.crud import user_crud
from user_profile_module.schemas.user import UserAsBudForMatchList

router = APIRouter()

html = """
<!DOCTYPE html>
<html>
    <head>
        <title>Websocket Demo</title>
           <!-- Bootstrap CSS -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-EVSTQN3/azprG1Anm3QDgpJLIm9Nao0Yz1ztcQTwFspd3yD65VohhpuuCOmLASjC" crossorigin="anonymous">

    </head>
    <body>
    <div class="container mt-3">
        <h1>FastAPI WebSocket Chat</h1>
        <h2>Your ID: <span id="ws-id"></span></h2>
        <form action="" onsubmit="sendMessage(event)">
            <input type="text" class="form-control" id="messageText" autocomplete="off"/>
            <button class="btn btn-outline-primary mt-2">Send</button>
        </form>
        <ul id='messages' class="mt-5">
        </ul>
        
    </div>
    
        <script>
            var client_id = Date.now()
            document.querySelector("#ws-id").textContent = client_id;
            var ws = new WebSocket(`ws://localhost:8000/ws/v1/chat/${client_id}`);
            ws.onmessage = function(event) {
                var messages = document.getElementById('messages')
                var message = document.createElement('li')
                var content = document.createTextNode(event.data)
                message.appendChild(content)
                messages.appendChild(message)
            };
            function sendMessage(event) {
                var input = document.getElementById("messageText")
                ws.send(input.value)
                input.value = ''
                event.preventDefault()
            }
        </script>
    </body>
</html>
"""


@router.get("/")
async def get():
    return HTMLResponse(html)


@router.websocket("/chat")
async def websocket_endpoint(websocket: WebSocket, db: Session = Depends(db_setup.get_db), current_user_id: str = Depends(jwt_scheme)):
    await connection_manager.connect(websocket=websocket, user_id=current_user_id)
    try:
        while True:
            message_data_input: ChatMessageCreate = await websocket.receive_text()

            # Save message in the database
            chat_message_crud.save_message(db=db, message=message_data_input)

            # Get websocket of the receiver
            receiver_id = bud_match_association_crud.get_chat_partner_id(db=db, user_id=current_user_id, match_id=message_data_input.match_id)

            # Add sender data to message data
            db_sender_data = user_crud.get_user_by_uuid(db=db, user_id=current_user_id)
            sender_data = UserAsBudForMatchList(**db_sender_data.model_dump())
            
            message_data_output = ChatMessage(**message_data_input.model_dump(), sender=sender_data)
            
            if receiver_id:
                # Send message to the receiver
                await connection_manager.send_message(message_data=message_data_output, receiver_id=receiver_id)

    except WebSocketDisconnect:
        connection_manager.disconnect(user_id=current_user_id)
