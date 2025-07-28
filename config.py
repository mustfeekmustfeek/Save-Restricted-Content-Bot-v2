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

API_ID = int(getenv("5618662", "20310539"))
API_HASH = getenv("bf2b762357b4b3c79bbb01e7529b81e2", "aec4988298a609673627f255a5adabc7")
BOT_TOKEN = getenv("7398759794:AAGf2lx9-Z8OFJcZnGcuygY_cMLi_fCCTs0", "")
OWNER_ID = list(map(int, getenv("7962530240", "6103594386").split()))
MONGO_DB = getenv("mongodb+srv://mustfeek8:3VmnTgNJ5vdkSXC3@cluster0.evfwy2i.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0", "")
LOG_GROUP = getenv("-1004708871302", "")
CHANNEL_ID = int(getenv("-1002885568913", "-1002511726148"))
FREEMIUM_LIMIT = int(getenv("FREEMIUM_LIMIT", "10"))
PREMIUM_LIMIT = int(getenv("PREMIUM_LIMIT", "5000"))
WEBSITE_URL = getenv("WEBSITE_URL", "upshrink.com")
AD_API = getenv("AD_API", "52b4a2cf4687d81e7d3f8f2b7bc2943f618e78cb")
STRING = getenv("STRING", None)
YT_COOKIES = getenv("YT_COOKIES", YTUB_COOKIES)
DEFAULT_SESSION = getenv("DEFAUL_SESSION", None)  # added old method of invite link joining
INSTA_COOKIES = getenv("INSTA_COOKIES", INST_COOKIES)
