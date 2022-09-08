import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from tqdm import tqdm

from db import MyDB


TARGET_YEAR = '109'
RESET = True


options = Options()
options.add_argument("--disable-notifications")

chrome = webdriver.Chrome('./chromedriver', chrome_options=options)
chrome.get("https://mops.twse.com.tw/mops/web/t100sb15")

time.sleep(1)
year = chrome.find_element("name", "RYEAR")
year.clear()
year.send_keys(TARGET_YEAR)

time.sleep(1)
select = Select(chrome.find_element("name", "code"))
select.select_by_visible_text('')

time.sleep(1)
submit = chrome.find_element(By.XPATH,
                             '/html/body/center/table/tbody/tr/td/div[4]/'
                             'table/tbody/tr/td/div/table/tbody/tr/td[3]/'
                             'div/div[3]/form/table/tbody/tr/td[4]/table/'
                             'tbody/tr/td[2]/div/div/input')
submit.click()

time.sleep(3)
all_rows = chrome.find_elements(By.XPATH, '//*[@id="table01"]/table[1]/tbody/tr')

this_db = MyDB('default.db', reset=RESET)


for ind in tqdm(range(1, len(all_rows) + 1)):
    this_row = chrome.find_elements(By.XPATH, f'//*[@id="table01"]/table[1]/tbody/tr[{ind}]/td')

    x = [x.text.replace(',', '') for x in this_row[:9]]

    if len(x) == 9:
        this_db.insert_data(TARGET_YEAR, x)

