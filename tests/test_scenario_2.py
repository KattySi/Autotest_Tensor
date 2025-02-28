import os
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.remote.webelement import WebElement

from pages.main_page import MainPage
from pages.contacts_page import ContactsPage


load_dotenv()

def test_two(browser: webdriver) -> None:
    link: str = 'https://sbis.ru/'
    main_page: MainPage = MainPage(browser, link, 10)
    main_page.open()
    contacts: WebElement = main_page.should_be_contacts()
    contacts.click()
    contacts_more: WebElement = main_page.should_be_contacts_more()
    contacts_more.click()
    contacts_page: ContactsPage = ContactsPage(browser, browser.current_url)
    region: WebElement = contacts_page.should_be_region()

    selected_region = os.getenv("REGION")
    selected_city = os.getenv("CITY")
    assert region.text == selected_region, "Неправильно определилось местоположение"

    list_partners: WebElement = contacts_page.should_be_list_partners()
    assert list_partners.text == selected_city, "Не правильный список партнеров"

    region.click()
    kamchatka: WebElement = contacts_page.should_be_kamchatka()
    kamchatka.click()
    contacts_page.should_be_present_text_new_region()
    new_list_partners: WebElement = contacts_page.should_be_list_partners()
    assert new_list_partners.text == "Петропавловск-Камчатский", "Список партнеров не Камчатка"

    new_url: str = browser.current_url
    assert "41-kamchatskij-kraj" in new_url, "В адресе нет Камчатского края"

    page_title: str = browser.title
    assert "Камчатский край" in page_title, "В тексте заголовка нет Камчатского края"







