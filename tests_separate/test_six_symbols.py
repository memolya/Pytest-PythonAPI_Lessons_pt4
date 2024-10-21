from utils.api_lesson7 import FindSixSymbols
dict = []

"""GET поле 6 символов"""
class TestGetSixSymbols():
    def test_get_six_symbols(self):
        print('Метод GET: ')
        result_get_2 = FindSixSymbols.get_six_symbols()
        check_get_2 = result_get_2.json()
        dict.append(check_get_2)
