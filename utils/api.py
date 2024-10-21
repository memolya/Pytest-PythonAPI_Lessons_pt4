from utils.http_methods import Http_methods

"""Методы для тестирования Google maps API"""

base_url = 'https://rahulshettyacademy.com'  #параметр для всех запросов
key = '?key=qaclick123'                      #параметр для всех запросов

class Google_maps_api():

    """Создание новой локации"""
    @staticmethod
    def create_new_place():

        json_for_create_new_place = {
            "location": {
                "lat": -38.383494,
                "lng": 33.427362
            }, "accuracy": 50,
            "name": "Frontline house",
            "phone_number": "(+91) 983 893 3937",
            "address": "29, side layout, cohen 09",
            "types": [
                "shoe park",
                "shop"
            ],
            "website": "http://google.com",
            "language": "French-IN"

        }

        post_resource = "/maps/api/place/add/json"
        post_url = base_url + post_resource + key
        print(post_url)
        result_post = Http_methods.post(post_url, json_for_create_new_place)
        print(result_post.text)
        return result_post

    """Метод для проверки новой локации"""
    @staticmethod
    def get_new_place(place_id): #place_id для этого метода берется из прошлого метода create_new_place
        get_resource = '/maps/api/place/get/json' #Ресурс метода GET
        get_url = base_url + get_resource + key + "&place_id=" + place_id
        print(get_url)
        result_get = Http_methods.get(get_url)
        print(result_get.text)
        return result_get