from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(executable_path='C:/Users/sam/PycharmProjects/python-selenium-automation/chromedriver.exe')
driver.maximize_window()

# open the url
driver.get('https://www.amazon.com/gp/help/customer/display.html')
# wait for 4 sec
sleep(4)
# Enter "Cancel order" text and perform "ENTER" keyboard action
search = driver.find_element(By.ID, 'helpsearch').send_keys('Cancel order' + Keys.ENTER)

# click search


actual_text = driver.find_element(By.XPATH, "//h1[text()='Cancel Items or Orders']").text
expected_text = 'Cancel Items or Orders'

assert expected_text == actual_text, f'Expected {expected_text},but got {actual_text}'
driver.quit()
