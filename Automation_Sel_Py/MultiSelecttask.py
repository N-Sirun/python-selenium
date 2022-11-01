import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
# DIDNT FIND PROPER WEBSITE TO TEST MULTISELECT
class DemodropdownSelect():
    def demo_dropdown(self):
        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        driver.get("https://preview.colorlib.com/theme/bootstrap/multiselect-08/")
        dd_demo = driver.find_element(By.CLASS_NAME, "chosen-choices")
        dd_new = Select(dd_demo)
        time.sleep(2)
        dd_new.select_by_index(2)
        time.sleep(2)
        dd_new.select_by_value("Value")
        dd_new.select_by_visible_text("New York Giants")
        dd_new.deselect_by_visible_text("New York Giants")
        dd_new.select_by_index(2)
        time.sleep(4)
dropdwn_check1 = DemodropdownSelect()
dropdwn_check1.demo_dropdown()