import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select

class MySignUpTest():
    def new_signup(self):
        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        driver.get("http://automationpractice.com/index.php?controller=authentication&back=my-account#account-creation")
        driver.maximize_window()
        driver.find_element(By.XPATH, "//a[normalize-space()='Sign in']").click()
        time.sleep(2)
        driver.find_element(By.XPATH, "//input[@id='email_create']").send_keys("skillehuhk10@luddo.me")
        driver.find_element(By.XPATH, "//span[normalize-space()='Create an account']").click()
        time.sleep(3)
        driver.find_element(By.ID, "id_gender1").click()
        time.sleep(3)
        driver.find_element(By.XPATH, "//input[@id='customer_firstname']").send_keys("Oscar")
        driver.find_element(By.XPATH, "//input[@id='customer_lastname']").send_keys("M")
        time.sleep(3)
        driver.find_element(By.XPATH, "//input[@id='passwd']").send_keys("newPass12")
        dropdwn = driver.find_element(By.XPATH, "//select[@id='days']")
        dd = Select(dropdwn)
        dd.select_by_index(3)
        time.sleep(3)
        dropdwn2 = driver.find_element(By.XPATH, "//select[@id='months']")
        dd2 = Select(dropdwn2)
        dd2.select_by_value("2")
        time.sleep(3)
        dropdwn3 = driver.find_element(By.XPATH, "//select[@id='years']")
        dd3 = Select(dropdwn3)
        dd3.select_by_value("1990")
        time.sleep(3)
        driver.find_element(By.XPATH, "//input[@id='newsletter']").click()
        driver.find_element(By.ID, "address1").send_keys("2639 Oral Lake Road")
        time.sleep(3)
        driver.find_element(By.XPATH, "//input[@id='city']").send_keys("Pineland")
        dropdwnstate = driver.find_element(By.XPATH, "//select[@id='id_state']")
        dstate = Select(dropdwnstate)
        dstate.select_by_value("40")
        time.sleep(3)
        driver.find_element(By.XPATH, "//input[@id='postcode']").send_keys("29934")
        time.sleep(3)
        driver.find_element(By.XPATH, "//input[@id='phone_mobile']").send_keys("618-674-5426")
        time.sleep(3)
        driver.find_element(By.XPATH, "//span[normalize-space()='Register']").click()
        time.sleep(3)

createacc=MySignUpTest()
createacc.new_signup()