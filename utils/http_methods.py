import requests

"""Список HTTP методов"""
class Http_methods:
    headers = {'Content-Type': 'application/json'}
    cookie = ""

    @staticmethod #вызов метода где угодно в отрыве от класса Http_methods
    def get(url):
        result = requests.get(url, headers=Http_methods.headers, cookies=Http_methods.cookie)
        return result

    @staticmethod
    def post(url, body):
        result = requests.post(url, json=body, headers=Http_methods.headers, cookies=Http_methods.cookie)
        return result

    @staticmethod
    def put(url, body):
        result = requests.put(url, json=body, headers=Http_methods.headers, cookies=Http_methods.cookie)
        return result

    @staticmethod
    def delete(url, body):
        result = requests.delete(url, json=body, headers=Http_methods.headers, cookies=Http_methods.cookie)
        return result