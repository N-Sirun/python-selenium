import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
#from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
#from selenium.webdriver.common.keys import Keys
#from selenium.webdriver.support.select import Select

class MySearchtest():
    def new_search(self):
        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        driver.get("http://automationpractice.com/index.php")
        driver.maximize_window()
        driver.find_element(By.XPATH, "//input[@id='search_query_top']").send_keys("casual dre")
        time.sleep(2)
        search_results = driver.find_elements(By.XPATH, "//div[@class='ac_results']//ul[1]/li[2]")
        time.sleep(4)
        #print(len(search_results))
        for results in search_results:
            if "Casual Dresses > Printed Dress" in results.text:
                results.click()
                time.sleep(3)
                break
        driver.find_element(By.XPATH, "//span[@id='our_price_display']").is_displayed()
        time.sleep(2)
        print("Tested Successfully. Found the Printed dress and navigated to its page.")


partialsearch = MySearchtest()
partialsearch.new_search()