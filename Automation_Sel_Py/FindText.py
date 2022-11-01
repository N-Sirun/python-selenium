import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

class DemoGetText():
    def demo_gettext(self):
        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        driver.get("https://rate.am/")
        text = driver.find_element(By.XPATH, "//a[contains(text(),'Ընտրեք Ձեզ ամենամոտ մասնաճյուղը և խնայեք Ձեր ժաման')]").text
        text1 = driver.find_element(By.LINK_TEXT, "Արդշինբանկ").text
        print(text1)
        time.sleep(4)
findbyid = DemoGetText()
findbyid.demo_gettext()
