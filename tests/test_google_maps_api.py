import json

from utils.api_google_maps import Google_maps_api
from utils.checking import Checking

"""Создание, изменение и удаление новой локации"""

class Test_create_place():
    def test_create_new_place(self):
        print('Метод POST: ')
        result_post = Google_maps_api.create_new_place()
        check_post = result_post.json()
        place_id = check_post.get('place_id')
        token = json.loads(result_post.text) #получение полей для check token
        # print(list(token))
        Checking.check_json_token(result_post,['status', 'place_id', 'scope', 'reference', 'id'])
        Checking.check_json_value(result_post, 'status','OK')

        """Проверка статус-кода методом checking"""
        Checking.check_status_code(result_post, 200) #проверяем result_post на соответствие 200
        print(result_post.status_code) #проверка реального статус-кода

        print('Метод GET POST: ')
        result_get_post = Google_maps_api.get_new_place(place_id)
        Checking.check_status_code(result_get_post, 200)
        # token = json.loads(result_get_post.text)  # получение полей для check token
        # print(list(token))
        Checking.check_json_token(result_get_post, ['location', 'accuracy', 'name', 'phone_number',
                                                    'address', 'types', 'website', 'language'])
        Checking.check_json_value(result_get_post, 'address', '29, side layout, cohen 09')

        print('Метод PUT: ')
        result_put = Google_maps_api.put_new_place(place_id)
        Checking.check_status_code(result_put, 200)
        Checking.check_json_token(result_put, ['msg'])
        Checking.check_json_value(result_put, 'msg', 'Address successfully updated')

        print('Метод GET PUT: ')
        result_get_put = Google_maps_api.get_new_place(place_id)
        Checking.check_status_code(result_get_put, 200)
        Checking.check_json_token(result_get_put, ['location', 'accuracy', 'name', 'phone_number',
                                                    'address', 'types', 'website', 'language'])
        Checking.check_json_value(result_get_put, 'address', '100 Lenina street, RU')

        print('Метод DELETE: ')
        result_delete = Google_maps_api.delete_new_place(place_id)
        Checking.check_status_code(result_delete, 200)
        # token = json.loads(result_delete.text)  # получение полей для check token
        # print(list(token))
        Checking.check_json_token(result_delete,['status'])
        Checking.check_json_value(result_delete, 'status', 'OK')

        print('Метод GET DELETE: ')
        result_get_delete = Google_maps_api.get_new_place(place_id)
        Checking.check_status_code(result_get_delete, 404)
        Checking.check_json_token(result_get_delete, ['msg'])
        Checking.check_json_word_in_value(result_get_delete, 'msg', 'failed')

        print('Тестирование создания, изменения и удаления новой локации прошло успешно.')



