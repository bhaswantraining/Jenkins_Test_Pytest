from selenium import webdriver
import pytest


@pytest.fixture(scope="module")
def login_data():
    datadict = {
        "User": "xyzabc@gmail.com",
        "password": "Test_123456"
    }
    print(datadict)
    return datadict


@pytest.fixture(scope="class")
def setup(request):
    print("initiating chrome driver")
    options = webdriver.ChromeOptions()
    options.add_experimental_option('useAutomationExtension', False)
    driver = webdriver.Chrome(executable_path="/Users/mac/PycharmProjects/Selenium_Automation1/chromedriver-2")
    driver.get("https://www.amazon.com")
    driver.maximize_window()
    driver.implicitly_wait(10)
    request.cls.driver = driver
    yield driver
    driver.close()
