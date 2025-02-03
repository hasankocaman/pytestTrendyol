import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import cv2
import numpy as np
import os
from datetime import datetime
import time
from pages.trendyol_page import TrendyolPage

class VideoRecorder:
    def __init__(self, filename):
        if not os.path.exists('videos'):
            os.makedirs('videos')
        self.filename = f"videos/{filename}"
        self.fourcc = cv2.VideoWriter_fourcc(*'XVID')
        self.out = None
        self.recording = False

    def start(self, screen_size):
        self.recording = True
        self.out = cv2.VideoWriter(self.filename, self.fourcc, 20.0, screen_size)

    def capture_frame(self, screenshot):
        if self.recording and self.out:
            frame = cv2.imdecode(np.frombuffer(screenshot, np.uint8), cv2.IMREAD_COLOR)
            self.out.write(frame)

    def stop(self):
        if self.recording and self.out:
            self.recording = False
            self.out.release()

@pytest.fixture(scope="function")
def driver():
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")
    # chrome_options.add_argument("--headless")  # Uncomment for headless mode
    
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
    yield driver
    driver.quit()

def test_add_macbook_to_cart(driver):
    # Initialize video recorder
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    video_recorder = VideoRecorder(f"test_recording_{timestamp}.avi")
    video_recorder.start((1920, 1080))  # Adjust resolution as needed

    try:
        # Initialize page object
        trendyol_page = TrendyolPage(driver)

        # Test steps
        trendyol_page.navigate_to_home()
        trendyol_page.search_product("macbook")
        trendyol_page.select_first_product()
        trendyol_page.add_to_cart()
        trendyol_page.go_to_cart()

        # Capture video frames throughout the test
        while True:
            screenshot = driver.get_screenshot_as_png()
            video_recorder.capture_frame(screenshot)
            time.sleep(0.05)  # Adjust frame rate as needed

    except Exception as e:
        pytest.fail(f"Test failed: {str(e)}")
    finally:
        video_recorder.stop()
