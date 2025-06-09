import pytest
import allure
from pages.dashboard.dashboard_page import DashboardPage
from pages.authentification.registration_page import RegistrationPage
from tools.allure.tags import AllureTag
from tools.allure.stories import AllureStory
from tools.allure.features import AllureFeature
from tools.allure.epics import AllureEpic
from allure_commons.types import Severity
from tools.routes import AppRoute
from config import settings


@pytest.mark.regression
@pytest.mark.registration
@allure.epic(AllureEpic.LMS)
@allure.feature(AllureFeature.AUTHENTICATION)
@allure.story(AllureStory.REGISTRATION)
@allure.parent_suite(AllureEpic.LMS)
@allure.suite(AllureFeature.AUTHENTICATION)
@allure.sub_suite(AllureStory.REGISTRATION)
class TestRegistration:
    @pytest.mark.xdist_group(name="authorization-group")
    @allure.title("Registration with correct login, email and password")
    @allure.tag(AllureTag.REGRESSION, AllureTag.REGISTRATION)
    @allure.severity(Severity.CRITICAL)
    def test_successful_registration(self, registration_page: RegistrationPage, dashboard_page: DashboardPage):
        registration_page.visit(AppRoute.REGISTRATION)
        registration_page.registration_form.fill(email=settings.test_user.email, username=settings.test_user.username, password=settings.test_user.password)
        registration_page.click_registration_button()
        dashboard_page.toolbar.check_visible()