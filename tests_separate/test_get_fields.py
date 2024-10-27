from utils.api_reqres import ReqresDataFields

"""Получение количества полей data"""

class TestDataFields():
    def test_data_fields(self):
        print('Метод GET: ')
        get_status = ReqresDataFields.get_data_fields()
        get_status_json = get_status.json()
        data = get_status_json.get('data')
        print(data)

        """Считаем кол-во полей"""
        # print(type(data))
        print(len(data))