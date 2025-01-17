import requests


class ChuckJoke:
    base_url = 'https://api.chucknorris.io/jokes/random'
    list_of_categories = None

    def get_categories(self):
        """
        Получаем категории для шуток
        """
        try:
            categories = requests.get('https://api.chucknorris.io/jokes/categories')
            assert categories.status_code == 200, \
                'Ошибка получения перечня категорий шуток.\nСписок категорий пуст.'
        except Exception as err:
            print(err.args[0])
            self.list_of_categories = None
        else:
            categories.encoding = "utf-8"
            self.list_of_categories = categories.json()

    def get_random_joke(self):
        """
        Получение случайной шутки
        """
        print(f'Получение случайной шутки\n')
        joke = requests.get(self.base_url)
        assert joke.status_code == 200, \
            'Ошибка получения случайной шутки'
        joke.encoding = 'utf-8'
        joke_text = joke.json().get("value")
        assert 'Chuck' in joke_text, 'Полученная шутка не про Чака'
        print(f'Шутка:\n\t{joke_text}\n')

    def get_joke_from_selected_category(self, current_category):
        """
        Получение случайной шутки из заданной категории
        :param current_category: категория случайной шутки
        """
        print(f'Получение случайной шутки из категории "{current_category}"\n')
        joke_url = f'{self.base_url}?category={current_category}'
        try:
            joke = requests.get(joke_url)
            assert joke.status_code == 200, \
                'Ошибка статус-кода для случайной шутки из заданной категории'
            assert joke.json().get("categories")[0] == current_category, \
                f'Категория шутки: "{joke.json().get("categories")[0]}", ожидалось: "{current_category}"'
            joke.encoding = 'utf-8'
            joke_text = joke.json().get("value")
            assert 'Chuck' in joke_text, \
                'Полученная шутка не про Чака'
        except Exception as err:
            print(err.args[0])
        else:
            print(f'Шутка:\n\t{joke_text}\n')

    def get_one_joke_from_each_category(self):
        """
        Получение по одной случайно шутке из каждой категории
        """
        self.get_categories()
        if self.list_of_categories:
            for current_category in self.list_of_categories:
                self.get_joke_from_selected_category(current_category)

    def get_one_joke_from_user_category(self):
        """
        Получение случайной шутки из категории введенной пользователем
        """
        self.get_categories()
        if self.list_of_categories:
            print('Доступны следующие категории шуток:\n')
            for category in self.list_of_categories:
                print(category, end=' ')
            current_category = input('\n\nВведите наименование интересующей категории:\n')
            if current_category in self.list_of_categories:
                self.get_joke_from_selected_category(current_category)
            else:
                print('Указанной категории не существует.')
