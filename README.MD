В данном задании реализованы тест-кейсы для сайта https://petfriends.skillfactory.ru/.

Список тест-кейсов (папка tests):
1) Test_show_all_pets - Показывает всех питомцев и затем проверяет список моих питомцев
2) test_show_all_my_pets - Показывает список всех питомцев пользователя и затем проверяет, что количество питомцев в таблице совпадает с количеством питомцев в боковой панели.
3) test_photo_pets - Проверяет, список фото питомцев и то, что как минимум у половины питомцев есть фотография.
4) test_all_my_pets_have_attributes - Проверяет, что в списке питомцев пользователя у всех питомцев есть атрибуты "Имя", "Возраст" и "Порода"
5) test_different_names - Проверяет, что у все питомцев уникальные имена
6) test_non_repitive_names - Проверяет, что нет одинаковых питомцев (со одинаковыми значениями атрибутов "Имя", "Возраст" и "Порода"

В файле main.py описана фикстура, а также используется driver.implicitly_wait(10), тем самым покрывается условия использования явных ожиданий в каждом тесте.
Также в тестах используются элементы класса WebDriverWait.
