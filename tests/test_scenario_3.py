import re
from pathlib import Path
import os
from typing import Match

from selenium import webdriver
from selenium.webdriver.remote.webelement import WebElement

from pages.main_page import MainPage
from pages.download_page import DownloadPage
from utils import wait_for_file_to_download



def test_three(browser: webdriver) -> None:
    link: str = 'https://sbis.ru/'
    main_page: MainPage = MainPage(browser, link, 10)
    main_page.open()

    browser.execute_script("window.scrollTo(0, document.body.scrollHeight)")

    download_local_versions: WebElement = main_page.should_be_download_local_versions()
    download_local_versions.click()

    download_page: DownloadPage = DownloadPage(browser, browser.current_url)

    sbis_plugin: WebElement = download_page.should_be_sbis_plugin()
    sbis_plugin.click()

    windows: WebElement = download_page.should_be_windows()
    windows.click()

    download_exe: WebElement = download_page.should_be_download_exe()
    download_exe.click()

    file_name: str = "sbisplugin-setup-web.exe"
    path_to_file: Path = Path.cwd() / 'download/'/ str(file_name)

    text_link_download: str = download_exe.text
    pattern: str = r"(\d+\.\d+)"
    match: Match = re.search(pattern, text_link_download)
    assert match, "Не указан размер файла 'СБИС Плагин Веб-установщик' в ссылке для скачивания"
    assert wait_for_file_to_download(path_to_file=str(path_to_file)), "В директории нет файла!"

    if match:
        size_file_from_link: str = match.group(1)
        if path_to_file.is_file():
            file_size_byte: int = os.path.getsize(path_to_file)
            file_size_mb: float = round((file_size_byte / (1024 * 1024)), 2)
            assert (str(file_size_mb)) == size_file_from_link, "Неправильный размер файла"

    clear_download(path_to_file=str(path_to_file))



