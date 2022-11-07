# def decorator_name(func):
#     def wrapper():
#         print('До выполнения функции')
#         func()
#         print('После выполнения функции')
#
#     return wrapper
#
# @decorator_name
# def my_func():
#     print('OK')
#
#
# my_func()
# print('*' * 20)



# def decorator_name(func):
#     def wrapper():
#         result = func()
#         print(f"Результат - {result}")
#         return 'Fail'
#
#     return wrapper
#
# @decorator_name
# def my_func():
#     print('OK')
#
#
# my_func()
# print('*' * 20)


def decorator_name(func):
    def wrapper(*args, **kwargs):

        print(f'До выполения функции')
        result = func(*args, **kwargs)
        print(f'После выполнения функции')
        return f"Decorator - {result}"

    return wrapper

@decorator_name
def my_func(user_name):
    return user_name

print(my_func("John"))