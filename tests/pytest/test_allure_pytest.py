import allure


@allure.step("Открываем браузер")
def open_browser():
    with allure.step("get browser"):
        ...

    with allure.step("start browser"):
        ...


@allure.step("Создаем курс")
def create_course(title: str):
    with allure.step(f"Cоздаем курс с названием {title}"):
        ...


@allure.step("Cоздаем курс с названием {title}")
def create_course(title: str):
    ...


@allure.step("Закрываем браузер")
def close_browser():
    ...


def test_feature():
    open_browser()
    create_course(title="Locust")
    create_course(title="Pytest")
    create_course(title="Python")
    create_course(title="Playwright")
    close_browser()
