from utils.http_methods import Http_methods

"""Методы для тестирования https://reqres.in/api/"""

base_url = 'https://reqres.in/api/users'
base_url_2 = 'https://reqres.in/api/register'
login_url = "https://reqres.in/api/login"
base_url_3 = "https://reqres.in/api/users/3"
base_url_4 = "https://reqres.in/api/users/2"
base_url_5 = "https://catfact.ninja/fact?max_length=100"
base_url_6 = "https://catfact.ninja/facts?max_length=100&limit=5"
base_url_7 = "https://dog.ceo/api/breeds/image/random/100"
base_url_8 = "https://dog.ceo/api/breed/hound/images"

url_1 = "https://reqres.in/api/users/7"
url_2 = "https://reqres.in/api/users?page=2"
url_3 = "https://reqres.in/api/users/15"
url_4 = "https://reqres.in/api/unknown/2"

class ReqresApi():
    """Отправка данных"""

    @staticmethod
    def send_data():
        json_post = {
            "name": "morpheus",
            "job": "leader"
        }

        print(base_url)
        result_post = Http_methods.post(base_url, json_post)
        print(result_post.text)
        return result_post

class ReqresRegister():
    """Отправка данных для post_creds"""

    @staticmethod
    def send_data2():
        json_post_2 = {
            "email": "eve.holt@reqres.in",
            "password": "pistol"
        }

        print(base_url_2)
        result_post_2 = Http_methods.post(base_url_2, json_post_2)
        print(result_post_2.text)
        return result_post_2
class ReqresLogin():
    """Логин в системе"""
    @staticmethod
    def login():
        json_post_3 = [
            {
                "username": "1",
                "email": "1@mail.ru",
                "password": "qwer1234"
            }
        ]

        print(login_url)
        result_post_3 = Http_methods.post(login_url, json_post_3)
        print(result_post_3.text)
        return result_post_3
class ReqresLogin_2():
    @staticmethod
    def login_2():
        json_post_4 = [
            {
                "email": "peter@klaven"
            }
        ]

        print(login_url)
        result_post_4 = Http_methods.post(login_url, json_post_4)
        print(result_post_4.text)
        return result_post_4

"""Для метода PUT"""
class ReqresUpdate():
    @staticmethod
    def update_info():
        json_put = [
            {
                "name": "morpheus",
                "job": "zion resident"
            }
        ]
        print(base_url_3)
        result_put = Http_methods.put(base_url_3, json_put)
        print(result_put.text)
        return result_put

    """Удаление данных"""
    @staticmethod
    def delete_info():
        json_delete = [
            {
                "name": "morpheus",
                "job": "zion resident"
            }
        ]
        print(base_url_4)
        result_delete = Http_methods.delete(base_url_4, json_delete)
        print(result_delete.text)
        return result_delete

class ReqresGet():
    """Получение данных"""
    @staticmethod
    def get_data_1():
        print(base_url_5)
        result_get = Http_methods.get(base_url_5)
        print(result_get.text)
        return result_get
    @staticmethod
    def get_data_2():
        print(base_url_6)
        result_get_2 = Http_methods.get(base_url_6)
        print(result_get_2.text)
        return result_get_2
    @staticmethod
    def get_data_3():
        print(base_url_7)
        result_get_3 = Http_methods.get(base_url_7)
        print(result_get_3.text)
        return result_get_3

    @staticmethod
    def get_data_4():
        print(base_url_8)
        result_get_4 = Http_methods.get(base_url_8)
        print(result_get_4.text)
        return result_get_4

class CheckJsonValue():
    """Метод для проверки длины массива в выбранном поле ответа"""

    @staticmethod
    def check_json_field_len(result, field_name):
        counter = 0
        check = result.json()
        check_info = check.get(field_name)

        for i in check_info:
            counter += 1
        print('Количество элементов в массиве: ' + str(counter))

    """Метод для проверки содержания слова в элементах массива в выбранном поле ответа"""
    @staticmethod
    def check_json_element_content(result, field_name, word):
        counter_2 = 0
        check = result.json()
        check_info = check.get(field_name)

        for i in check_info:
            if word in i:
                counter_2 += 1
        print('Количество элементов в массиве с заданным словом: ' + str(counter_2))
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
class ReqresApiFirstName():
    """Метод для отправки GET first name"""
    @staticmethod
    def get_first_name():
        print(url_1)
        result_get = Http_methods.get(url_1)
        print(result_get)
        return result_get
        # print(result_get.text)

        # check = result_get.json()
        # check_second_name = check.get(field_name)
        # print(check_second_name)