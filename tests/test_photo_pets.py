import time
from selenium.webdriver.common.by import By
from main import driver


def test_photo_pets(driver):
    # Вводим email
    driver.find_element(By.ID, 'email').send_keys('dsgf5fsddaw@gff.ru')
    # Вводим пароль
    driver.find_element(By.ID, 'pass').send_keys('12345')
    # Нажимаем на кнопку входа в аккаунт
    driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
    time.sleep(1)
    # Переходим во вкладку "Мои питомцы"
    driver.find_element(By.XPATH, '//*[@id="navbarNav"]/ul/li[1]/a').click()
    # Считаем количество питомцев из таблицы
    pets_count = driver.find_elements(By.XPATH, '//table[@class="table table-hover"]/tbody/tr')
    # Находим питомцев у которых есть фото
    image_count = driver.find_elements(By.XPATH, '//img[starts-with(@src, "data:image/")]')
    # Проверяем что фотографии имеются более чем у половины питомцев
    assert len(image_count) > len(pets_count) / 2
