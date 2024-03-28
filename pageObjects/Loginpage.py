import pytest
import selenium
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By

class Login:
    textbox_username_id="Email"
    textbox_password_id="Password"
    button_login_xpath="//button[normalize-space()='Log in']"
    link_logout_linktext="Logout"

    def __init__(self,driver):  #The purpose of the constructor is to construct an object and assign a value to the object's members.
        self.driver=driver

    def set_username(self,username):
        self.driver.find_element(By.ID,self.textbox_username_id).clear()
        self.driver.find_element(By.ID,self.textbox_username_id).send_keys(username)

    def set_password(self,password):
        self.driver.find_element(By.ID,self.textbox_password_id).clear()
        self.driver.find_element(By.ID,self.textbox_password_id).send_keys(password)

    def click_login(self):
        self.driver.find_element(By.XPATH,self.button_login_xpath).click()


    def click_logout(self):
        self.driver.find_element(By.LINK_TEXT,self.link_logout_linktext).click()
