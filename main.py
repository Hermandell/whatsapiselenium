from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.chrome.options import Options


options = webdriver.ChromeOptions()
options.add_argument(r"user-data-dir=C:\Users\Hermandell\PycharmProjects\whatsSelenium\data")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
options.add_argument("--headless=new")  # Add this line for headless mode

driver = webdriver.Chrome(options=options)
#driver.maximize_window()
driver.get('https://web.whatsapp.com')


time.sleep(20)


driver.find_element(By.XPATH, "//span[@title='Larch']").click()
# Improved XPath to find the message field
message_field = driver.find_element(By.XPATH, "//div[@class='x1hx0egp x6ikm8r x1odjw0f x1k6rcq7 x6prxxf']//p[@class='selectable-text copyable-text x15bjb6t x1n2onr6']")
message_field.send_keys("Message to be sent to Larch!")
message_field.click()
message_field.send_keys(Keys.ENTER)
time.sleep(5)
