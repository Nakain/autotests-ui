import pytest

from pages.dashboard_page import DashboardPage
from pages.login_page import LoginPage
from pages.registration_page import RegistrationPage


@pytest.fixture()
def login_page(chromium_page) -> LoginPage:
    return LoginPage(page=chromium_page)

@pytest.fixture()
def registration_page(chromium_page) -> RegistrationPage:
    return RegistrationPage(page=chromium_page)

@pytest.fixture()
def dashboard_page(chromium_page) -> DashboardPage:
    return DashboardPage(page=chromium_page)