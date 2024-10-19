from utils.http_methods import Http_methods

"""Методы для тестирования https://petstore.swagger.io"""

url = "https://petstore.swagger.io/v2/user/createWithArray"

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
