from utils.api_morpheus import ReqresGet
import json

class TestGetFields():
    """Получение содержимого в json ответа"""
    def test_get_fields(self):
        result_get = ReqresGet.get_data_1()
        fields = json.loads(result_get.text)
        print(list(fields))

    def test_get_fields_2(self):
        result_get_2 = ReqresGet.get_data_2()
        fields_2 = json.loads(result_get_2.text)
        print(list(fields_2))