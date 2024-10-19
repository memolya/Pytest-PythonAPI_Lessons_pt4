from utils.api_morpheus import ReqresLogin

"""Логин"""

class TestLogin():
    def test_post_login(self):
        print('Метод POST 3: ')
        result_post_3 = ReqresLogin.login()

        """Проверяем статус-код"""
        print('Статус код: ' + str(result_post_3.status_code))
