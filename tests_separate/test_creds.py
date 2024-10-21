from utils.api_morpheus import ReqresRegister

"""Отправка кредов"""

class TestPostCreds():
    def test_post_creds(self): #обязательно включать test в название класса для распознавания pycharm

        print('Метод POST 2:')
        result_post_2 = ReqresRegister.send_data2()

        """Проверяем статус-код"""
        print('Статус код: ' + str(result_post_2.status_code))

        """Проверяем кол-во символов поля token"""
        check_post_2_jsn = result_post_2.json()
        token = check_post_2_jsn.get('token')
        print('Длина токена: ', len(token))
