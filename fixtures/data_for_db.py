# region Users
users = [
    {
        "nickname": "Alice Johnson",
        "email": "alice@example.com",
        "birthday": "1990-03-15T10:30:00.000Z",
        "gender": "female",
        "password": "password123",
        "games": [1, 2, 3],
        "country": "China",
        "base_filters": {
            "min_age_preference": 18,
            "max_age_preference": 30,
            "country_preference": "China"
        },
        "gender_filter": ["female", "other", "male"]
    },
    {
        "nickname": "Bob Smith",
        "email": "bob@example.com",
        "birthday": "1985-08-22T16:45:00.000Z",
        "gender": "male",
        "password": "securePass",
        "games": [1, 4, 5],
        "country": "India",
        "base_filters": {
            "min_age_preference": 18,
            "max_age_preference": 30,
            "country_preference": "India"
        },
        "gender_filter": ["female", "other", "male"]
    },
    {
        "nickname": "Charlie Brown",
        "email": "charlie@example.com",
        "birthday": "1992-05-03T08:15:00.000Z",
        "gender": "male",
        "password": "myP@ssw0rd",
        "games": [1, 3, 6],
        "country": "India",
        "base_filters": {
            "min_age_preference": 18,
            "max_age_preference": 30,
            "country_preference": "India"
        },
        "gender_filter": ["female", "other", "male"]
    },
    {
        "nickname": "David Lee",
        "email": "david@example.com",
        "birthday": "1987-11-11T12:00:00.000Z",
        "gender": "male",
        "password": "davidPass123",
        "games": [7, 8, 9],
        "country": "Colombia",
        "base_filters": {
            "min_age_preference": 18,
            "max_age_preference": 30,
            "country_preference": "Colombia"
        },
        "gender_filter": ["female"]
    },
    {
        "nickname": "Emily Davis",
        "email": "emily@example.com",
        "birthday": "1988-09-05T14:20:00.000Z",
        "gender": "female",
        "password": "eMiLy789",
        "games": [1, 10, 11],
        "country": "Colombia",
        "base_filters": {
            "min_age_preference": 18,
            "max_age_preference": 30,
            "country_preference": "Colombia"
        },
        "gender_filter": ["female"]
    },
    {
        "nickname": "Frankie Adams",
        "email": "frankie@example.com",
        "birthday": "1995-07-28T11:10:00.000Z",
        "gender": "male",
        "password": "secureFrank",
        "games": [12, 13, 14],
        "country": "Colombia",
        "base_filters": {
            "min_age_preference": 18,
            "max_age_preference": 30,
            "country_preference": "Colombia"
        },
        "gender_filter": ["female", "other", "male"]
    },
    {
        "nickname": "Grace Evans",
        "email": "grace@example.com",
        "birthday": "1984-12-18T09:00:00.000Z",
        "gender": "female",
        "password": "graceful@123",
        "games": [15, 16, 17],
        "country": "Colombia",
        "base_filters": {
            "min_age_preference": 18,
            "max_age_preference": 30,
            "country_preference": "Colombia"
        },
        "gender_filter": ["female", "other", "male"]
    },
    {
        "nickname": "Hank Wilson",
        "email": "hank@example.com",
        "birthday": "1991-02-27T15:55:00.000Z",
        "gender": "male",
        "password": "H@nkIsCool",
        "games": [1, 18, 19],
        "country": "Sweden",
        "base_filters": {
            "min_age_preference": 18,
            "max_age_preference": 30,
            "country_preference": "Sweden"
        },
        "gender_filter": ["female", "other", "male"]
    },
    {
        "nickname": "Ivy Turner",
        "email": "ivy@example.com",
        "birthday": "1989-06-10T13:40:00.000Z",
        "gender": "female",
        "password": "IvyT#rner",
        "games": [10, 11, 12],
        "country": "Sweden",
        "base_filters": {
            "min_age_preference": 18,
            "max_age_preference": 30,
            "country_preference": "Sweden"
        },
        "gender_filter": ["female", "other", "male"]
    },
    {
        "nickname": "Jackie Hall",
        "email": "jackie@example.com",
        "birthday": "1993-04-04T17:25:00.000Z",
        "gender": "female",
        "password": "Jackie#123",
        "games": [1, 13, 14],
        "country": "Sweden",
        "base_filters": {
            "min_age_preference": 18,
            "max_age_preference": 30,
            "country_preference": "Sweden"
        },
        "gender_filter": ["female", "other", "male"]
    },
    {
        "nickname": "Kevin Moore",
        "email": "kevin@example.com",
        "birthday": "1990-07-19T10:05:00.000Z",
        "gender": "male",
        "password": "KevMoore2023",
        "games": [15, 16, 17],
        "country": "Spain",
        "base_filters": {
            "min_age_preference": 18,
            "max_age_preference": 30,
            "country_preference": "Spain"
        },
        "gender_filter": ["female"]
    },
    {
        "nickname": "Linda Clark",
        "email": "linda@example.com",
        "birthday": "1986-01-29T14:45:00.000Z",
        "gender": "female",
        "password": "LindaP@ss",
        "games": [1, 18, 19],
        "country": "Spain",
        "base_filters": {
            "min_age_preference": 18,
            "max_age_preference": 30,
            "country_preference": "Spain"
        },
        "gender_filter": ["female", "other", "male"]
    },
    {
        "nickname": "Mike Johnson",
        "email": "mike@example.com",
        "birthday": "1994-09-14T12:20:00.000Z",
        "gender": "male",
        "password": "M1keP@ssword",
        "games": [1, 2, 3],
        "country": "Spain",
        "base_filters": {
            "min_age_preference": 18,
            "max_age_preference": 30,
            "country_preference": "Spain"
        },
        "gender_filter": ["female", "other"]
    },
    {
        "nickname": "Nora Garcia",
        "email": "nora@example.com",
        "birthday": "1992-06-08T09:30:00.000Z",
        "gender": "female",
        "password": "Nora123!",
        "games": [4, 5, 6],
        "country": "Spain",
        "base_filters": {
            "min_age_preference": 18,
            "max_age_preference": 30,
            "country_preference": "Spain"
        },
        "gender_filter": ["female"]
    },
    {
        "nickname": "Oliver Smith",
        "email": "oliver@example.com",
        "birthday": "1985-11-02T14:15:00.000Z",
        "gender": "male",
        "password": "OliverPass456",
        "games": [7, 8, 9],
        "country": "Spain",
        "base_filters": {
            "min_age_preference": 18,
            "max_age_preference": 30,
            "country_preference": "Spain"
        },
        "gender_filter": ["female", "other"]
    },
    {
        "nickname": "Paula Harris",
        "email": "paula@example.com",
        "birthday": "1987-03-21T11:50:00.000Z",
        "gender": "female",
        "password": "P@ulaHaRR1s",
        "games": [10, 11, 12],
        "country": "Canada",
        "base_filters": {
            "min_age_preference": 18,
            "max_age_preference": 30,
            "country_preference": "Canada"
        },
        "gender_filter": ["female"]
    },
    {
        "nickname": "Quincy Adams",
        "email": "quincy@example.com",
        "birthday": "1993-08-30T16:10:00.000Z",
        "gender": "male",
        "password": "Quincy#Pass",
        "games": [13, 14, 15],
        "country": "Canada",
        "base_filters": {
            "min_age_preference": 18,
            "max_age_preference": 30,
            "country_preference": "Canada"
        },
        "gender_filter": ["female"]
    },
    {
        "nickname": "Rachel Lee",
        "email": "rachel@example.com",
        "birthday": "1990-04-25T13:05:00.000Z",
        "gender": "female",
        "password": "R@chel21",
        "games": [16, 17, 18],
        "country": "Germany",
        "base_filters": {
            "min_age_preference": 18,
            "max_age_preference": 30,
            "country_preference": "Germany"
        },
        "gender_filter": ["female", "other"]
    },
    {
        "nickname": "Sam Taylor",
        "email": "sam@example.com",
        "birthday": "1988-12-11T14:40:00.000Z",
        "gender": "male",
        "password": "S@am12345",
        "games": [19, 10, 20],
        "country": "Germany",
        "base_filters": {
            "min_age_preference": 18,
            "max_age_preference": 30,
            "country_preference": "Germany"
        },
        "gender_filter": ["female"]
    },
    {
        "nickname": "Tracy Turner",
        "email": "tracy@example.com",
        "birthday": "1994-01-17T09:15:00.000Z",
        "gender": "female",
        "password": "TracyT#rn3r",
        "games": [12, 13, 14],
        "country": "Germany",
        "base_filters": {
            "min_age_preference": 18,
            "max_age_preference": 30,
            "country_preference": "Germany"
        },
        "gender_filter": ["female", "other"]
    },
    {
        "nickname": "Dick Biggenson",
        "email": "dick@example.com",
        "birthday": "1999-07-05T18:30:00.000Z",
        "gender": "male",
        "password": "d1ckB1g",
        "games": [15, 16, 17],
        "country": "Japan",
        "base_filters": {
            "min_age_preference": 18,
            "max_age_preference": 30,
            "country_preference": "Japan"
        },
        "gender_filter": ["female", "male"]
    },
    {
        "nickname": "Sue Smith",
        "email": "sue@example.com",
        "birthday": "2000-12-15T12:20:00.000Z",
        "gender": "female",
        "password": "SueS@ecure",
        "games": [18, 19, 1],
        "country": "Japan",
        "base_filters": {
            "min_age_preference": 18,
            "max_age_preference": 30,
            "country_preference": "Japan"
        },
        "gender_filter": ["female"]
    },
    {
        "nickname": "Harry Potter",
        "email": "harry@example.com",
        "birthday": "1980-07-31T16:40:00.000Z",
        "gender": "male",
        "password": "Wizard123",
        "games": [2, 3, 4],
        "country": "Ukraine",
        "base_filters": {
            "min_age_preference": 18,
            "max_age_preference": 30,
            "country_preference": "Ukraine"
        },
        "gender_filter": ["female"]
    },
    {
        "nickname": "Mickey Mouse",
        "email": "mickey@example.com",
        "birthday": "1928-11-18T11:00:00.000Z",
        "gender": "male",
        "password": "DisneyFan1",
        "games": [5, 6, 7],
        "country": "Singapore",
        "base_filters": {
            "min_age_preference": 18,
            "max_age_preference": 30,
            "country_preference": "Singapore"
        },
        "gender_filter": ["female"]
    },
    {
        "nickname": "Elvis Presley",
        "email": "elvis@example.com",
        "birthday": "1935-01-08T09:50:00.000Z",
        "gender": "male",
        "password": "RockKing123",
        "games": [8, 9, 10],
        "country": "Ukraine",
        "base_filters": {
            "min_age_preference": 18,
            "max_age_preference": 30,
            "country_preference": "Ukraine"
        },
        "gender_filter": ["female"]
    },
    {
        "nickname": "Wonder Woman",
        "email": "wonder@example.com",
        "birthday": "1941-10-25T15:15:00.000Z",
        "gender": "female",
        "password": "Amazon123",
        "games": [11, 12, 13],
        "country": "Singapore",
        "base_filters": {
            "min_age_preference": 18,
            "max_age_preference": 30,
            "country_preference": "Singapore"
        },
        "gender_filter": ["female"]
    },
    {
        "nickname": "Darth Vader",
        "email": "darth@example.com",
        "birthday": "1977-05-25T14:30:00.000Z",
        "gender": "male",
        "password": "DarkSideRulez",
        "games": [14, 15, 16],
        "country": "Ukraine",
        "base_filters": {
            "min_age_preference": 18,
            "max_age_preference": 30,
            "country_preference": "Ukraine"
        },
        "gender_filter": ["female"]
    },
    {
        "nickname": "Spider-Man",
        "email": "spider@example.com",
        "birthday": "1962-08-10T17:20:00.000Z",
        "gender": "male",
        "password": "WebSlinger12",
        "games": [17, 18, 19],
        "country": "Singapore",
        "base_filters": {
            "min_age_preference": 18,
            "max_age_preference": 30,
            "country_preference": "Singapore"
        },
        "gender_filter": ["female"]
    },
    {
        "nickname": "Black Widow",
        "email": "widow@example.com",
        "birthday": "1964-04-01T10:10:00.000Z",
        "gender": "female",
        "password": "SecretAgent1",
        "games": [10, 11, 12],
        "country": "Ukraine",
        "base_filters": {
            "min_age_preference": 18,
            "max_age_preference": 30,
            "country_preference": "Ukraine"
        },
        "gender_filter": ["female"]
    },
    {
        "nickname": "Sherlock Holmes",
        "email": "sherlock@example.com",
        "birthday": "1854-01-06T09:00:00.000Z",
        "gender": "male",
        "password": "Elementary1",
        "games": [13, 14, 15],
        "country": "Singapore",
        "base_filters": {
            "min_age_preference": 18,
            "max_age_preference": 30,
            "country_preference": "Singapore"
        },
        "gender_filter": ["female"]
    },
    {
        "nickname": "string",
        "email": "user@example.com",
        "birthday": "2003-10-08T05:05:59.584Z",
        "gender": "female",
        "password": "string",
        "games": [1, 5, 10, 15],
        "country": "Japan",
        "base_filters": {
            "min_age_preference": 18,
            "max_age_preference": 30,
            "country_preference": "Japan"
        },
        "gender_filter": ["female"]
    }
]
# endregion

# region Genres
genres = [
    {
        "name": "Action",
        "description": "Experience thrilling and fast-paced gameplay."
    },
    {
        "name": "Adventure",
        "description": "Embark on epic journeys and explore new worlds."
    },
    {
        "name": "RPG",
        "description": "Immerse yourself in character-driven stories and make choices that shape the narrative."
    },
    {
        "name": "Strategy",
        "description": "Plan your moves, outwit your opponents, and conquer your objectives."
    },
    {
        "name": "Simulation",
        "description": "Simulate real-life scenarios and experiences to test your skills."
    },
    {
        "name": "Puzzle",
        "description": "Challenge your mind with intricate puzzles and brain teasers."
    },
    {
        "name": "Racing",
        "description": "Feel the adrenaline rush as you compete in high-speed races."
    },
    {
        "name": "Sports",
        "description": "Take part in athletic competitions and sports challenges."
    },
    {
        "name": "Horror",
        "description": "Face your fears in spine-tingling and terrifying settings."
    },
    {
        "name": "Music",
        "description": "Groove to the rhythm and test your musical talents in music-themed gameplay."
    },
    {
        "name": "First-Person Shooter (FPS)",
        "description": "Engage in intense combat from a first-person perspective."
    },
    {
        "name": "Fighting",
        "description": "Enter the arena and engage in one-on-one combat with formidable fighters."
    },
    {
        "name": "Platformer",
        "description": "Leap and bound through platforms and obstacles on your exciting journey."
    },
    {
        "name": "Sandbox",
        "description": "Shape and create your own world, letting your creativity run wild."
    },
    {
        "name": "Stealth",
        "description": "Become a master of stealth and cunning to achieve your covert objectives."
    },
    {
        "name": "Survival",
        "description": "Test your survival skills as you brave challenging environments with limited resources."
    },
    {
        "name": "Racing Simulation",
        "description": "Experience realistic racing simulations with detailed physics and true-to-life challenges."
    },
    {
        "name": "Hack and Slash",
        "description": "Unleash powerful melee attacks to conquer hordes of enemies in fast-paced combat."
    },
    {
        "name": "Tactical RPG",
        "description": "Combine strategy and role-playing elements in tactical battles filled with depth and strategy."
    },
    {
        "name": "Open World",
        "description": "Explore vast open worlds filled with freedom and countless adventures waiting to be discovered."
    }
]
# endregion

# region Games
games = [
    {
        "name": "The Legend of Zelda: Breath of the Wild",
        "description": "An action-adventure game that takes place in a vast open world.",
        "genre_list": [3, 10]  # Genres: Action-Adventure, RPG
    },
    {
        "name": "Grand Theft Auto V",
        "description": "An action-adventure game set in the fictional state of San Andreas.",
        "genre_list": [1]  # Genre: Action
    },
    {
        "name": "The Witcher 3: Wild Hunt",
        "description": "A role-playing game featuring a rich open world and complex characters.",
        "genre_list": [3, 10]  # Genres: Action-Adventure, RPG
    },
    {
        "name": "Red Dead Redemption 2",
        "description": "An action-adventure game set in the late 1800s, featuring an open world.",
        "genre_list": [1, 3]  # Genres: Action, Action-Adventure
    },
    {
        "name": "Minecraft",
        "description": "A sandbox game that allows players to build and explore their own worlds.",
        "genre_list": [14]  # Genre: Sandbox
    },
    {
        "name": "Fortnite",
        "description": "A battle royale game where players fight to be the last one standing.",
        "genre_list": [1]  # Genre: Action
    },
    {
        "name": "Among Us",
        "description": "A multiplayer game where players work together to identify an impostor among them.",
        "genre_list": [8]  # Genre: Party
    },
    {
        "name": "League of Legends",
        "description": "A multiplayer online battle arena game featuring teams of champions.",
        "genre_list": [5]  # Genre: MOBA
    },
    {
        "name": "Call of Duty: Warzone",
        "description": "A free-to-play battle royale game set in the Call of Duty universe.",
        "genre_list": [1, 2]  # Genres: Action, Shooter
    },
    {
        "name": "FIFA 22",
        "description": "A sports simulation game featuring football (soccer) matches.",
        "genre_list": [8]  # Genre: Sports
    },
    {
        "name": "Cyberpunk 2077",
        "description": "An open-world RPG set in a dystopian future city.",
        "genre_list": [3, 10]  # Genres: Action-Adventure, RPG
    },
    {
        "name": "Overwatch",
        "description": "A team-based multiplayer first-person shooter game.",
        "genre_list": [1, 2]  # Genres: Action, Shooter
    },
    {
        "name": "Dark Souls III",
        "description": "An action RPG known for its challenging gameplay and dark fantasy setting.",
        "genre_list": [3, 10]  # Genres: Action-Adventure, RPG
    },
    {
        "name": "Animal Crossing: New Horizons",
        "description": "A life simulation game where players build and customize their island paradise.",
        "genre_list": [15]  # Genre: Simulation
    },
    {
        "name": "Counter-Strike: Global Offensive",
        "description": "A multiplayer first-person shooter game with competitive gameplay.",
        "genre_list": [1, 2]  # Genres: Action, Shooter
    },
    {
        "name": "Among Us",
        "description": "A multiplayer game where players work together to identify an impostor among them.",
        "genre_list": [8]  # Genre: Party
    },
    {
        "name": "Rainbow Six Siege",
        "description": "A tactical shooter game that emphasizes teamwork and strategy.",
        "genre_list": [1, 2]  # Genres: Action, Shooter
    },
    {
        "name": "Stardew Valley",
        "description": "A farming simulation game where players can grow crops and build a farm.",
        "genre_list": [15]  # Genre: Simulation
    },
    {
        "name": "Rocket League",
        "description": "A sports-action game that combines soccer with rocket-powered cars.",
        "genre_list": [7, 8]  # Genres: Racing, Sports
    },
    {
        "name": "Terraria",
        "description": "An action-adventure game with exploration and crafting elements.",
        "genre_list": [3, 14]  # Genres: Action-Adventure, Sandbox
    },
]
# endregion
