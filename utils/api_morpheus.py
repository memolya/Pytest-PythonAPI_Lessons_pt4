from utils.http_methods import Http_methods

"""Методы для тестирования https://reqres.in/api/users"""

base_url = 'https://reqres.in/api/users'  #параметр для всех запросов

class Reqres_api():

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


