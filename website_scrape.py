from selenium import webdriver 
#download selenium according to chrome version
from selenium.webdriver.chrome.service import Service

service = Service('--Path to Chromedriver exe on system')
def get_driver():
  options = webdriver.ChromeOptions()#needs path of driver exe files present on system of that web browsers
  options.add_argument("disable-infobars")
  options.add_argument("start-maximized")#start browser in full-window
  options.add_argument("disable-dev-shm-usage")#for linux
  options.add_argument("no-sandbox")
  options.add_argument("disable-blink-featueres = AutomationControlled")
  options.add_experimental_option("excludeSwitches",["enable-automation"])#some browsers blocks external scraping script this surpass that limitation

  driver = webdriver.Chrome(service = service, options = options)
  driver.get('link to web address to automate')
  return driver

def main():
  driver = get_driver()
  element = driver.find_element(by = "xpath", value = "")
  return element.text

print(main())