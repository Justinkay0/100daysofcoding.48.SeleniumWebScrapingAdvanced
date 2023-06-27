from selenium import webdriver

CHROMEDRIVER = '/usr/bin/chromedriver'
driver = webdriver.Chrome(executable_path=CHROMEDRIVER)

py_web = driver.get('https://www.python.org/')
calender_of_items = driver.find_elements_by_xpath("/html/body/div/div[3]/div/section/div[2]/div[2]/div/ul")
state = 0

list_of_events = [event.text.split('\n') for event in calender_of_items]
list_of_events = list_of_events[0]

calender_of_event = {}
dates_of_event = list_of_events[0::2]
name_of_event = list_of_events[1::2]

for number, event in enumerate(dates_of_event):
    calender_of_event[number] = {
        'Time': f"2023-{event}",
        'Name': f'{name_of_event[number]}'
    }
print(calender_of_event)
driver.quit()