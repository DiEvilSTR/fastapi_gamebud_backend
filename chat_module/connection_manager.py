from fastapi import WebSocket
from typing import Dict

from chat_module.schemas.chat_message import ChatMessageCreate


class ConnectionManager:
    """
    Connection manager class
    
    This class is responsible for managing the active connections
    
    Attributes:
    - **active_connections**: Dictionary of active connections
    
    Methods:
    - **connect**: Connects a websocket to the manager
    - **disconnect**: Disconnects a websocket from the manager
    - **send_message**: Sends a message to a websocket
    """
    def __init__(self):
        self.active_connections: Dict[str, WebSocket] = {}


    async def connect(self, websocket: WebSocket, user_id: str):
        """
        Connects a websocket to the manager
        
        Parameters:
        - **websocket**: Websocket to connect
        - **user_id**: User id to connect
        """
        await websocket.accept()
        self.active_connections[user_id] = websocket


    def disconnect(self, user_id: str):
        """
        Disconnects a websocket from the manager
        
        Parameters:
        - **user_id**: User id to disconnect
        """
        if user_id in self.active_connections:
            del self.active_connections[user_id]


    async def send_message(self, message_data: ChatMessageCreate, receiver_id: str):
        """
        Sends a message to a websocket
        
        Parameters:
        - **message**: Message to send
        - **user_id**: User id to send
        """
        websocket = self.active_connections.get(receiver_id, None)
        if websocket:
            await websocket.send_text(message_data)


connection_manager = ConnectionManager()
