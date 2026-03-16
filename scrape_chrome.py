import time
import traceback

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


def browser():
    opts = Options()
    # opts.add_argument('--headless')
    opts.add_argument('user-agent="Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 " \
                  "(KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36"')
    opts.add_argument("--disable-gpu")
    opts.add_argument("--no-sandbox")
    opts.add_argument("--disable-dev-shm-usage")

    br = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=opts)

    br.set_window_position(50, 50)
    br.set_window_size(900, 900)

    br.implicitly_wait(10)
    return br


if __name__ == '__main__':

    br = browser()

    url = 'https://www.google.com'

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

