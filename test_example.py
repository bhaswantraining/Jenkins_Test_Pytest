from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pytest
import logging

logging.basicConfig(level=logging.INFO)
mylogger = logging.getLogger()


@pytest.mark.usefixtures("setup","login_data")
class TestAmazonlogin:
    def test_title(self):
        mylogger.info(self.driver.title)
        assert "Amazon.com: Online Shopping" in self.driver.title

    def test_print_login_deails(self, login_data):
        print(login_data.get('User'))
        print(login_data.get('password'))

    def test_login_site(self, login_data):
        User_name = login_data.get('User')
        Password = login_data.get('password')

        try:
            mylogger.info(self.driver.find_element(By.XPATH, "/html/body/div[1]/header/div/div[1]/div[2]/div/a[2]/span[1]").text)
            self.driver.find_element(By.XPATH, "/html/body/div[1]/header/div/div[1]/div[2]/div/a[2]/span[1]").click()
            time.sleep(2)
        except:
            mylogger.info("Element Not Found - Login Button")
            exit(2)

        try:
            self.driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div[1]/form/div/div/div/div[1]/input[1]").send_keys(User_name)
            self.driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div[1]/form/div/div/div/div[2]/span/span/input").click()
            time.sleep(2)
        except:
            mylogger.info("Element Not Found - Enter Username")
            exit(2)
        try:
            self.driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div/form/div/div[1]/input").send_keys(Password)
            self.driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div/form/div/div[2]/span/span/input").click()
            time.sleep(2)
        except:
            mylogger.info("Element Not Found - Password")
            exit(2)
        try:
            welcome_screen = self.driver.find_element(By.XPATH,"/html/body/div[1]/header/div/div[1]/div[2]/div/a[2]/span[1]").text
            mylogger.info('Welcome Message :', welcome_screen)
            assert "Hello, Bhaswan" in welcome_screen
        except:
            mylogger.info("Login Failed")
            assert "Login Failed"
