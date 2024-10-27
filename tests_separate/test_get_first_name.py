from utils.api_reqres import ReqresApiFirstName

"""GET first name"""
class TestGetFirstName():
    def test_get_first_name(self):
        print('Метод GET: ')
        result_get = ReqresApiFirstName.get_first_name()

        get_status_json = result_get.json()
        data = get_status_json.get('data')
        print(data)

        first_name = data.get('first_name')
        print('Имя: ', first_name)