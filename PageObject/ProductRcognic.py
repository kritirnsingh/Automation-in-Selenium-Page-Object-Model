from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ProductPage:
    # A class for all Product page locators

    Click_Product_xpath = "//*[@id='header-menu-list']/div[1]/a"
    Extract_Aadhar_card_xpath = "//a[contains(text(),'Extract Aadhaar card')]"

    def __init__(self, driver):
        self.driver = driver

    # Contact page action methods come here
    # Clicks on Product Option
    def clickOnProduct(self):
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, self.Click_Product_xpath))).click()

    # Clicks on Extract Aadhaar card
    def extractAadhaar(self):
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, self.Extract_Aadhar_card_xpath))).click()