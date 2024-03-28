import pytest
import selenium
from selenium import webdriver
from pageObjects.Loginpage import Login

class Test_001_login:
    baseURL= "http://admin-demo.nopcommerce.com"
    username: str= "admin@yourstore.com"
    password= "admin"

    def test_homepage_title(self):
        self.driver=webdriver.Chrome()
        self.driver.get(self.baseURL)
        act_title=self.driver.title
        if act_title=="Your store. Login8":
          assert True
          self.driver.close()
        else:
            self.driver.save_screenshot('./screenshots'+"test_homepage_title.png")
            self.driver.close()
            assert False

    def test_login(self):
        self.driver =webdriver.Chrome()
        self.driver.get(self.baseURL)
        #inorder to access methods of loginpage class, we need to create object for the class
        self.lp=Login(self.driver)  #why we are passing driver as parameter means we used this loginpage model
        self.lp.set_username(self.username)
        self.lp.set_password(self.password)
        self.lp.click_login()

        act_title=self.driver.title

        if act_title=="Dashboard / nopCommerce administration8":
            self.driver.close()
            assert True
        else:
            self.driver.save_screenshot('./screenshots' + "test_login.png")
            self.driver.close()
            assert False


