import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()

driver.get("https://magento.softwaretestingboard.com/")

driver.maximize_window()
print(driver.title)
print(driver.current_url)

driver.find_element(By.ID, 'search').send_keys('hero')
driver.find_element(By.XPATH, "//input[@id='search']").send_keys('hero')

driver.find_element(By.XPATH, "//*[@id='ui-id-5']").click()
text = driver.find_element(By.XPATH, "//div[@class='breadcrumbs']/ul/li[2]/strong").text
assert 'Men' in text
driver.find_element(By.LINK_TEXT, "Sale").click()

time.sleep(5)

# for static dropdowns

# dropdown = Select(driver.find_element((By.ID, "Rahul")))
# dropdown.select_by_index(1)


'''countries = driver.find_elements(By.CSS_SELECTOR, '#countries')

print(len(countries))

for country in countries:
    if country.text == 'India':
        country.click()
        break'''


'''checkboxes = driver.find_elements(By.CSS_SELECTOR, '#checkbox')

print(len(checkboxes))

for checkbox in checkboxes:
    if checkbox.get_attribute("value") == "option2":
    checkbox.click()
    assert checkbox.is_selected()
    break
'''

