
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import chromedriver_autoinstaller
from selenium.webdriver.common.keys import Keys
import time
option = Options()
option.add_argument("app-version=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.75 Safari/537.36")
chrome_ver = chromedriver_autoinstaller.get_chrome_version().split('.')[0]
try:
    driver = webdriver.Chrome(f'./{chrome_ver}/chromedriver.exe', options=option)
except:
    chromedriver_autoinstaller.install(True)
    driver = webdriver.Chrome(f'./{chrome_ver}/chromedriver.exe', options=option)

chrome_ver = chromedriver_autoinstaller.get_chrome_version().split('.')[0]
try:
    driver = webdriver.Chrome(f'./{chrome_ver}/chromedriver.exe', options=option)
except:
    chromedriver_autoinstaller.install(True)
    driver = webdriver.Chrome(f'./{chrome_ver}/chromedriver.exe', options=option)
driver.get("https://www.dropbox.com/login?cont=https%3A%2F%2Fwww.dropbox.com%2Fhome")
id = driver.find_elements_by_class_name("text-input-input")[0]
id.send_keys("pbcar@naver.com")
pw = driver.find_elements_by_class_name("text-input-input")[1]
pw.send_keys("han7980")
pw.send_keys(Keys.ENTER)
time.sleep(5)
driver.implicitly_wait(10)
driver.get("https://dropbox.github.io/dropbox-api-v2-explorer/#files_search_v2")
btn = driver.find_elements_by_class_name("align-right")[0].find_elements_by_tag_name("button")[0].click()
time.sleep(3)
token = driver.find_element_by_id("token-input").get_attribute('value')
print(token)