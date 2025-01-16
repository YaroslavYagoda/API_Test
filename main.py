import requests
from random import randint


class ChuckJoke:

    base_url = 'https://api.chucknorris.io/jokes/random'
    list_of_categories = None

    def __init__(self):
        """
        При инициализации экземпляра класса получаем категории для шуток
        """
        try:
            categories = requests.get('https://api.chucknorris.io/jokes/categories')
            assert categories.status_code == 200, \
                'Ошибка получения перечня категорий шуток'
        except Exception as err:
            print(err.args[0])
        else:
            categories.encoding = "utf-8"
            self.list_of_categories = categories.json()

    def get_joke(self):
        """
        Получение шутки из случайной категории, при ошибке загрузки категорий будет получена случайная шутка
        """
        if self.list_of_categories:
            num_category = randint(0, len(self.list_of_categories) - 1)
            current_category = self.list_of_categories[num_category]
            print(f'Получение случайной шутки из категории "{current_category}"\n')
            joke_url = f'{self.base_url}?category={current_category}'
            joke = requests.get(joke_url)
            assert joke.status_code == 200, \
                'Ошибка получения случайной шутки из заданной категории'
            assert joke.json().get("categories")[0] == current_category, \
                f'Получена категория шутки: "{joke.json().get("categories")[0]}", ожидалось: "{current_category}"'
        else:
            print(f'Получение случайной шутки из случайной категории\n')
            joke = requests.get(self.base_url)
            assert joke.status_code == 200, \
                'Ошибка получения случайной шутки'

        joke_text = joke.json().get("value")
        assert 'Chuck' in joke_text, 'Полученная шутка не про Чака'
        print(f'Шутка:\n\t{joke_text}')


chuck_joke = ChuckJoke()
chuck_joke.get_joke()
