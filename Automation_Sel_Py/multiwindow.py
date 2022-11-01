import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

class Demomultiplewindow():
    def demo_window(self):
        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        driver.get("https://www.yatra.com/")
        driver.maximize_window()
        driver.find_element(By.XPATH, "//a[@href='https://www.yatra.com/offer/details/icici-bank-credit-card-offers']//div[@class='image-holder']//img[@alt='Flat 12% OFF (up to Rs 1,500)']").click()

        parent_handle = driver.current_window_handle
        print(parent_handle)
        time.sleep(4)
        all_handles = driver.window_handles
        print(all_handles)
        for handle in all_handles:
            if handle != parent_handle:
                driver.switch_to.window(handle)
                driver.find_element(By.XPATH, "//a[@id='twtr_yttkd']").click()
                time.sleep(4)
                driver.close()
                time.sleep(2)
                break
        driver.switch_to_window(parent_handle)
        driver.find_element(By.XPATH, "//a[@title='Niyo Global HP']//img[@class='conta iner large-banner']").click()
multiplewin= Demomultiplewindow()
multiplewin.demo_window()