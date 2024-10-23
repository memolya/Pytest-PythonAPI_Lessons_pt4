from utils.api_morpheus import ReqresApi, ReqresUpdate

"""Отправка новых данных"""
class TestPostUserdata():

    def test_post_userdata(self):

        print('Метод POST:')
        result_post = ReqresApi.send_data()

        """Проверяем статус-код"""
        print('Статус код: ' + str(result_post.status_code))

        """Проверяем тип данных в id"""
        check_post_jsn = result_post.json()  # получать ответ в json формате и значения определенных полей из него
        person_id = check_post_jsn.get('id')
        print('ID type: ', type(person_id))

    def test_delete_data(self):

        print('Метод DELETE:')
        result_delete = ReqresUpdate.delete_info()
        print('Статус код: ' + str(result_delete.status_code))

