from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


class TestAutomation:
    def __init__(self):
        self.browser = webdriver.Chrome()

class Login(TestAutomation):
    def __init__(self, url, username_xpath, password_xpath, submit_xpath):
        super().__init__()
        self.browser.get(url)
        time.sleep(2)
        self.username_element = self.browser.find_element_by_xpath(username_xpath)
        self.password_element = self.browser.find_element_by_xpath(password_xpath)
        self.submit_element = self.browser.find_element_by_xpath(submit_xpath)

    def login(self, username, password):
        self.username_element.send_keys(username)
        self.password_element.send_keys(password)
        self.submit_element.click()



trialrun = Login(url='http://127.0.0.1:8000/',
                 username_xpath="//*[@id='exampleModalCenter']/div/div/div/div/form/div[1]/input",
                 password_xpath="//*[@id='exampleModalCenter']/div/div/div/div/form/div[2]/input",
                 submit_xpath="//*[@id='exampleModalCenter']/div/div/div/div/form/button[1]")

trialrun.login(username='sree', password='sreehari123')

