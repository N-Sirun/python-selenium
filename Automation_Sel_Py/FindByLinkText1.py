import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

class DemoFindElementByLink():
    def locate_by_id_demo(self):
        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        driver.get("https://trinket.io/python3")
        element = driver.find_element(By.LINK_TEXT, "Learn More »").click()
        time.sleep(4)
        element = driver.find_element(By.LINK_TEXT, "full documentation").click()
        time.sleep(4)
findbyid = DemoFindElementByLink()
findbyid.locate_by_id_demo()