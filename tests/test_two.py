from time import  sleep
from selenium import webdriver

from selenium.webdriver.remote.webelement import WebElement

from pages.main_page import MainPage
from pages.contacts_page import ContactsPage



def test_two(browser: webdriver) -> None:
    link: str = 'https://sbis.ru/'
    main_page: MainPage = MainPage(browser, link, 10)
    main_page.open()
    sleep(0.44)
    contacts: WebElement = main_page.should_be_contacts()
    contacts.click()
    contacts_mote: WebElement = main_page.should_be_contacts_more()
    contacts_mote.click()
    sleep(1.5)
    contacts_page: ContactsPage = ContactsPage(browser, browser.current_url)
    region: WebElement = contacts_page.should_be_region()
    assert region.text ==  "Нижегородская обл.", "Неправильно определилось местоположение"

    list_partners: WebElement = contacts_page.should_be_list_partners()
    assert list_partners.text == "Нижний Новгород", "Не правильный список партнеров"
    region.click()
    sleep(2)
    kamchatka: WebElement = contacts_page.should_be_kamchatka()
    kamchatka.click()
    sleep(5)

    new_region: WebElement = contacts_page.should_be_region()
    new_list_partners: WebElement = contacts_page.should_be_list_partners()
    assert new_region.text == "Камчатский край", "Не Камчатский Край"
    assert new_list_partners.text == "Петропавловск-Камчатский", "Список партнеров не Камчатка"
    new_url: str = browser.current_url
    assert "41-kamchatskij-kraj" in new_url, "В адресе нет Камчатского края"
    page_title: str = browser.title
    assert "Камчатский край" in page_title, "В тексте заголовка нет Камчатского края"







