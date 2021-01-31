from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path='C:/Users/sam/PycharmProjects/python-selenium-automation/chromedriver.exe')
driver.maximize_window()

# open the url
driver.get('https://www.amazon.com/')

search = driver.find_element(By.ID, 'twotabsearchtextbox').send_keys('Dress')

# wait for 4 sec
sleep(4)

# click search
driver.find_element(By.ID, 'nav-search-submit-button').click()

actual_text = driver.find_element(By.XPATH, "//span[@class='a-color-state a-text-bold']").text
expected_text = '"Dress"'

assert expected_text == actual_text, f'Expected {expected_text},but got {actual_text}'
driver.quit()