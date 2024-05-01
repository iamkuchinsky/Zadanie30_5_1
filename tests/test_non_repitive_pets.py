import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as WDW
from selenium.webdriver.support import expected_conditions as EC
from main import driver


def test_no_duplicate_pets(driver):
    # Вводим email
    driver.find_element(By.ID, 'email').send_keys('dsgf5fsddaw@gff.ru')
    # Вводим пароль
    driver.find_element(By.ID, 'pass').send_keys('12345')
    # Нажимаем на кнопку входа в аккаунт
    driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
    # Проверяем, что мы оказались на главной странице пользователя
    assert WDW(driver, 5).until(EC.presence_of_element_located((By.TAG_NAME, 'h1'))).text == "PetFriends"
    time.sleep(1)
    # Переходим во вкладку "Мои питомцы"
    driver.find_element(By.XPATH, '//*[@id="navbarNav"]/ul/li[1]/a').click()

    # Находим все элементы с именами, породами и возрастами питомцев
    pet_elements = driver.find_elements(By.XPATH, '//*[@id="all_my_pets"]/table[1]/tbody[1]/tr')

    pet_info = []
    for pet_element in pet_elements:
        name = pet_element.find_element(By.XPATH, './td[1]').text
        breed = pet_element.find_element(By.XPATH, './td[2]').text
        age = pet_element.find_element(By.XPATH, './td[3]').text
        pet_info.append((name, breed, age))

    # Проверяем, что количество питомцев больше 0
    assert len(pet_info) > 0, "Нет доступных питомцев"

    # Проверяем, что нет повторяющихся питомцев (одинаковое имя, порода и возраст)
    for i in range(len(pet_info)):
        for j in range(i + 1, len(pet_info)):
            assert pet_info[i] != pet_info[j], f"Повторяющиеся питомцы: {pet_info[i]} и {pet_info[j]}"