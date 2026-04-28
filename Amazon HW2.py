from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()

#Open website
driver.get("https://www.amazon.com/")
sleep(2)

#Amazon logo
driver.find_element(By.XPATH,  "//i[@aria-label='Amazon']")

#Email Logo
driver.find_element(By.XPATH, "//input[@id='ap_email_login']")

#Continue
driver.find_element(By.XPATH, "//input[@type='submit']")

#Conditions of use link
driver.find_element(By.XPATH, "//a[contains(text(), 'Conditions of Use')]")

#Privacy Notice
driver.find_element(By.XPATH, "//a[@href='/gp/help/customer/display.html/ref=ap_signin_notification_privacy_notice?ie=UTF8&nodeId=468496']")

#Need Help
driver.find_element(By.XPATH, "//a[@class='a-size-base a-link-normal']")