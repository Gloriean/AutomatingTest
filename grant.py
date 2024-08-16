from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://grant-staging.vercel.app/apply")
time.sleep(1)

driver.find_element(By.ID, "surname").send_keys("John")
time.sleep(2)

driver.find_elememt(By.ID, "other_names").send_keys("Doe")
time.sleep(2)

driver.find_element(By.ID, "email").send_keys("johndoe@mailinator.com")
time.sleep(2)

driver.find_element(By.ID, "phone_number").send_keys("09027271102")
time.sleep(2)

gender_button = driver.find_element(By.XPATH, "//button[@type='male']")  
gender_button.click()
time.sleep(2)

driver.find_element(By.ID, "residential_address").send_keys("29, goke oladokun")
time.sleep(2)

dropdown_element = driver.find_element_by_id("state_id")
dropdown = Select(dropdown_element)
dropdown.select_by_visible_text("Option 1")

driver.find_element(By.ID, "")

driver.find_element(By.ID, "")