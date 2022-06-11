from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.action_chains import ActionChains
import time, oreilly_vars

#TODO: input python scheduler logic so that the script keeps looking for email
class oreilly:
    def open_account(self):
        #Setting up headless options
        options = Options()
        options.headless = True
        #This prevents me from having to dwnload the gecko self.driver
        self.driver = webdriver.Firefox(options=options, service=Service(executable_path=GeckoDriverManager().install()))
        #im prolly gonna have to add vars later
        vars = {}
        #open the oreilly site
        self.driver.get("https://www.oreilly.com/member/login/")
        self.driver.set_window_size(894, 1430)
        #click the username form
        self.driver.find_element(By.CSS_SELECTOR, ".orm-Input-labelTxt").click()
        #input username
        self.driver.find_element(By.ID, "input-yrseibl2vce").send_keys(oreilly_vars.user)
        self.driver.find_element(By.CSS_SELECTOR, ".orm-Button-btnContentWrap").click()
        element = self.driver.find_element(By.CSS_SELECTOR, ".orm-Input-labelTxt")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).click_and_hold().perform()
        element = self.driver.find_element(By.ID, "input-1b7bwfrw657")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).release().perform()
        #click password form
        self.driver.find_element(By.CSS_SELECTOR, ".orm-Input-inputLabel").click()
        #enter password
        self.driver.find_element(By.ID, "input-1b7bwfrw657").send_keys(oreilly_vars.password)
        self.driver.find_element(By.CSS_SELECTOR, ".orm-Button-btnContentWrap").click()
        time.sleep(60)
        self.driver.quit()

Oreilly = oreilly()
Oreilly.open_account()