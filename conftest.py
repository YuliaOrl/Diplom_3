import pytest
from data import *
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions

@pytest.fixture(params=['chrome', 'firefox'])
def driver(request):
    if request.param == 'chrome':
        options = ChromeOptions()
        options.add_argument('--window-size=1280,720')
        driver = webdriver.Chrome(options=options)
    elif request.param == 'firefox':
        options = FirefoxOptions()
        options.add_argument('--window-size=1280,720')
        driver = webdriver.Firefox(options=options)
    yield driver
    driver.quit()