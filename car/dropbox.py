
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import chromedriver_autoinstaller
from selenium.webdriver.common.keys import Keys
import time
from selenium import webdriver 
from pyvirtualdisplay import Display 
import requests
from bs4 import BeautifulSoup, SoupStrainer
import re
import requests
import urllib
import os
from io import BytesIO
import time
from urllib.parse import urlparse
from uuid import uuid4
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings.local")
import django
import cv2
django.setup()
from car.repair.models import Key

while True:
    display = Display(visible=0, size=(1920, 1080)) 
    display.start() 
    path='/srv/car/chromedriver' 
    driver = webdriver.Chrome(path)

    driver.get("https://www.dropbox.com/login?cont=https%3A%2F%2Fwww.dropbox.com%2Fhome")
    id = driver.find_elements_by_class_name("text-input-input")[0]
    id.send_keys("pbcar@naver.com")
    pw = driver.find_elements_by_class_name("text-input-input")[1]
    pw.send_keys("han7980")
    pw.send_keys(Keys.ENTER)
    time.sleep(5)
    driver.implicitly_wait(10)
    for i in range(0,100):
        driver.get("https://dropbox.github.io/dropbox-api-v2-explorer/#files_search_v2")
        btn = driver.find_elements_by_class_name("align-right")[0].find_elements_by_tag_name("button")[0].click()
        time.sleep(3)
        token = driver.find_element_by_id("token-input").get_attribute('value')
        key = Key.objects.get()
        key.key = token
        key.save()
        time.sleep(1800)
    driver.quit()