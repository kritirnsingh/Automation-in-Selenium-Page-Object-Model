import time
import pytest
from selenium.webdriver import ActionChains, Keys
from PageObject.ProductRcognic import ProductPage


class TestProductRecognic():

    @pytest.fixture(autouse=True)
    def classSetup(self, setup):
        self.driver = setup

    def test_Product(self):
        self.driver.get("https://www.recognic.ai/")

        # To Maximize the browser
        self.driver.maximize_window()

        self.ep = ProductPage(self.driver)
        self.ep.clickOnProduct()

        act_title = self.driver.title
        if act_title == "Product - Recognic":
            assert True
        else:
            assert False

        # Click on space to scroll the page down

        actions = ActionChains(self.driver)
        for _ in range(2):
            actions.send_keys(Keys.SPACE).perform()
            time.sleep(1)

        self.ep.extractAadhaar()

    def tearDown(self):
        self.driver.close()

