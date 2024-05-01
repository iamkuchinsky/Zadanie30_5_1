import pytest
from selenium import webdriver


@pytest.fixture(autouse=True)
def driver():
    driver = webdriver.Chrome(executable_path='D:\chromedriver.exe')
    # Устанавливаем неявное ожидание в 10 секунд для установки драйвера
    driver.implicitly_wait(10)
    # Переходим на страницу авторизации
    driver.get('https://petfriends.skillfactory.ru/login')
    driver.maximize_window()

    yield driver

    driver.quit()
