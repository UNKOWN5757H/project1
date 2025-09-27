from os import getenv

class Config:
    API_ID = int(getenv("API_ID", ""))
    API_HASH = getenv("API_HASH", "")
    BOT_TOKEN = getenv("BOT_TOKEN", "")
    # Admin Or Owner Id(s)
    SUDO = list(map(int, getenv("SUDO", "").split()))
    MONGO_URI = getenv("MONGO_URI", "")

cfg = Config()
