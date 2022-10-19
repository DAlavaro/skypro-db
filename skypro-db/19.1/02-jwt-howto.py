import calendar
import datetime

import jwt

secret = 's3cR$eT'
algo = 'HS256'


def generate_token(data):
    """ Функция принимает информацию и возвращает jwt.encode """
    min30  = datetime.datetime.utcnow() + datetime.timedelta(minutes=30)
    data["exp"] = calendar.timegm(min30.timetuple())

    return jwt.encode(data, secret, algorithm=algo) # кодирует информацию в jvt token


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







