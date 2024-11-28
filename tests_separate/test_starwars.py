from utils.api_starwars import StarWarsInfo
import pytest

class TestGetMovies():
    wader_films_list = []  # Атрибут экземпляра класса для хранения списка фильмов
    character_list = set() # Используем множество, чтобы избежать дублирования
                           # + Атрибут экземпляра класса для хранения списка персонажей
    character_names = []   #Имена персонажей
    def test_get_films(self):
        print('Метод GET: ')
        get_films = StarWarsInfo.get_data()
        get_films_wader_json = get_films.json()
        wader_films = get_films_wader_json.get('films')
        TestGetMovies.wader_films_list = list(wader_films)  # Сохраняем список фильмов в атрибут класса
        print(f'Фильмы с Дартом Вейдером: {TestGetMovies.wader_films_list}')
        assert TestGetMovies.wader_films_list  # Проверяем, что список не пуст


    def test_get_character_links(self):
        """Получение персонажей фильмов"""
        if not TestGetMovies.wader_films_list:
            pytest.fail('Список фильмов пуст. Сначала вызовите test_get_films.')

        for link in TestGetMovies.wader_films_list: # Получаем данные о фильме
            get_chars = StarWarsInfo.get_characters(link)
            get_chars_json = get_chars.json()
            selected_characters = get_chars_json.get('characters', []) # Извлекаем список персонажей и добавляем их в множество
                                                                       # [] используются для значения по умолчанию, будет возвращено,
                                                                       # если ключ 'characters' отсутствует в словаре get_chars_json.
            TestGetMovies.character_list.update(selected_characters)

        print(f'Список ссылок на персонажей в фильмах с Дартом Вейдером: {sorted(TestGetMovies.character_list)}')
        assert TestGetMovies.character_list  # Проверяем, что список ссылок на персонажей не пуст

    def test_get_character_names(self):
        """Получение списка имен персонажей"""
        if not TestGetMovies.character_list:
            pytest.fail('Список ссылок на персонажей пуст. Сначала вызовите test_get_character_links')

        for link in TestGetMovies.character_list: # Получаем список имен по каждой ссылке на персонажа
            get_names = StarWarsInfo.get_character_names(link)
            get_names_json = get_names.json()
            character_names = get_names_json.get('name', [])
            TestGetMovies.character_names.append(character_names)


        print(f'Список персонажей в фильмах с Дартом Вейдером: {sorted(TestGetMovies.character_names)}')
        assert TestGetMovies.character_names # Проверяем, что список имен персонажей не пуст

        with open('starwars.txt', 'w', encoding='utf-8') as file:
            file.write('\n'.join(TestGetMovies.character_names))
