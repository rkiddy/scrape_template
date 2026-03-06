import time
import traceback

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options

opts = Options()
opts.add_argument("--headless")
opts.add_argument('user-agent="Mozilla/5.0 (X11; Linux x86_64; rv:128.0) Gecko/20100101 Firefox/128.0"')

br = webdriver.Firefox(options=opts)

br.set_window_position(50, 50)
br.set_window_size(900, 900)

br.implicitly_wait(10)

# url = 'https://procurement.sccgov.org/doing-business-county/active-contracts'
url = 'https://justicethomasvacationclub.com'

br.get(url)

print("Good to go!")

time.sleep(5)

try:

    for link in br.find_elements(By.TAG_NAME, 'a'):
        print(f"    link: {link.get_attribute('href')}")

except:
    traceback.print_exc()
finally:
    br.quit()

print("OK!")
