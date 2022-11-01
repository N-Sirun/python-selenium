import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select

class MyLoginTest():
    def new_login(self):
        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        #driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
        driver.get("http://automationpractice.com/index.php")
        driver.find_element(By.XPATH, "//a[normalize-space()='Sign in']").click()
        #time.sleep(2)
        driver.find_element(By.XPATH, "//input[@id='email']").send_keys("lola.matiz@mail.ru")
        driver.find_element(By.XPATH, "//input[@id='passwd']").send_keys("lolapractice")
        #time.sleep(2)
        driver.find_element(By.XPATH, "//span[normalize-space()='Sign in']").click()
        #time.sleep(2)
        driver.find_element(By.XPATH, "//span[normalize-space()='Order history and details']").is_displayed()
        #driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div[3]/div/div/div[1]/ul/li[1]/a/span").is_displayed()
        #time.sleep(2)
        driver.close()
newtestlogin=MyLoginTest()
newtestlogin.new_login()
