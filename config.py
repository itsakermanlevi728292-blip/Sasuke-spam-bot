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

OWNER_ID = 8762430892 

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

BOT_TOKEN = "8729033912:AAF40BVQtm-oPAshYyUBgUQ64uBJbgUBE8k"
BOT_TOKEN2 = "8673515468:AAEgcxvwz-vMgU6hMac_U_WSLzeux4FtsU4"
BOT_TOKEN3 = "8841286654:AAHrUaeitvtBboo13oaY_jF1sq-1cj5ju3Y"
BOT_TOKEN4 = "8863803584:AAGZAhuqpyV0i0xIV1Sag4VDoujENiv_KDI"
BOT_TOKEN5 = "8907115818:AAHqPXZ3sUtW6oZ0FKDrtJDAvd6HLR2eJdc"
BOT_TOKEN6 = "8873632455:AAGtpd_DuCR8FpeDOE928n0hq1ETOpk73do"
BOT_TOKEN7 = "8647962263:AAEksnmUjgZIviGeiu74ypRM6-I4o1vGgHc"
BOT_TOKEN8 = "8850881671:AAFe8Nmv4xXBvMT9qBs9vNx4OL40qle8CiM"
BOT_TOKEN9 = "7955396710:AAHsNgJPlAO5xlyi61YIms3DsMGnJbSptA8"
BOT_TOKEN10 = "8637388887:AAGOyBwTx2kHjJVESPJ5_qXmq40TDWzAsOw"

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
