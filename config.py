# devggn
# Note if you are trying to deploy on vps then directly fill values in ("")

from os import getenv

API_ID = int(getenv("API_ID", "25492855"))
API_HASH = getenv("API_HASH", "61876db014de51a4ace6b169608be4f1")
BOT_TOKEN = getenv("BOT_TOKEN", "")
OWNER_ID = list(map(int, getenv("OWNER_ID", "6359874284").split()))
MONGO_DB = getenv("MONGO_DB", "mongodb+srv://")
LOG_GROUP = getenv("LOG_GROUP", "-1002346166150")
CHANNEL_ID = int(getenv("CHANNEL_ID", "-1002166149059"))
