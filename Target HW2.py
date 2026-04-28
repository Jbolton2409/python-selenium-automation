from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()

#Open website
driver.get("https://www.target.com/")
sleep(2)

#Click account button
driver.find_element(By.XPATH, "//a[@data-test='@web/AccountLink']").click()
driver.find_element(By.XPATH, "//button[@data-test='accountNav-signIn']").click()
sleep(7)

#verification
expected_result = 'Sign in or create account'
actual_result = driver.find_element(By .XPATH, "//h1[contains(.,'Sign in')]").text
assert expected_result in actual_result, f'Expected "{expected_result}" not in actual {actual_result}'

print('Test case passed')
driver.quit()