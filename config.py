import logging
from telethon import TelegramClient
from RAUSHAN.data import ALTRON

# ------------------ LOGGING ------------------

logging.basicConfig(
    format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
    level=logging.INFO
)

# ------------------ CORE CONFIG ------------------

API_ID = 35411328
API_HASH = "4c8d3c8f5d3483296f5fb530ea2cfcc6"

CMD_HNDLR = "."

OWNER_ID = 8672927645

HEROKU_APP_NAME = ""
HEROKU_API_KEY = ""

# ------------------ USERS ------------------

SUDO_USERS = [8245258112 , 7823771907 , 6054364402 , 8613288855 , 8672927645 , 6574184187 , 6769803792 , 6725827412 ]

for x in ALTRON:
    if x not in SUDO_USERS:
        SUDO_USERS.append(x)

if OWNER_ID not in SUDO_USERS:
    SUDO_USERS.append(OWNER_ID)

# ------------------ BOT TOKENS ------------------

BOT_TOKEN = "8609648734:AAH1F1RGIwC0_y0Uor3U2eqwVxPxgGhd9_Y"
BOT_TOKEN2 = "8753354699:AAEWhyWQ2IMFvJJ0DQj1Zw1R4IeH0dc_sP0"
BOT_TOKEN3 = "8701467251:AAHnBn_RS1AbOI8uSdv4_ynO6CWHFf6yFgM"
BOT_TOKEN4 = "8808041749:AAEfOHFazDocB0S_WQ0x5WFmTxK1IPVkJZg"
BOT_TOKEN5 = "8813725599:AAEXkPfpRpHAvgcyKIBwp9HiGp178XmvRis"
BOT_TOKEN6 = "8701467251:AAFG45zT8JsFppTikmJGuI-BN8fr6PSocLw"
BOT_TOKEN7 = "8870176881:AAEcnxkdGWU9zJog7FHF3VaRinDMVXJmJqc"
BOT_TOKEN8 = "8706730933:AAE8QFXwLhNjS-AAJ9BLlcYcastfvBZP3Xs"
BOT_TOKEN9 = "9246982060:AAEeUsxi9pdmZXArRT5YBIfBxfvZEviCLOI" 
BOT_TOKEN10 = "8609648734:AAG_kv-lREhqnUxFL8f-dcHYMDe3wASr46E"

# ------------------ CLIENT HANDLER ------------------

def start_bot(session_name, bot_token):
    try:
        client = TelegramClient(session_name, API_ID, API_HASH)
        client.start(bot_token=bot_token)
        print(f"{session_name} started")
        return client
    except Exception as e:
        print(f"{session_name} failed: {e}")
        return None

# ------------------ START CLIENTS ------------------

X1 = start_bot("X1", BOT_TOKEN)
X2 = start_bot("X2", BOT_TOKEN2)
X3 = start_bot("X3", BOT_TOKEN3)
X4 = start_bot("X4", BOT_TOKEN4)
X5 = start_bot("X5", BOT_TOKEN5)
X6 = start_bot("X6", BOT_TOKEN6)
X7 = start_bot("X7", BOT_TOKEN7)
X8 = start_bot("X8", BOT_TOKEN8)
X9 = start_bot("X9", BOT_TOKEN9)
X10 = start_bot("X10", BOT_TOKEN10)

# ------------------ ACTIVE CLIENTS ------------------

CLIENTS = [x for x in [X1, X2, X3, X4, X5, X6, X7, X8, X9, X10] if x is not None]

print(f"Total Active Bots: {len(CLIENTS)}")
