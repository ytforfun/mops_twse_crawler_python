from db import MyDB
from crwaler import MopsCrawler


TARGET_YEAR = [108, 109, 110]
TARGET_URL = "https://mops.twse.com.tw/mops/web/t100sb15"
RESET = True

this_db = MyDB('default.db', reset=RESET)


for y in TARGET_YEAR:
    mops = MopsCrawler(TARGET_URL)
    mops.get(y)
    mops.insert_db(this_db)
    mops.close()
