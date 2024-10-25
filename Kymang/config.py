#Kymang

import os

from dotenv import load_dotenv

load_dotenv(".env")


BOT_TOKEN = os.environ.get("BOT_TOKEN", "7368858350:AAH20IUEV1o_f_vAPj187fTlmU_2Im8MjW8")
API_ID = int(os.environ.get("API_ID", "6244159"))
API_HASH = os.environ.get("API_HASH", "3f15b21827506cb63890f756743be15f")
MONGO_URL = os.environ.get("MONGO_URL", "mongodb+srv://fsubprem:itsiannnn@fsubprem.lgqre.mongodb.net/?retryWrites=true&w=majority&appName=fsubprem")
ADMINS = [int(x) for x in (os.environ.get("ADMINS", "1494610306").split())]
MEMBER = [int(x) for x in (os.environ.get("MEMBER", "160").split())]
LOG_GRP = int(os.environ.get("LOG_GRP", "-1002350694478"))
BOT_ID = int(os.environ.get("BOT_ID", "7368858350"))

KITA = [int(x) for x in (os.environ.get("KITA", "7593735232").split())]
