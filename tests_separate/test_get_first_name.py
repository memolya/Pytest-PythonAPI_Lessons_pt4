from utils.api_lesson7 import ReqresApiFirstName

"""GET first name"""
class TestGetFirstName():
    def test_get_first_name(self):
        print('Метод GET: ')
        result_get = ReqresApiFirstName.get_first_name()
        check_get = result_get.json()
        first_name = check_get.get('first_name')
        print(first_name)
