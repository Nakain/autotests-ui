import pytest
import allure
from pages.dashboard.dashboard_page import DashboardPage
from pages.authentification.registration_page import RegistrationPage
from tools.allure.tags import AllureTag
from tools.allure.stories import AllureStory
from tools.allure.features import AllureFeature
from tools.allure.epics import AllureEpic
from allure_commons.types import Severity


@pytest.mark.regression
@pytest.mark.registration
@allure.epic(AllureEpic.LMS)
@allure.feature(AllureFeature.AUTHENTICATION)
@allure.story(AllureStory.REGISTRATION)
@allure.parent_suite(AllureEpic.LMS)
@allure.suite(AllureFeature.AUTHENTICATION)
@allure.sub_suite(AllureStory.REGISTRATION)
class TestRegistration:
    @allure.title("Registration with correct login, email and password")
    @allure.tag(AllureTag.REGRESSION, AllureTag.REGISTRATION)
    @allure.severity(Severity.CRITICAL)
    def test_successful_registration(self, registration_page: RegistrationPage, dashboard_page: DashboardPage):
        registration_page.visit("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")
        registration_page.registration_form.fill(email="user@gmail.com", username="username", password="password")
        registration_page.click_registration_button()
        dashboard_page.toolbar.check_visible()