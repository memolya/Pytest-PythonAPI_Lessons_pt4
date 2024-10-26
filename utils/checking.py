"""Методы для проверки ответов запросов"""
import json
from requests import Response
class Checking():

    """Метод для проверки статус-кода"""
    @staticmethod #для staticmethod не нужен параметр self в методах, тк нет привязки к классу
    def check_status_code(response: Response, status_code): #status - ожидаемый статус код в assert
        assert status_code == response.status_code #слева заданный ожидаемый статус-код, справа - статус-код из ответа
        if response.status_code == status_code:
            print('Успешно. Статус-код = ' + str(response.status_code))
        else:
            print('Провал. Статус-код = ' + str(response.status_code))

    """Метод для проверки обязательных полей"""
    @staticmethod
    def check_json_token(result, expected_value):
        fields = json.loads(result.text) #строка, которую получаем, этим методом преобразуется в json
        assert list(fields) == expected_value, 'ОШИБКА, Список полей не совпадает' #преобразуем json из fields в список
        print('Все поля присутствуют.')

    """Метод для проверки значений полей"""
    @staticmethod
    def check_json_value(result, field_name, expected_value):
        check = result.json()
        check_info = check.get(field_name)
        assert check_info == expected_value
        print(field_name + ' верен.')

    """Метод для проверки значений полей по заданному слову"""
    @staticmethod
    def check_json_word_in_value(result, field_name, search_word):
        check = result.json()
        check_info = check.get(field_name)
        if search_word in check_info:
            print('Слово ' + search_word + ' присутствует.')
        else:
            print('Слово ' + search_word + ' отсутствует.')