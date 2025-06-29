import pytest

from pages.courses.courses_list_page import CoursesListPage
from pages.courses.create_course_page import CreateCoursePage
import allure
from tools.allure.tags import AllureTag
from tools.allure.stories import AllureStory
from tools.allure.features import AllureFeature
from tools.allure.epics import AllureEpic
from tools.routes import AppRoute
from allure_commons.types import Severity
from config import settings

@pytest.mark.courses
@pytest.mark.regression
@allure.tag(AllureTag.REGRESSION, AllureTag.COURSES)
@allure.epic(AllureEpic.LMS)
@allure.feature(AllureFeature.COURSES)
@allure.story(AllureStory.COURSES)
@allure.parent_suite(AllureEpic.LMS)
@allure.suite(AllureFeature.COURSES)
@allure.sub_suite(AllureStory.COURSES)
class TestCourses:
    @allure.title("Check displaying of empty courses list")
    @allure.severity(Severity.NORMAL)
    def test_empty_courses_list(self, page_with_state, courses_list_page: CoursesListPage):
        courses_list_page.visit(AppRoute.COURSE_LIST)

        courses_list_page.sidebar.check_visible()
        courses_list_page.navbar.check_visible(settings.test_user.username)
        courses_list_page.toolbar_view.check_visible()
        courses_list_page.check_visible_empty_view()

    @allure.title("Create course")
    @allure.severity(Severity.CRITICAL)
    def test_create_course(self, courses_list_page: CoursesListPage, create_course_page: CreateCoursePage):
        create_course_page.visit(AppRoute.CREATE_COURSE)
        create_course_page.toolbar.check_visible(is_create_course_disabled=True)
        create_course_page.image_upload_widget.check_visible(is_image_uploaded=False)
        create_course_page.create_course_form.check_visible(title="", description="", estimated_time="", max_score="0",
                                                            min_score="0")
        create_course_page.exercises_toolbar.check_visible()
        create_course_page.check_visible_exercises_empty_view()
        create_course_page.image_upload_widget.upload_preview_image(settings.test_data.image_png_file)
        create_course_page.image_upload_widget.check_visible(is_image_uploaded=True)
        create_course_page.create_course_form.fill(
            title="Playwright",
            estimated_time="2 weeks",
            description="Playwright",
            max_score="100",
            min_score="10"
        )
        create_course_page.toolbar.click_create_course_button()
        courses_list_page.toolbar_view.check_visible()
        courses_list_page.course_view.check_visible(
            index=0,
            title="Playwright",
            max_score="100",
            min_score="10",
            estimated_time="2 weeks"
        )

    @allure.title("Edit course")
    @allure.severity(Severity.CRITICAL)
    def test_edit_course(self, courses_list_page: CoursesListPage, create_course_page: CreateCoursePage):
        create_course_page.visit(AppRoute.CREATE_COURSE)
        create_course_page.create_course_form.check_visible(title="", description="", estimated_time="", max_score="0",
                                                            min_score="0")
        create_course_page.create_course_form.fill(
            title="Playwright",
            estimated_time="2 weeks",
            description="Playwright",
            max_score="100",
            min_score="10"
        )
        create_course_page.image_upload_widget.upload_preview_image(settings.test_data.image_png_file)
        create_course_page.toolbar.click_create_course_button()
        courses_list_page.course_view.check_visible(
            index=0,
            title="Playwright",
            max_score="100",
            min_score="10",
            estimated_time="2 weeks"
        )
        courses_list_page.course_view.menu.click_edit(index=0)
        create_course_page.create_course_form.check_visible(
            title="Playwright",
            max_score="100",
            description="Playwright",
            min_score="10",
            estimated_time="2 weeks"
        )
        create_course_page.create_course_form.fill(
            title="Python",
            estimated_time="2 years",
            description="Python",
            max_score="10",
            min_score="1"
        )
        create_course_page.toolbar.click_create_course_button()
        courses_list_page.course_view.check_visible(
            index=0,
            title="Python",
            estimated_time="2 years",
            max_score="10",
            min_score="1"
        )




