from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import logging
import os
from datetime import datetime

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.logger = self._setup_logger()

    def _setup_logger(self):
        logger = logging.getLogger(self.__class__.__name__)
        if not logger.handlers:
            logger.setLevel(logging.INFO)
            formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
            
            # Create logs directory if it doesn't exist
            if not os.path.exists('logs'):
                os.makedirs('logs')
            
            file_handler = logging.FileHandler(f'logs/test_{datetime.now().strftime("%Y%m%d_%H%M%S")}.log')
            file_handler.setFormatter(formatter)
            logger.addHandler(file_handler)
        
        return logger

    def find_element(self, locator):
        try:
            element = self.wait.until(EC.presence_of_element_located(locator))
            self.logger.info(f"Found element with locator: {locator}")
            return element
        except TimeoutException:
            self.logger.error(f"Element not found with locator: {locator}")
            self.take_screenshot(f"element_not_found_{locator[1]}")
            raise

    def click(self, locator):
        element = self.find_element(locator)
        self.wait.until(EC.element_to_be_clickable(locator))
        element.click()
        self.logger.info(f"Clicked element with locator: {locator}")

    def send_keys(self, locator, text):
        element = self.find_element(locator)
        element.clear()
        element.send_keys(text)
        self.logger.info(f"Sent keys '{text}' to element with locator: {locator}")

    def take_screenshot(self, name):
        if not os.path.exists('screenshots'):
            os.makedirs('screenshots')
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        screenshot_path = f"screenshots/{name}_{timestamp}.png"
        self.driver.save_screenshot(screenshot_path)
        self.logger.info(f"Screenshot saved: {screenshot_path}")
        return screenshot_path
