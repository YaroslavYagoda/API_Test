#from chuck_joke import ChuckJoke

from academy_place import AcademyPlace


test1 = AcademyPlace()

# Запись place_id в файл
test1.place_id_to_file(4)

# Проверка сохраненных place_id
test1.test_get_place()
