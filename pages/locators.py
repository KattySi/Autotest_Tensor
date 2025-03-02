from selenium.webdriver.common.by import By


class MainPageLocators:
    '''Локаторы главной страницы'''
    CONTACTS: tuple = (By.CSS_SELECTOR, "ul.sbisru-Header__menu div.sbisru-Header__menu-link")
    CONTACTS_MORE: tuple = (By.CSS_SELECTOR, "ul.sbisru-Header__menu a.sbisru-link.sbis_ru-link span")
    DOWNLOAD_LOCAL_VERSIONS: tuple = (By.XPATH, "//a[text()='Скачать локальные версии']")


class ContactsLocators:
    '''Локаторы главной страницы'''
    BANNER: tuple = (By.CSS_SELECTOR, "div#contacts_clients div.sbisru-Contacts__border-left img")
    REGION: tuple = (By.CSS_SELECTOR, "div.sbis_ru-container.sbisru-Contacts__relative span span")
    LIST_PARTNERS: tuple = (By.CSS_SELECTOR, "div#contacts_list div.sbisru-Contacts-List__col div[name='itemsContainer'] div#city-id-2")
    KAMCHATKA: tuple = (By.XPATH, "//span[text()='41 Камчатский край']")


class TensorLocators:
    '''Локаторы страницы tensor'''
    STRENGTH_IN_PEOPLE: tuple = (By.CSS_SELECTOR, "div.tensor_ru-Index__block4-content p:nth-of-type(1)")
    MORE_DETAILS: tuple = (By.CSS_SELECTOR, "div.tensor_ru-Index__block4-bg p:nth-child(4) a")


class AboutLocators:
    '''Локаторы страницы О компании'''
    IMG_1: tuple = (By.CSS_SELECTOR, "div.tensor_ru-container.tensor_ru-About__block3 div.s-Grid-container div.s-Grid-col:nth-of-type(1) img")
    IMG_2: tuple = (By.CSS_SELECTOR, "div.tensor_ru-container.tensor_ru-About__block3 div.s-Grid-container div.s-Grid-col:nth-of-type(2) img")
    IMG_3: tuple = (By.CSS_SELECTOR, "div.tensor_ru-container.tensor_ru-About__block3 div.s-Grid-container div.s-Grid-col:nth-of-type(3) img")
    IMG_4: tuple = (By.CSS_SELECTOR, "div.tensor_ru-container.tensor_ru-About__block3 div.s-Grid-container div.s-Grid-col:nth-of-type(4) img")


class DownloadLocators:
    '''Локаторы страницы download'''
    SBIS_PLUGIN: tuple = (By.XPATH, "//div[text()='Saby Plugin']")
    WINDOWS: tuple = (By.XPATH, "//span[text()='Windows']")
    DOWNLOAD_EXE: tuple = (By.XPATH, "//a[contains(text(), 'Скачать (Exe')]")





