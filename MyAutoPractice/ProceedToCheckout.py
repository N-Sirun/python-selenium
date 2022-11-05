import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from webdriver_manager.chrome import ChromeDriverManager
#from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
#from selenium.webdriver.common.keys import Keys
#from selenium.webdriver.support.select import Select


class MyCheckout():
    def new_checkout(self):
        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        driver.get("http://automationpractice.com/index.php?id_category=11&controller=category")
        driver.maximize_window()
        item_container = driver.find_element(By.XPATH, "(//div[@class='product-container'])[2]")
        actions = ActionChains(driver)
        actions.move_to_element(item_container)
        actions.perform()
        time.sleep(3)
        driver.find_element(By.XPATH, "(//span[contains(text(),'Add to cart')])[2]").click()
        time.sleep(6)
        driver.find_element(By.XPATH, "//span[@title='Continue shopping']//span[1]").click()
        time.sleep(4)
        item_container2 = driver.find_element(By.XPATH, "(//div[@class='product-container'])[3]")
        actions = ActionChains(driver)
        actions.move_to_element(item_container2)
        actions.perform()
        time.sleep(4)
        driver.find_element(By.XPATH, "(//a[@id='color_37'])[1]").click()
        time.sleep(4)
        driver.find_element(By.XPATH, "//span[@class='span_link no-print']").click()
        time.sleep(4)
        driver.find_element(By.XPATH, "//a[@title='Close']").click()
        time.sleep(4)
        driver.find_element(By.XPATH, "//span[normalize-space()='Add to cart']").click()
        time.sleep(5)
        driver.find_element(By.XPATH, "//span[normalize-space()='Proceed to checkout']").click()
        time.sleep(4)
        first_item = driver.find_element(By.XPATH, "//div//tr[1][@id='product_6_31_0_0']").is_displayed()
        second_item = driver.find_element(By.XPATH, "//div//tr[2][@id='product_7_37_0_0']").is_displayed()

        if first_item and second_item:
            print("Items added to cart")
        time.sleep(2)


proceedToPay = MyCheckout()
proceedToPay.new_checkout()