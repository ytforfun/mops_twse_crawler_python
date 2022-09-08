from utils.db import MyDB
from utils.crwaler import MopsCrawler


TARGET_YEAR = [108, 109, 110]
TARGET_URL = "https://mops.twse.com.tw/mops/web/t100sb15"
RESET = True

this_db = MyDB('db/default.db', reset=RESET)


for y in TARGET_YEAR:
    mc = MopsCrawler(TARGET_URL)
    mc.get(y)
    mc.insert_db(this_db)
    mc.close()
