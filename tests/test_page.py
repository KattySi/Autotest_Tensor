from time import  sleep
from typing import List

from selenium import webdriver
from selenium.webdriver.remote.webelement import WebElement

from pages.main_page import MainPage
from pages.contacts_page import ContactsPage
from pages.tensor_page import TensorPage
from pages.about_page import AboutPage



def test_one(browser: webdriver) -> None:
    link: str = 'https://sbis.ru/'
    main_page: MainPage = MainPage(browser,link, 10)
    main_page.open()
    sleep(0.44)
    contacts: WebElement = main_page.should_be_contacts()
    contacts.click()
    contacts_mote: WebElement = main_page.should_be_contacts_more()
    contacts_mote.click()
    sleep(0.44)
    contacts_page: ContactsPage = ContactsPage(browser, browser.current_url)
    banner: WebElement = contacts_page.should_be_banner()
    banner.click()
    sleep(2)

    main_window: str = browser.window_handles[0]
    tensor_window: str = browser.window_handles[1]
    browser.switch_to.window(tensor_window)
    tensor: TensorPage = TensorPage(browser, browser.current_url)

    strength_in_people: WebElement = tensor.should_be_strength_in_people()
    browser.execute_script("arguments[0].scrollIntoView();", strength_in_people)
    sleep(2)
    more_details: WebElement = tensor.should_be_more_details()
    more_details.click()
    sleep(2)
    about: AboutPage = AboutPage(browser, browser.current_url)
    img1: WebElement = about.should_be_img_1()
    browser.execute_script("arguments[0].scrollIntoView();", img1)
    img2: WebElement = about.should_be_img_2()
    img3: WebElement = about.should_be_img_3()
    img4: WebElement = about.should_be_img_4()
    images: List[WebElement] = [img1, img2, img3, img4]
    height: int = img1.size["height"]
    width: int = img1.size["width"]

    for img in images[1:]:
        assert img.size["height"] == height, 'Высота картинок не совпадает'
        assert img.size["width"] == width, 'Ширина картинок не совпадает'
    sleep(2)