import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class Demojs():
    def demo_javascript(self):
        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        #driver.get("https://www.rcvacademy.com/")
        driver.execute_script("window.open('https://www.rcvacademy.com/', '_self')")
        time.sleep(5)

        demo_element = driver.execute_script("return document.getElementsByTagName('p')[1];")
        driver.execute_script("arguments[0].click();", demo_element)
demo_execution = Demojs()
demo_execution.demo_javascript()