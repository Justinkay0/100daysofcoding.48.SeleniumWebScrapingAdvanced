from selenium import webdriver

CHROMEDRIVER = '/usr/bin/chromedriver'
driver = webdriver.Chrome(executable_path=CHROMEDRIVER)

URL = 'https://en.wikipedia.org/wiki/Main_Page'

driver.get(url=URL)
# number_links = driver.find_element_by_id("articlecount")
number_links = driver.find_element_by_css_selector("#articlecount a")
print(number_links.text)

driver.quit()
