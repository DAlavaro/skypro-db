import time

import pytest

# autouse=True для того чтобы фикстуры использовались автоматически без указания в аргументах
@pytest.fixture(autouse=True, scope='module')
def time_after_module_tests():
    # yield - выполнение теста
    yield
    print("module finished. not time...")


@pytest.fixture(autouse=True, scope='class')
def time_after_class_test():
    yield
    now = time.time()
    print('---')
    print(' finshed : {}'.format(time.strftime('%d %b %X', time.localtime(now))))
    print('---')


@pytest.fixture(autouse=True, scope='session')
def time_after_class_test():
    yield
    now = time.time()
    print('---')
    print(' finshed : {}'.format(time.strftime('%d %b %X', time.localtime(now))))
    print('---')


@pytest.fixture(autouse=True, scope='function')
def time_after_class_test():
    yield
    now = time.time()
    print('---')
    print(' finshed : {}'.format(time.strftime('%d %b %X', time.localtime(now))))
    print('---')


@pytest.fixture()
def number_42():
    return 42