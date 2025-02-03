import pytest
from selenium import webdriver
import chromedriver_autoinstaller
from pages.trendyol_page import TrendyolPage
import time

@pytest.fixture
def driver():
    # ChromeDriver'ı otomatik olarak yükle
    chromedriver_autoinstaller.install()
    
    # Chrome ayarlarını yapılandır
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--start-maximized")  # Tarayıcıyı tam ekran başlat
    
    # WebDriver'ı başlat
    driver = webdriver.Chrome(options=chrome_options)
    yield driver
    # Test bitiminde tarayıcıyı kapat
    driver.quit()

def test_search_and_add_to_cart(driver):
    # TrendyolPage nesnesini oluştur
    trendyol_page = TrendyolPage(driver)
    
    # Ana sayfaya git
    trendyol_page.navigate_to_home()
    
    # Macbook ara
    trendyol_page.search_product("macbook")
    
    # İlk ürünü seç
    trendyol_page.select_first_product()
    
    # Sepete ekle
    trendyol_page.add_to_cart()
    
    # Sepete git
    trendyol_page.go_to_cart()
    
    # Sepete eklemenin başarılı olduğundan emin olmak için kısa bir bekleme
    time.sleep(2)
