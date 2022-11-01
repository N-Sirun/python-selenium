import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

class Demodisplayed():
    def demo_displayed(self):
        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        driver.get("https://www.w3schools.com/howto/howto_js_display_checkbox_text.asp")
        driver.find_element(By.ID, "myCheck").click()
        time.sleep(2)
        var1 = driver.find_element(By.ID, "myCheck").is_selected()
        print(var1)


displayed = Demodisplayed()
displayed.demo_displayed()