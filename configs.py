from os import getenv

class Config:
    API_ID = int(getenv("API_ID", "1313697"))
    API_HASH = getenv("API_HASH", "9f1f1ed9bb3585823c77e1953d3b102d")
    BOT_TOKEN = getenv("BOT_TOKEN", "7969568367:AAE8SnlYzjuD3z6IrX42jy9evVIqVGFchxg")
    # Admin Or Owner Id(s)
    SUDO = list(map(int, getenv("SUDO", "2098589219").split()))
    MONGO_URI = getenv("MONGO_URI", "mongodb+srv://Autof1:Autof01@autof1.zza5eft.mongodb.net/?retryWrites=true&w=majority&appName=Autof1")

cfg = Config()
