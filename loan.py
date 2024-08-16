from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pickle
import time


driver = webdriver.Chrome()  
driver.maximize_window()  
driver.get("https://loan-staging.vercel.app/auth/loan-register")

time.sleep(1)

driver.find_element(By.ID, "validateOnly_firstName").send_keys("Mercy")
time.sleep(2)

driver.find_element(By.ID, "validateOnly_surName").send_keys("Day")
time.sleep(2)

driver.find_element(By.ID, "validateOnly_email").send_keys("mercyday@mailinator.com")
time.sleep(2)

driver.find_element(By.ID, "validateOnly_password").send_keys("Ol@s@nm1")
time.sleep(2)

driver.find_element(By.ID, "validateOnly_confirm").send_keys("Ol@s@nm1")
time.sleep(2)

print("Successfully Registered")

continue_button = driver.find_element(By.XPATH, "//*[@id='validateOnly']/div[3]/div/div/div/div/button")
continue_button.click()
time.sleep(5)

redirected_url = driver.current_url

print("Redirected_URL:", redirected_url)
print("Your Account has been successfully created")
time.sleep(5)



#Navigate to login page   

driver.get("https://loan-staging.vercel.app/auth/login")
time.sleep(3)

driver.find_element(By.ID, "email").send_keys("mercyday@mailinator.com")
time.sleep(2)

driver.find_element(By.ID, "password").send_keys("Ol@s@nm1")
time.sleep(2)

submit_button = driver.find_element(By.XPATH, "//button[@type='submit']")  
submit_button.click() 
time.sleep(5)

redirected_url = driver.current_url

print("Redirected_URL:", redirected_url) 
print("You can now access your dashboard")
time.sleep(5)


#//button[@type='apply'
#Access to the dashboard

#apply_button = driver.find_element(By.XPATH, "//*[@id='validateOnly']/div[2]/div/div/div[2]/div/div/div[2]/div/div/div/div[1]/button")  
#apply_button.click() 
#time.sleep(3)



driver.get("https://loan-staging.vercel.app/app/applicant") 
time.sleep(3)

cookies = driver.get_cookies()


    

#driver.add_cookie({"name": "key", "value": "value"})
driver.add_cookie({"Business Type": "Sole Propietorship", "Company Name": "test", "Registration Number": "2", "NIN": "28191627181", "Date of Birth": "1997-04-13", "Gender": "Male", "Phone Number": "07027278122"})
cookies = driver.get_cookies()
#apply_button = driver.find_element(By.XPATH, "//button[@type='apply']")  
#apply_button.click() 
#time.sleep(5)



business_id = driver.find_element(By.ID, "validateOnly_businessType")

#driver.find_element(By.ID, "validateOnly_businessType")
business_id = driver.find_element(By.XPATH, "//*[@id='validateOnly_businessType']/label[1]/span[1]/input")
business_id.click()

driver.find_element(By.ID, "validateOnly_companyName").send_keys("test")
time.sleep(2)

driver.find_element(By.ID, "validateOnly_registrationNumber").send_keys("test3663")
time.sleep(2)

driver.find_element(By.ID, "validateOnly_nin").send_keys("71349801235")
time.sleep(2)

driver.find_element(By.ID, "validateOnly_nin").send_keys("091275412459")
time.sleep(2)

day_input = driver.find_element(By.ID, "validateOnly_date_of_birth")
month_input = Select(driver.find_element(By.ID, "month_input_id"))
year_input = driver.find_element(By.ID, "year_input_id")

# Input the date of birth
day_input.send_keys("01")  # Enter the day
month_input.select_by_visible_text("January")  # Select the month from the dropdown
year_input.send_keys("1990")  # Enter the year

dropdown_gender = driver.find_element_by_id("validateOnly_gender")

# Wrap the dropdown element with the Select class
dropdown = Select(dropdown_gender)

# Select an option by visible text
dropdown.select_by_visible_text("Option 1")

driver.find_element(By.ID, "validateOnly_phone_number").send_keys("09028288210")
time.sleep(3)




driver.quit()





# try:
#     redirected_url = WebDriverWait(driver, 10).until(EC.url_changes(driver.current_url))
#     print("Redirected URL:", redirected_url)
# finally:
#     # Close the browser
#     driver.quit()