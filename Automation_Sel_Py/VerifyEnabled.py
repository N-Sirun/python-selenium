import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

class Demodisabled():
    def demo_disabled(self):
        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        driver.get("https://training.openspan.com/login")
        button_enabled = driver.find_element(By.XPATH, "//input[@id='login_button']").is_enabled()
        print(button_enabled)
new_disable = Demodisabled()
new_disable.demo_disabled()