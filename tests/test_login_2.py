from utils.api_morpheus import ReqresLogin_2

"""Логин 2"""

class TestLogin():
    def test_post_login(self):
        print('Метод POST 4: ')
        result_post_4 = ReqresLogin_2.login_2()

        """Проверяем статус-код"""
        print('Статус код: ' + str(result_post_4.status_code))