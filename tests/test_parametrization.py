import pytest
from _pytest.fixtures import SubRequest

@pytest.mark.parametrize('number', [1, 2, 3, -1])
def test_number(number: int):
    assert number > 0

# 2 параметра на тест
@pytest.mark.parametrize('number, expected',[(1, 1), (2, 4), (3, 9)])
def test_several_numbers(number: int, expected: int):
    assert number**2 == expected


#Тестовые данные перемножаются
@pytest.mark.parametrize('os', ['macos', 'windows', 'linux', 'debian'])
@pytest.mark.parametrize('browser', ['chromiun', 'webkit', 'firefox'])
def test_multiplication_of_numbers(os: str, browser: str):
    assert len(os + browser) > 0

@pytest.fixture(params=['chromiun', 'webkit', 'firefox'])
def browser(request: SubRequest):
    return request.param

def test_open_browser(browser: str):
    print(f'Running test on browser {browser}')

@pytest.mark.parametrize('user', ['Alice', 'Zara'])
class TestOperations:
    @pytest.mark.parametrize('account', ['Credit card', 'Debit card'])
    def test_with_operations(self, user: str, account: str):
        print(f'User with onperation {user}')

    def test_without_operations(self, user):
        print(f'User without onperation {user}')


users = {
    '+7-999-123-12-12': 'User with money on bank account',
    '+7-999-123-12-13': 'User without money on bank account',
    '+7-999-123-12-14':  'User with operations on bank account'
}

#Добавляем айди для параметров
@pytest.mark.parametrize(
    'phone_number',
    users.keys(),
    ids=lambda phone_number: f'{phone_number}: {users[phone_number]}'
)
def test_identifiers(phone_number: str):
    ...