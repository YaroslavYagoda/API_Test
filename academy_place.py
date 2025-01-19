import requests


class AcademyPlace:
    base_url = 'https://rahulshettyacademy.com'
    post_resource = '/maps/api/place/add/json'
    key = '?key=qaclick123'
    get_resource = '/maps/api/place/get/json'
    get_param = '&place_id='
    body = \
        {
            "location":
                {
                    "lat": -38.383494,
                    "lng": 33.427362
                },
            "accuracy": 50,
            "name": "Frontline house",
            "phone_number": "(+91) 983 893 3937",
            "address": "29, side layout, cohen 09",
            "types": ["shoe park", "shop"],
            "website": "http://google.com",
            "language": "French-IN"
        }

    def test_create_place(self):
        """
        Создает новую локацию
        :return: 'place_id' локации из тела ответа
        """
        post_url = self.base_url + self.post_resource + self.key
        post_result = requests.post(post_url, json=self.body)

        assert post_result.status_code == 200, \
            f'Статус-код не верен, получено {post_result.status_code}'
        post_result.encoding = 'utf-8'
        assert post_result.json().get('place_id'), \
            f'В теле ответа отсутствует "place_id", статус ответа: {post_result.json().get('status')} '
        return post_result.json().get('place_id')

    def place_id_to_file(self, repeat_count):
        """
        Запись в файл 'place_id' локации(й)
        :param repeat_count: количество локаций для записи
        """
        place_ides = []
        try:
            for _ in range(repeat_count):
                place_ides.append(self.test_create_place() + '\n')
        except Exception as err:
            print(err.args[0])
            print('Запись не добавлена')
        with open('place_ides.txt', "w", encoding='utf-8') as file:
            file.writelines(place_ides)

    def test_get_place(self):
        """
        Проверка сохраненных в файл 'place_id'
        :return:
        """
        with open('place_ides.txt', "r", encoding='utf-8') as file:
            place_ides = file.readlines()
        for place_id in place_ides:
            get_url = self.base_url + self.get_resource + self.key + self.get_param + place_id[:-1]
            try:
                get_result = requests.get(get_url)
                assert get_result.status_code == 200, \
                    f'Статус-код запроса не верен, получено {get_result.status_code}'
                assert get_result.json().get('name') == self.body.get('name'), \
                    f'Сведения (поле "name") о полученной локации не совпадают со сведениями созданной'
            except Exception as err:
                print(err.args[0])
            else:
                print(f'place_id: "{place_id[:-1]}" - проверка успешна')
