import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.implicitly_wait(5)
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")

driver.find_element(By.CSS_SELECTOR, '.search-keyword').send_keys('ber')
time.sleep(5)
results = driver.find_elements(By.XPATH, "//div[@class='products']/div")
print(type(results))
count = len(results)
assert count > 0
print(count)

for result in results:
    productName = result.find_element(By.XPATH, "h4").text
    print(productName)
    if productName == 'Strawberry - 1/4 Kg':
        print("{}{}".format("Inside: ", productName))
        result.find_element(By.XPATH, "div/button").click()
        break
driver.find_element(By.XPATH, "//a[@class='cart-icon']").click()
wait = WebDriverWait(driver, 10)
wait.until(expected_conditions.presence_of_element_located(By.XPATH, "//a[@class='text']"))
time.sleep(5)
