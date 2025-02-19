from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import undetected_chromedriver as uc
import time

def get_driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--disable-blink-features=AutomationControlled")  # Prevent detection
    options.add_argument("--start-maximized")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--no-sandbox")
    
    # Use undetected_chromedriver
    driver = uc.Chrome(options=options)
    driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")  # Remove WebDriver flag

    return driver

def main():
    driver = get_driver()
    driver.get('https://www.linkedin.com')
    
    time.sleep(5)  # Give time for elements to load
    try:
        element = driver.find_element(By.XPATH, "//some_xpath")
        return element.text
    except:
        return "Element not found or blocked"

print(main())
