from utils.http_methods import Http_methods

"""Методы для тестирования "https://reqres.in/api/"""

url_1 = "https://reqres.in/api/users/7"
url_2 = "https://reqres.in/api/users?page=2"
url_3 = "https://reqres.in/api/users/15"
url_4 = "https://reqres.in/api/unknown/2"

class ReqresApiFirstName():
    """Метод для отправки GET first name"""
    @staticmethod
    def get_first_name():
        print(url_1)
        result_get = Http_methods.get(url_1)
        print(result_get.text)
        return result_get

class FindSixSymbols():
    """Метод для подсчета 6 символов в поле"""
    @staticmethod
    def get_six_symbols():
        print(url_2)
        result_get_2 = Http_methods.get(url_2)
        print(result_get_2.text)
        return result_get_2
class ReqresStatusCode():
    """Метод для получения статус-кода"""
    @staticmethod
    def get_status_code():
        print(url_3)
        result_get_3 = Http_methods.get(url_3)
        print(result_get_3)
        return result_get_3

class ReqresDataFields():
    """Метод для получения полей data"""
    @staticmethod
    def get_data_fields():
        print(url_4)
        result_get_4 = Http_methods.get(url_4)
        print(result_get_4)
        return result_get_4