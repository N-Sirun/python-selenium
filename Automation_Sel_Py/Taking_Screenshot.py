import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class Demoscreenshot():
    def demo_capture(self):
        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        driver.get("https://secure.yatra.com/social/common/yatra/signin.htm")
        continue1 = driver.find_element(By.XPATH, "//button[@id='login-continue-btn']")
        continue1.screenshot(".\\DemoScreen.png")
        continue1.click()
        time.sleep(4)
        driver.get_screenshot_as_file("C:\\Users\\Narine_Sirunyan\\new.png")
        driver.save_screenshot(".\\ErrorScreen.png")

ddscreenshot = Demoscreenshot()
ddscreenshot.demo_capture()