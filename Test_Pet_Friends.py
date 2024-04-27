from api import PetFriends
from settings import valid_email, valid_password
import os

pf = PetFriends()


def test_get_api_key_for_invalid_user_email(email='rsdcfvbhjjx', password=valid_password):
    """ Код 403 при неверном логине в запросе api ключа"""

    status, result = pf.get_api_key(email, password)

    assert status == 403



def test_get_api_key_for_invalid_user_password(email=valid_email, password='dhnecd645415dx'):
    """ Код 403 при неверном пароле в запросе api ключа"""

    status, result = pf.get_api_key(email, password)

    assert status == 403



def test_add_new_pet_without_photo_with_valid_data(name='Гарфилд', animal_type='кот', age='2'):
    """Добавить питомца без фото"""

    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.create_new_pet_simple(auth_key, name, animal_type, age)

    assert status == 200


def test_add_pet_new_photo(pet_photo='images/dobin.jpg'):
    """Добавить фото питомца"""

    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")
    status, result = pf.add_pet_photo(auth_key, my_pets['pets'][0]['id'], pet_photo)

    assert status == 200


def test_add_pet_new_photo(pet_photo='images/cool-fun.gif'):
    """Добавить фото несоответствующего формата """

    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")
    status, result = pf.add_pet_photo(auth_key, my_pets['pets'][0]['id'], pet_photo)

    assert status != 200



def test_add_new_pet_with_invalid_name(name='', animal_type='экзот', age='2', pet_photo='images/dobin.jpg'):
    """Нельзя добавить питомца, без указания имени"""

    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)
    auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.add_new_pet(auth_key, name, animal_type, age, pet_photo)

    assert status == 200
    print('Пожалуйста, укажите имя питомца')


def test_add_new_pet_with_invalid_animal_type(name='Добин', animal_type='', age='2', pet_photo='images/dobin.jpg'):
    """Нельзя добавить питомца, без указания породы"""

    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)
    auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.add_new_pet(auth_key, name, animal_type, age, pet_photo)

    assert status == 200
    print('Пожалуйста, укажите породу питомца')


def test_add_new_pet_with_invalid_age(name='Добин', animal_type='экзот', age='', pet_photo='images/dobin.jpg'):
        """Нельзя добавить питомца, без указания возраста"""

        pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)
        auth_key = pf.get_api_key(valid_email, valid_password)
        status, result = pf.add_new_pet(auth_key, name, animal_type, age, pet_photo)

        assert status == 200
        print('Пожалуйста, укажите возраст питомца')



def test_add_new_pet_with_negative_age(name='Наполеон', animal_type='Сибирская',
                                       age='-1', pet_photo='images/Napoleon.jpg'):
    """Нельзя добавить питомца с отрицательным возрастом"""

    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.add_new_pet(auth_key, name, animal_type, age, pet_photo)

    assert status == 200
    print('Баг - сайт позволяет добавить в стороку "возраст" отрицательное число')



def test_add_new_pet_with_too_old_age(name='Юлий', animal_type='конь',
                                       age='78000', pet_photo='images/horse_iuliy.jpg'):
    """Нельзя добавить питомца, указывая возраст более 50-и лет"""

    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.add_new_pet(auth_key, name, animal_type, age, pet_photo)

    assert status == 200
    print('Баг - сайт позволяет довавить в строку "возраст" число более 50-и')
