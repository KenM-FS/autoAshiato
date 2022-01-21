from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox import service as fs
from mailerAshiato import honto_email
import time
import json

# load json file
json_open = open('secret.json', 'r')
json_key = json.load(json_open)

# setup selenium
options = Options()
options.headless = True
service = fs.Service(executable_path = '/usr/local/bin/geckodriver')
driver = webdriver.Firefox(options=options, service=service)

# login
driver.get('https://honto.jp/reg/login.html')
MAIL_ADDRESS = json_key['MAIL_ADDRESS']
PASS = json_key['HONTO_PASS']
driver.find_element(By.ID, "dy_lginId").send_keys(MAIL_ADDRESS)
driver.find_element(By.ID, "dy_pw").send_keys(PASS)
driver.find_element(By.ID, "dy_btLgin").click()

# draw lots
driver.get('https://honto.jp/my/account/point/footmark.html')
driver.execute_script('javascript:setFootMarkLot(2)')

# check points
time.sleep(10)
xpath = '/html/body/div[6]/div/div[9]/div/div/div/p/span'
winPoint = 0
try:
    winPoint = driver.find_element(By.XPATH, xpath).get_attribute("textContent")
except:
    honto_email()
else:
    if winPoint != "1":
        honto_email()

