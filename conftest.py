from pathlib import Path
import pytest

from selenium.webdriver.remote.webdriver import WebDriver
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service



@pytest.fixture(scope='session')
def browser():
    chrome_driver_path: str = '/usr/local/bin/chromedriver'
    download_in_directory: Path = Path.cwd() / 'Download'
    chrome_options: Options = Options()
    chrome_options.add_experimental_option(
        "prefs", {
        "download.default_directory": str(download_in_directory),
    })

    service: Service = Service(chrome_driver_path)
    browser: WebDriver = webdriver.Chrome(options=chrome_options, service=service)
    yield browser
    browser.quit()


