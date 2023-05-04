import os

API_ID = API_ID = 23442389

API_HASH = os.environ.get("API_HASH", "70490ec8a810932cb5cb7f9d6a839ee0")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "6272292618:AAFcnKbo01-kuHUTMju4uG39VrCv-MItlAE")

PASS_DB = int(os.environ.get("PASS_DB", "721"))

OWNER = int(os.environ.get("OWNER", 5448647404))

LOG = -902663113

try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "5448647404").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")
ADMINS.append(OWNER)


