from decouple import config
import requests
from selenium import webdriver
from bs4 import BeautifulSoup as bs
import time

url = 'https://www.esmplus.com/Member/SignIn/LogOn?ReturnValue=-96'

user_id = config('USER_ID', '')
user_pwd = config('USER_PWD', '')

driver = webdriver.Chrome('./chromedriver.exe')
driver.get(url)
driver.find_element_by_css_selector("input[type='radio'][value='GMKT']").click()
driver.find_element_by_css_selector('#SiteId').send_keys(user_id)
driver.find_element_by_css_selector('#SitePassword').send_keys(user_pwd)
driver.find_element_by_css_selector('#btnSiteLogOn').click()
time.sleep(2)

# 팝업창 닫기
if len(driver.window_handles) > 1:
    driver.switch_to.window(driver.window_handles[1])
    driver.close()
    driver.switch_to.window(driver.window_handles[0])

html_source = driver.page_source

try:
    html = driver.page_source
    soup = bs(html, 'html.parser')
    selector = '#sell_note_inner1>ul.processing_info>li #snNewOrder'
    data = soup.select_one(selector)
    print(f'{data.text}개의 신규주문')

    driver.find_element_by_css_selector('#logoff > a').click()
    driver.close()
except Exception as e:
    print(e) 

time.sleep(3)