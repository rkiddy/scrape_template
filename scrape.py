import time
from selenium import webdriver
from selenium.webdriver.common.by import By

br = webdriver.Chrome()

br.set_window_position(50, 50)
br.set_window_size(900, 900)

br.implicitly_wait(10)

url = 'https://procurement.sccgov.org/doing-business-county/active-contracts'

br.get(url)

print("Good to go!")

time.sleep(5)

try:

    for link in br.find_elements(By.TAG_NAME, 'a'):
        print(f"    link: {link.get_attribute('href')}")

except:
    traceback.print_exc()

print("OK!")

br.quit()

