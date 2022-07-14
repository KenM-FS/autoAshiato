from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox import service as fs
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from mailerAshiato import honto_email
import json

# load json file
## inpul full path to use with crontab
json_open = open('/home/ken/honto/secret.json', 'r')
json_key = json.load(json_open)

# setup selenium
options = Options()
options.headless = True
service = fs.Service(executable_path = '/usr/local/bin/geckodriver')
driver = webdriver.Firefox(options=options, service=service)

# login
url_login = 'https://honto.jp/reg/login.html'
driver.get(url_login)
MAIL_ADDRESS = json_key['MAIL_ADDRESS']
PASS = json_key['HONTO_PASS']
driver.find_element(By.ID, "dy_lginId").send_keys(MAIL_ADDRESS)
driver.find_element(By.ID, "dy_pw").send_keys(PASS)
driver.find_element(By.ID, "dy_btLgin").click()

## waiting for refirect after login
## EC.presence_of_all_elements_located did not work
wait = WebDriverWait(driver, 15)
wait.until(EC.url_changes(url_login))

# draw lots
driver.get('https://honto.jp/my/account/point/footmark.html')
driver.execute_script('javascript:setFootMarkLot(2)')

# check points
WebDriverWait(driver, 15).until(EC.presence_of_all_elements_located)
xpath = '/html/body/div[6]/div/div[9]/div/div/div/p/span'
winPoint = 0
try:
    winPoint = driver.find_element(By.XPATH, xpath).get_attribute("textContent")
except:
    honto_email()
else:
    if winPoint != "1":
        honto_email()

driver.close()
driver.quit()
