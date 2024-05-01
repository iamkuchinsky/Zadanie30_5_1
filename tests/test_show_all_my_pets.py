from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as WDW
from selenium.webdriver.support import expected_conditions as EC
from main import driver


def test_show_all_my_pets(driver):
    # Вводим email
    driver.find_element(By.ID, 'email').send_keys('dsgf5fsddaw@gff.ru')
    # Вводим пароль
    driver.find_element(By.ID, 'pass').send_keys('12345')
    # Нажимаем на кнопку входа в аккаунт
    driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
    # Переходим во вкладку "Мои питомцы"
    driver.find_element(By.XPATH, '//*[@id="navbarNav"]/ul/li[1]/a').click()
    # Проверяем, что мы оказались на странице пользователя по имени пользователя "ыфыф4343", используя явное ожидание
    assert WDW(driver, 5).until(EC.presence_of_element_located((By.TAG_NAME, 'h2'))).text == "ыфыф4343"
    # Считаем количество питомцев из боковой панели
    pets_number = driver.find_element(By.XPATH, '//div[@class=".col-sm-4 left"]').text.split('\n')[1].split(': ')[1]
    # Считаем количество питомцев из таблицы
    pets_count = driver.find_elements(By.XPATH, '//table[@class="table table-hover"]/tbody/tr')
    # Проверяем, что количество питомцев из таблицы и из боковой панели совпадают
    assert int(pets_number) == len(pets_count)