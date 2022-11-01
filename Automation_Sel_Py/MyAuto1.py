import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

class MyNewAutomation():
    def locate_by_id_demo(self):
        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        driver.get('https://rate.am/')
        driver.find_element(By.ID, 'ctl00_pnAdds1_Cal_tbR1_v').send_keys('3000')
        time.sleep(6)
        driver.find_element(By.ID, 'ctl00_pnAdds1_Cal_imgRefresh_v').click()
        time.sleep(4)
        driver.find_element(By.ID, 'ctl00_pnAdds1_Cal_dlR1_v').click()
        time.sleep(4)
findbyid = MyNewAutomation()
findbyid.locate_by_id_demo()