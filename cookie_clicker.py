from selenium import webdriver
from datetime import timedelta, datetime
import time

CHROMEDRIVER = '/usr/bin/chromedriver'
driver = webdriver.Chrome(executable_path=CHROMEDRIVER)
URL = 'http://orteil.dashnet.org/experiments/cookie/'

driver.get(url=URL)

cookie = driver.find_element_by_id("cookie")

game_start = datetime.now()
buy_time = game_start + timedelta(seconds=5)
while datetime.now() < game_start + timedelta(seconds=60):
    cookie.click()
    if datetime.now() >= buy_time:

        money = driver.find_element_by_id("money").text
        money = int(str(money).replace(',', ''))
        cursor = int(str(driver.find_element_by_id("buyCursor").text).split('\n')[0].split(' ')[2].replace(',', ''))
        grandma = int(str(driver.find_element_by_id("buyGrandma").text).split('\n')[0].split(' ')[2].replace(',', ''))
        factory = int(str(driver.find_element_by_id("buyFactory").text).split('\n')[0].split(' ')[2].replace(',', ''))
        mine = int(str(driver.find_element_by_id("buyMine").text).split('\n')[0].split(' ')[2].replace(',', ''))
        shipment = int(str(driver.find_element_by_id("buyShipment").text).split('\n')[0].split(' ')[2].replace(',', ''))

        if money > shipment:
            driver.find_element_by_id("buyShipment").click()
            print('buy shipment')
        elif money > mine:
            driver.find_element_by_id("buyMine").click()
            print('buy mine')
        elif money > factory:
            driver.find_element_by_id("buyFactory").click()
            print('buy factory')
        elif money > grandma:
            driver.find_element_by_id("buyGrandma").click()
            print('buy grandma')
        elif money > cursor:
            driver.find_element_by_id("buyCursor").click()
            print('buy mouse')

        buy_time += timedelta(seconds=5)

