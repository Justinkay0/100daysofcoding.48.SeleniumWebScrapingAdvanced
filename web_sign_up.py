from selenium import webdriver

CHROMEDRIVER = '/usr/bin/chromedriver'
driver = webdriver.Chrome(executable_path=CHROMEDRIVER)
URL = 'http://secure-retreat-92358.herokuapp.com/'

driver.get(url=URL)

first_name = driver.find_element_by_name("fName")
first_name.send_keys("John")

last_name = driver.find_element_by_name("lName")
last_name.send_keys("cena")

email = driver.find_element_by_name("email")
email.send_keys("youcant@seemee.com")

signup = driver.find_element_by_class_name("btn-primary")
signup.click()