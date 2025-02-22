from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from .base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import time

class TrendyolPage(BasePage):
    # Locators
    ACCEPT_COOKIES = (By.ID, "onetrust-accept-btn-handler")
    SEARCH_BOX = (By.CLASS_NAME, "V8wbcUhU")
    FIRST_PRODUCT = (By.CSS_SELECTOR, "div.p-card-wrppr")
    ADD_TO_CART_BUTTON = (By.CLASS_NAME, "add-to-basket")
    CART_ICON = (By.CLASS_NAME, "account-basket")
    OVERLAY = (By.CLASS_NAME, "overlay")
    
    def __init__(self, driver):
        super().__init__(driver)
        self.url = "https://www.trendyol.com"

    def navigate_to_home(self):
        self.driver.get(self.url)
        self.logger.info(f"Navigated to {self.url}")
        self.accept_cookies()

    def accept_cookies(self):
        try:
            self.click(self.ACCEPT_COOKIES)
            self.logger.info("Accepted cookies")
        except:
            self.logger.warning("Cookie acceptance button not found or not needed")

    def search_product(self, product_name):
        self.send_keys(self.SEARCH_BOX, product_name + Keys.RETURN)
        self.logger.info(f"Searched for product: {product_name}")
        time.sleep(2)  # Wait for search results to load

    def select_first_product(self):
        self.click(self.FIRST_PRODUCT)
        self.logger.info("Selected first product from search results")
        # Switch to new tab if opened
        self.driver.switch_to.window(self.driver.window_handles[-1])

    def add_to_cart(self):
        try:
            # Öncelikle overlay varsa kapat
            overlay = self.driver.find_element(By.CLASS_NAME, "overlay")
            if overlay.is_displayed():
                print("Overlay bulundu, kapatılıyor...")
                self.driver.execute_script("arguments[0].style.display='none';", overlay)
            
            # Şimdi "Sepete Ekle" butonuna tıkla
            self.click(self.ADD_TO_CART_BUTTON)
        except NoSuchElementException:
            print("Overlay bulunamadı, devam ediliyor...")
            self.click(self.ADD_TO_CART_BUTTON)

    def go_to_cart(self):
        self.click(self.CART_ICON)
        self.logger.info("Navigated to cart")
