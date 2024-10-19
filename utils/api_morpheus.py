from utils.http_methods import Http_methods

"""Методы для тестирования https://reqres.in/api/"""

base_url = 'https://reqres.in/api/users'
base_url_2 = 'https://reqres.in/api/register'
login_url = "https://reqres.in/api/login"

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
