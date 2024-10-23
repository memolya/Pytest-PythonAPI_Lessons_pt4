from utils.http_methods import Http_methods

"""Методы для тестирования https://petstore.swagger.io"""

url = "https://petstore.swagger.io/v2/user/createWithArray"
url_2 = "https://petstore.swagger.io/v2/pet"
url_3 = "https://petstore.swagger.io/v2/store/order/1"

class SendDataPetstore():
    @staticmethod
    def send_data():
        json_post = [
            {
                "id": 1,
                "username": "beb",
                "firstName": "Meh",
                "lastName": "Kek",
                "email": "123@rfe.com",
                "password": "348533",
                "phone": "88005553535",
                "userStatus": 0
            }
        ]
        print(url)
        result_post = Http_methods.post(url, json_post)
        print(result_post.text)
        return result_post

    """Метод для изменения данных"""
    @staticmethod
    def update_data():
        json_put = [
            {
                "id": 1,
                "category": {
                    "id": 1,
                    "name": "Bobik"
                },
                "name": "doggie",
                "photoUrls": [
                    "string"
                ],
                "tags": [
                    {
                        "id": "1",
                        "name": "Bob"
                    }
                ],
                "status": "available"
            }
        ]
        print(url_2)
        result_put = Http_methods.put(url_2, json_put)
        print(result_put.text)
        return result_put

    """Метод для удаления данных"""
    @staticmethod
    def delete_data():
        print(url_3)
        json_for_delete_data = {
                "id": 1,
                "username": "beb",
                "firstName": "Meh",
                "lastName": "Kek",
                "email": "123@rfe.com",
                "password": "348533",
                "phone": "88005553535",
                "userStatus": 0
            }
        result_delete = Http_methods.delete(url_3, json_for_delete_data)
        print(result_delete.text)
        return result_delete
