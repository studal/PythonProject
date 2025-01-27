import os

import pytest
from selenium import webdriver

from Config.config import TestData
from Pages.CheckoutPage import CheckoutPage
from Pages.HeaderPage import HeaderPage
from Pages.HomePage import HomePage
from Pages.InventoryItemPage import InventoryItemPage
from Pages.LoginPage import LoginPage
from Pages.SideBarPage import SideBarPage

web_driver = None

@pytest.fixture(params=["chrome"], scope='class')
def init_driver(request):
    global web_driver

    if request.param == "chrome":
        web_driver = webdriver.Chrome(executable_path=TestData.CHROME_EXECUTABLE_PATH)
    if request.param == "firefox":
        web_driver = webdriver.Firefox(executable_path=TestData.FIREFOX_EXECUTABLE_PATH)
    web_driver.implicitly_wait(10)
    web_driver.maximize_window()
    web_driver.delete_all_cookies()
    request.cls.driver = web_driver    # This will make 'driver' accessible at class level accessing this fixture

    request.cls.loginPage = LoginPage(web_driver)
    request.cls.sidebar = SideBarPage(web_driver)
    request.cls.homePage = HomePage(web_driver)
    request.cls.header = HeaderPage(web_driver)
    request.cls.checkout = CheckoutPage(web_driver)
    request.cls.inventoryitemPage = InventoryItemPage(web_driver)
    yield
    web_driver.close()
