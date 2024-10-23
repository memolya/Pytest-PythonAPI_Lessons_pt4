from utils.api_morpheus import ReqresUpdate

"""Обновление данных"""

class TestReqresUpdateData():
    def test_reqres_update_data(self):
        print('Метод PUT:')
        result_put = ReqresUpdate.update_info()
        print(result_put.json())


