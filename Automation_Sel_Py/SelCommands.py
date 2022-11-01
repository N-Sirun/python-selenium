import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

class DemoLearnSel():
    def demobrowsermethods(self):
        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        driver.get("https://trinket.io/python3")
        driver.maximize_window()
        time.sleep(2)
        driver.fullscreen_window()
        time.sleep(2)
        driver.refresh()
        time.sleep(2)
        driver.find_element(By.LINK_TEXT, "Learn More »")
        time.sleep(2)
        driver.back()
        time.sleep(2)
        driver.forward()
        driver.minimize_window()
        time.sleep(2)
        driver.maximize_window()
        driver.quit()

demobrowser = DemoLearnSel()
demobrowser.demobrowsermethods()