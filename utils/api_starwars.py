from utils.http_methods import Http_methods

"""Методы для тестирования https://swapi.dev/"""

base_url = 'https://swapi.dev/api'
people_url = f'{base_url}/people/'
films_url = f'{base_url}/films/'

class StarWarsInfo():
    @staticmethod
    def get_data():
        """Получение данных по Дарту Вейдеру"""
        url_darth_wader = people_url + '4'
        print(f'Метод GET DATA. Запрос данных по Дарту Вейдеру: {url_darth_wader}')
        get_wader_data = Http_methods.get(url_darth_wader)
        return get_wader_data

    @staticmethod
    def get_characters(films_url):
        """Получение списка ссылок на персонажей"""
        print(f'Метод GET CHARACTERS. Запрос данных по фильму: {films_url}')
        get_character_data = Http_methods.get(films_url)
        return get_character_data

    @staticmethod
    def get_character_names(people_url):
        """Получение списка имен персонажей"""
        print(f'Метод GET CHARACTER NAMES. Запрос имен персонажейЖ {people_url}')
        get_character_names = Http_methods.get(people_url)
        return get_character_names
