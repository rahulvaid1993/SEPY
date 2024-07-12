import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://nagarro.sharepoint.com/sites/aqt-learning-development")
print(driver.current_url)
print(driver.title)
# time.sleep(10)

# The above method works if the chromedriver is available
# if you want to pass manually the browserdriver

# service_obj = Service("/users/rahul/browserdrivers/chromedriver")
# driver = webdriver.Chrome(service=service_obj)
