from pathlib import Path
import pytest
import shutil

from selenium.webdriver.remote.webdriver import WebDriver
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service


DOWNLOAD_DIR: Path = Path.cwd() / 'download/'

@pytest.fixture(scope='module')
def browser():
    download_in_directory: Path = Path.cwd() / 'download'
    chrome_options: Options = Options()
    chrome_options.add_experimental_option(
        "prefs", {
        "download.default_directory": str(download_in_directory),
    })
    browser: WebDriver = webdriver.Chrome(options=chrome_options)
    yield browser
    browser.quit()

@pytest.fixture(scope='session')
def cleanup_download():
    if DOWNLOAD_DIR.is_dir():
        shutil.rmtree(str(DOWNLOAD_DIR))
    DOWNLOAD_DIR.mkdir(parents=True, exist_ok=True)
    yield DOWNLOAD_DIR
    shutil.rmtree(str(DOWNLOAD_DIR))
