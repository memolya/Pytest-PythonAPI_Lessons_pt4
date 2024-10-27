from utils.api_reqres import ReqresStatusCode

"""Получение статус-кода"""
class TestGetStatus():
    def test_get_status(self):
        print('Метод GET: ')
        get_status = ReqresStatusCode.get_status_code()

        """Проверяем статус-код"""
        print('Статус код: ' + str(get_status.status_code))
