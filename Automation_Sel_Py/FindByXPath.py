import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

class DemoFindElementByXPath():
    def locate_by_id_demo(self):
        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        driver.get("https://rate.am/")
        element = driver.find_element(By.XPATH, "//a[contains(text(),'Վարկային կազմակերպություններ')]")
        element.click()
        time.sleep(4)
findbyid = DemoFindElementByXPath()
findbyid.locate_by_id_demo()


