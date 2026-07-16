from selenium.webdriver.common.by import By

class WelcomePage:
    def __init__(self,driver):
        self.driver = driver

    def register_link(self):
        self.driver.find_element(By.XPATH, "//a[text()='Register']").click()

    def login_link(self):
        self.driver.find_element(By.XPATH, "//a[text()='Log in']").click()

    def search_bar(self):
        self.driver.find_element(By.XPATH, "//input[@value='Search store']").send_keys("books")

    def search_button(self):
        self.driver.find_element(By.XPATH, "//input[@value='Search']").click()

    def shopping_cart(self):
        self.driver.find_element(By.XPATH, "//span[text()='Shopping cart']").click()