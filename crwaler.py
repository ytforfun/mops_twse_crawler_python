from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from tqdm import tqdm
import time


class MopsCrawler:
    def __init__(self, url):
        options = Options()
        options.add_argument("--disable-notifications")
        options.add_argument("--headless")
        self.chrome = webdriver.Chrome('./chromedriver', chrome_options=options)
        self.chrome.get(url)
        self.year = None
        self.this_table = None

    def get(self, target_year):
        self.year = target_year
        time.sleep(1)
        year = self.chrome.find_element("name", "RYEAR")
        year.clear()
        year.send_keys(self.year)

        time.sleep(1)
        select = Select(self.chrome.find_element("name", "code"))
        select.select_by_visible_text('')

        time.sleep(1)
        submit = self.chrome.find_element(
            By.XPATH,
            '/html/body/center/table/tbody/tr/td/div[4]/'
            'table/tbody/tr/td/div/table/tbody/tr/td[3]/'
            'div/div[3]/form/table/tbody/tr/td[4]/table/'
            'tbody/tr/td[2]/div/div/input'
        )
        submit.click()

        time.sleep(3)
        self.this_table = self.chrome.find_elements(By.XPATH, '//*[@id="table01"]/table[1]/tbody/tr')

    def insert_db(self, db):
        for ind in tqdm(range(1, len(self.this_table) + 1), desc=f'Get {self.year}'):

            this_row = self.chrome.find_elements(By.XPATH, f'//*[@id="table01"]/table[1]/tbody/tr[{ind}]/td')
            x = [x.text.replace(',', '') for x in this_row[:9]]

            if len(x) == 9:
                db.insert_data(self.year, x)

    def close(self):
        self.chrome.close()
