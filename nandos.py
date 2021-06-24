#coding: utf-8
import os
import time
import datetime
from codefetch import verification
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

# Selecting driver and setting up format for screenshot naming
driver = webdriver.Safari()
today = datetime.datetime.now()
# Option for creating a folder
# os.mkdir("Screens/" + today.strftime('%Y%m%d'))

# Opening the Nandos URL
driver.get('https://order.nandos.co.uk/store/70f8d9ee-ec44-11ea-aee2-06027916b713/menu/overview?menuUUID=5ec5d7c2-4780-40ad-b413-7fac83aac212')

# This sleep function is an attempt to wait for the page to load first and prevent an error, but it is not entirely efficient
# Usually set to 1 or 3 in this page
time.sleep(3)

# Save a screenshot of the homepage
driver.save_screenshot("Screens/" + today.strftime('%Y%m%d') + "_home.png")

# Tap list and locations
starters_xpath = '//*[@id="scroll-container"]/div[1]/div/div/div[4]/a[2]'
halloumi_xpath = '//*[@id="scroll-container"]/div[1]/div/div/div/div[2]/div/div[2]/div[1]/img'
popup_xpath = '/html/body/div[8]/div/div/footer/div[2]/button'
cart_xpath = '/html/body/div[8]/div/div/footer/div/button'
checkout_xpath = '//*[@id="scroll-container"]/div[1]/header/div[1]/div[2]/a[2]/span[2]'
dismiss_xpath = '/html/body/div[7]/div/div/footer/div/button'
email_xpath = '//*[@id="capture_signIn_signInEmailAddress"]'
password_xpath = '//*[@id="capture_signIn_currentPassword"]'
two_step_xpath = '//*[@id="secondFactorCodeLoginInput"]'
payment_xpath = '//*[@id="scroll-container"]/footer/div[2]/button'
second_popup_xpath = '/html/body/div[6]/div/div/footer/div/button'
pay_button_xpath = '/html/body/div[6]/div/div/footer/div/button'

### Tap 1 - Clicking to see the Starters

try:
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, starters_xpath)))
finally:
    starters_button = driver.find_element_by_xpath(starters_xpath)
    starters_button.click()

time.sleep(1)

### Tap 2 - Selecting a side (halloumi) from the menu

try:
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, halloumi_xpath)))
finally:
    halloumi_button = driver.find_element_by_xpath(halloumi_xpath)
    halloumi_button.click()

### Tap 3 - Add to cart
try:
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, popup_xpath)))
finally:
    dismiss_popup = driver.find_element_by_xpath(popup_xpath)
    dismiss_popup.click()

### Tap 4 - Go to cart / bag view
try:
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, cart_xpath)))
finally:
    view_cart = driver.find_element_by_xpath(cart_xpath)
    view_cart.click()

### Tap 5 - Checkout page
try:
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, checkout_xpath)))
finally:
    checkout_page = driver.find_element_by_xpath(checkout_xpath)
    checkout_page.click()

time.sleep(1)

### Tap 6 - Dismiss allergy alert pop-up
try:
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, dismiss_xpath)))
finally:
    dismiss_allergy = driver.find_element_by_xpath(dismiss_xpath)
    dismiss_allergy.click()

### Tap 7 - Email entry
try:
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, email_xpath)))
finally:
    user_email = driver.find_element_by_xpath(email_xpath)
    user_email.send_keys('user email address here')

### Tap 8 - Password entry
try:
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, password_xpath)))
finally:
    user_pass = driver.find_element_by_xpath(password_xpath)
    user_pass.send_keys('user password here')
    user_pass.send_keys(Keys.RETURN)

time.sleep(3)

### Fetching the verification code from the email inbox
entry_code = driver.find_element_by_xpath(two_step_xpath)
entry_code.send_keys(verification())
entry_code.send_keys(Keys.RETURN)

time.sleep(3)

### Tap 9 - Proceeding to payment
try:
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, payment_xpath)))
finally:
    checkout_button = driver.find_element_by_xpath(payment_xpath)
    checkout_button.click()
    
time.sleep(3)

### Tap 10 - Dismissing another alergy popup, again
try:
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, second_popup_xpath)))
finally:
    allergy_again = driver.find_element_by_xpath(second_popup_xpath)
    allergy_again.click()

time.sleep(1)

### Tap 11 - Click on Apple Pay button if available
try:
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, pay_button_xpath)))
finally:
    # Further code could be added to throw an error in case the button does not appear
    apple_pay = driver.find_element_by_xpath(pay_button_xpath)

# Save a screenshot of payment method seen
driver.save_screenshot("Screens/" + today.strftime('%Y%m%d') + "_cart.png")
time.sleep(1)

# Done!
driver.close()