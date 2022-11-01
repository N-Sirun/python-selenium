import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

class DemoFindElementByID():
    def locate_by_id_demo(self):
        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        driver.get("https://wearecommunity.io/events/integration-tests-in-30-minutes/talks/17284")
        element = driver.find_element(By.CSS_SELECTOR, "#video_play")
        element.click()
        time.sleep(2)
        element = driver.find_element(By.CSS_SELECTOR,".evnt-button.sky-gradient.small")
        element.click()
        time.sleep(4)
findbycss = DemoFindElementByID()
findbycss.locate_by_id_demo()