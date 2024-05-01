from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as WDW
from selenium.webdriver.support import expected_conditions as EC
from main import driver


def test_non_repitive_pets(driver):
    # Вводим email
    driver.find_element(By.ID, 'email').send_keys('dsgf5fsddaw@gff.ru')
    # Вводим пароль
    driver.find_element(By.ID, 'pass').send_keys('12345')
    # Нажимаем на кнопку входа в аккаунт
    driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
    # Проверяем, что мы оказались на главной странице пользователя
    assert WDW(driver, 5).until(EC.presence_of_element_located((By.TAG_NAME, 'h1'))).text == "PetFriends"
    # Переходим во вкладку "Мои питомцы"
    driver.find_element(By.XPATH, '//*[@id="navbarNav"]/ul/li[1]/a').click()
    # Находим все элементы с именами питомцев
    pet_elements = driver.find_elements(By.XPATH, '//*[@id="all_my_pets"]/table[1]/tbody[1]/tr/td[1]')

    pet_names = []
    for pet_element in pet_elements:
        pet_names.append(pet_element.text)

    # Проверяем, что количество имен питомцев больше 0
    assert len(pet_names) > 0, "Нет доступных питомцев"

    # Проверяем, что все имена питомцев разные
    assert len(pet_names) == len(set(pet_names)), "Имеются повторяющиеся имена"
