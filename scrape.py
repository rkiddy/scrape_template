
import time
import traceback

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options

if __name__ == '__main__':

    opts = Options()
    opts.add_argument("--headless")

    br = webdriver.Firefox(options=opts)

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
