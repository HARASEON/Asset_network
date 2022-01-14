import datetime as dt
import pandas as pd
import requests
import time
import urllib.request 
import re 
import konlpy
from bs4 import BeautifulSoup
from pandas import DataFrame
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys

#크롬드라이버 연결

delay=0.1
browser = Chrome()
browser.implicitly_wait(delay)
start_url = 'https://www.youtube.com/channel/UCtckgmUcpzqGnzcs7xEqMzQ/videos'
browser.get(start_url) 
browser.maximize_window()
body = browser.find_element_by_tag_name('body')

num_of_pagedowns = 30


#스크롤다운
while num_of_pagedowns:
	body.send_keys(Keys.PAGE_DOWN)

time.sleep(0.1)
num_of_pagedowns -= 1

