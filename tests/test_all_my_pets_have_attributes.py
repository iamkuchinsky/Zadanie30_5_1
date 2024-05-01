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
    # Считаем количество питомцев из таблицы
    pets_count = driver.find_elements(By.XPATH, '//table[@class="table table-hover"]/tbody/tr')

    for row in pets_count:
        # Получаем значения Имени, возраста и породы питомца из каждой строки
        name = row.find_element(By.XPATH, './td[2]').text
        age = row.find_element(By.XPATH, './td[4]').text
        breed = row.find_element(By.XPATH, './td[3]').text

        # Проверяем, что Имя, возраст и порода не пустые
        assert name.strip() != "", "Имя питомца не указано"
        assert age.strip() != "", "Возраст питомца не указан"
        assert breed.strip() != "", "Порода питомца не указана"
