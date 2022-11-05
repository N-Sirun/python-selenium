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
        driver.implicitly_wait(6)
        driver.maximize_window()
        item_container = driver.find_element(By.XPATH, "(//div[@class='product-container'])[2]")
        actions = ActionChains(driver)
        actions.move_to_element(item_container)
        actions.perform()
        time.sleep(3)
        driver.find_element(By.XPATH, "(//span[contains(text(),'Add to cart')])[2]").click()
        time.sleep(3)
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
        totlprice = driver.find_element(By.XPATH, "//span[@id='total_price']")
        #totlprice.text = "$48.90"
        if totlprice.text == "$48.90":
            driver.find_element(By.XPATH, "(//span[contains(text(),'Proceed to checkout')])[2]").click()
            print("Successfully proceeded to checkout")
        else:
            print("Wrong price or items in cart")
            time.sleep(4)
        if first_item and second_item:
            print("Items added to cart")
        driver.find_element(By.XPATH, "//input[@id='email']").send_keys("lola.matiz@mail.ru")
        driver.find_element(By.XPATH, "//input[@id='passwd']").send_keys("lolapractice")
        # time.sleep(2)
        driver.find_element(By.XPATH, "//span[normalize-space()='Sign in']").click()
        driver.find_element(By.XPATH, "//b[normalize-space()='Cart']").click()
        first_item = driver.find_element(By.XPATH, "(//td[@class='cart_product'])[1]").is_displayed()
        second_item = driver.find_element(By.XPATH, "(//tr[@id='product_7_37_0_764388'])[1]").is_displayed()
        if first_item and second_item:
            driver.find_element(By.XPATH, "(//span[contains(text(),'Proceed to checkout')])[2]").click()
        if driver.find_element(By.XPATH, "//li[@class='step_current third']//span[1]").is_displayed():
            driver.find_element(By.XPATH, "(//span[contains(text(),'Proceed to checkout')])[2]").click()
        driver.find_element(By.XPATH, "//input[@id='cgv']").click()
        driver.find_element(By.CSS_SELECTOR, "button[name='processCarrier'] span").click()
        time.sleep(3)
        driver.find_element(By.XPATH, "//a[@title='Pay by bank wire']").click()
        if driver.find_element(By.XPATH, "//h3[normalize-space()='Bank-wire payment.']").is_displayed():
            driver.find_element(By.XPATH, "//span[normalize-space()='I confirm my order']").click()
        print("Successfully created an order. Test completed!")


proceedToPay = MyCheckout()
proceedToPay.new_checkout()