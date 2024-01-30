
import time

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

    url = 'https://www.sjsu.edu/classes/schedules/fall-2023.php'

    br.get(url)

    time.sleep(5)

    br.execute_script("removeButton()")

    time.sleep(5)

    for row in br.find_elements(By.TAG_NAME, 'tr'):
        print(f"row: {row}")

    link = br.find_element(By.ID, 'classSchedule_next')
    br.execute_script("arguments[0].scrollIntoView();", link)
    time.sleep(3)
    link.click()

    print("OK!")

    br.quit()
