# devgagan
# Note if you are trying to deploy on vps then directly fill values in ("")

from os import getenv

# VPS --- FILL COOKIES 🍪 in """ ... """ 

INST_COOKIES = """
# wtite up here insta cookies
"""

YTUB_COOKIES = """
# write here yt cookies
"""

API_ID = int(getenv("API_ID", "25624824"))
API_HASH = getenv("API_HASH", "3b705ab47b4018cb26c87b482a32a70a")
BOT_TOKEN = getenv("BOT_TOKEN", "7964859573:AAFpOzrfQsy2z8BUQfJZiCfPtJo9uR6e-cU")
OWNER_ID = list(map(int, getenv("OWNER_ID", "5707498585").split()))
MONGO_DB = getenv("MONGO_DB", "")
LOG_GROUP = getenv("LOG_GROUP", "-1001701493097")
CHANNEL_ID = int(getenv("CHANNEL_ID", "-1001918774095"))
FREEMIUM_LIMIT = int(getenv("FREEMIUM_LIMIT", "0"))
PREMIUM_LIMIT = int(getenv("PREMIUM_LIMIT", "500"))
WEBSITE_URL = getenv("WEBSITE_URL", "tnlinks.in")
AD_API = getenv("AD_API", "03d52a6cae2e4b2fce67525b7a0ff4b26ad8eee2")
STRING = getenv("STRING", None)
YT_COOKIES = getenv("YT_COOKIES", YTUB_COOKIES)
INSTA_COOKIES = getenv("INSTA_COOKIES", INST_COOKIES)
