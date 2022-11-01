import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from webdriver_manager.chrome import ChromeDriverManager
#from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
#from selenium.webdriver.common.keys import Keys
#from selenium.webdriver.support.select import Select


class MyAddToCart():
    def new_cart(self):
        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        driver.get("http://automationpractice.com/index.php")
        driver.maximize_window()
        menu_title = driver.find_element(By.XPATH, "//a[@class='sf-with-ul'][normalize-space()='Women']")
        actions = ActionChains(driver)
        actions.move_to_element(menu_title)
        actions.perform()
        time.sleep(2)
        driver.find_element(By.XPATH, "//a[@title='Blouses']").click()
        time.sleep(2)
        blouse_item = driver.find_element(By.XPATH, "//div[@class='product-container']")
        actions = ActionChains(driver)
        actions.move_to_element(blouse_item)
        actions.perform()
        time.sleep(2)
        driver.find_element(By.XPATH, "//span[normalize-space()='Add to cart']").click()
        time.sleep(3)
        driver.find_element(By.XPATH, "//div[@class='layer_cart_cart col-xs-12 col-md-6']").is_displayed = True
        time.sleep(3)
        print("Item successfully added to cart.")


add_to_cart = MyAddToCart()
add_to_cart.new_cart()