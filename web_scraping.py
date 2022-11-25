from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import codecs
import re
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(ChromeDriverManager().install())

web_email = "<email here>"
web_pass = "<password here>"

driver.get("<website url here")

username = driver.find_element_by_id("email")
password = driver.find_element_by_xpath("//input[@type='password']")
username.send_keys(web_email)
password.send_keys(web_pass)
driver.find_element_by_class_name("confirm-btn").click()
driver.switch_to_default_content()
time.sleep(10)

page_source = driver.page_source

soup = BeautifulSoup(page_source,features="html.parser")
# print(soup)


