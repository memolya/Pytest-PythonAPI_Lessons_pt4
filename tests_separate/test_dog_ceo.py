from utils.api_reqres import ReqresGet, CheckJsonValue
import json

class TestBreedsMessage():
    """Считаем количество элементов в массиве message"""
    def test_breeds_message(self):
        result_get_breeds = ReqresGet.get_data_3()
        CheckJsonValue.check_json_field_len(result_get_breeds, 'message')
    def test_breeds_hound_english(self):
        result_get_hound = ReqresGet.get_data_4()
        CheckJsonValue.check_json_element_content(result_get_hound, 'message', 'hound-english')