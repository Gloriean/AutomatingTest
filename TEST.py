from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time

driver = webdriver.Chrome()
driver.get("https://www.google.com/")

action = ActionChains(driver)

search_bar = driver.find_element(By.NAME, "q").send_keys("jim ron")
time.sleep(3)

submit_button = driver.find_element(By.NAME, "btnk").send_keys(Keys.click)
time.sleep(3) 


driver.close()