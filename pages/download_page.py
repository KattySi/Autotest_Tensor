from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement

from pages.base_page import BasePage
from pages.locators import DownloadLocators



class DownloadPage(BasePage):
    def __init__(self, browser: WebDriver, url: str, timeout: int = 10) -> None:
        super().__init__(browser, url, timeout)


    def should_be_sbis_plugin(self) -> WebElement:
        assert (sbis_plugin := self.is_element_present(DownloadLocators.SBIS_PLUGIN)), "нет кнопки СБИС Плагин"
        return sbis_plugin

    def should_be_windows(self) -> WebElement:
        assert (windows := self.is_element_present(DownloadLocators.WINDOWS)), "нет вкладки windows"
        return windows

    def should_be_download_exe(self) -> WebElement:
        assert (download_exe := self.is_element_present(DownloadLocators.DOWNLOAD_EXE)), "нет ссылки на файл"
        return download_exe

