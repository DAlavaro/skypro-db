import calendar
import datetime

import jwt # pip install pyjwt


# Секретный ключ не должен меняться иначе все предыдущие созданные JWT будут невозможны
secret = 's3cR$eT'
# лгорит для создания токена
algo = 'HS256'


def generate_token(data):
    """ Функция принимает информацию и возвращает jwt.encode """
    # берем текущую дату и добавляем 30 минут, задает время жизни токена
    min30  = datetime.datetime.utcnow() + datetime.timedelta(minutes=30)
    # кодируемая информация по ключу 'exp'
    data["exp"] = calendar.timegm(min30.timetuple())

    # образаемся к библиотеке jwt там есть метод encode который кодирует информацию в jwt токен
    # мы передаем туда данные секретный ключ и указываем алгоритv в ответе получим значение
    # fgdasgfsag.asdgsag.asdfgasdfg
    return jwt.encode(data, secret, algorithm=algo) #   кодирует информацию в jvt token


def check_token(token):
    """ Функция проверки токена """
    try:
        jwt.decode(token, secret, algorithms=[algo]) # декодирует информацию
        return True
    except Exception:
        return False


if __name__ == '__main__':
    data = {
        'username': 'myname',
        'role': 'user'
    }
    token = generate_token(data)
    is_ok = check_token(token)

    print(token)
    print(is_ok)


""" 
    JWT - это срока
    header.payload.signature
    
    Как работает JWT
    1. Авторизовать пользователя
        Клиент присылает логин и пароль и отправляем токен который 
        сгенерировали на сервере проверяем логин и пароль и только после этого отдаем токен.
    2. токен имеет время жизни
    3. Позволяет понять от кого пришел запрос
"""







