import pytest
import allure
from data import *
from helpers import *
from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.profile_page import ProfilePage
from pages.orders_history_page import OrderHistoryPage


class TestPersonalPage:

    @classmethod
    def setup_class(cls):
        cls.user = register_new_user_and_return_email_password()
        cls.payload = {
            'email': cls.user[0],
            'password': cls.user[1],
            'name': cls.user[2]
        }
        login_response = requests.post(API_LOGIN_URL, data=cls.payload)
        cls.user_token = login_response.json()['accessToken']

    @allure.title('Проверка перехода в личный кабинет по клику на кнопку "Личный кабинет"')
    @allure.description('Выполняется авторизация по клику на кнопку "Личный кабинет" и проверка активации страницы.')
    def test_enter_in_personal_page(self, driver):
        login_page = LoginPage(driver)
        main_page = MainPage(driver)
        profile_page = ProfilePage(driver)
        main_page.open_url(MAIN_URL)
        main_page.click_to_button_personal_page()
        login_page.set_email(self.payload['email'])
        login_page.set_password(self.payload['password'])
        login_page.click_to_button_enter()
        main_page.click_to_button_personal_page()
        assert EXPECTED_PROFILE_CLASS_TEXT in profile_page.get_element_attribute_class()

    @allure.title('Проверка перехода в раздел "История заказов"')
    @allure.description('Выполняется авторизация, переход в раздел "История заказов" и проверяется активация страницы.')
    def test_enter_in_order_history_page(self, driver):
        main_page = MainPage(driver)
        profile_page = ProfilePage(driver)
        order_history_page = OrderHistoryPage(driver)
        login_page = LoginPage(driver)
        login_page.open_url(LOGIN_URL)
        login_page.set_email(self.payload['email'])
        login_page.set_password(self.payload['password'])
        login_page.click_to_button_enter()
        main_page.click_to_button_personal_page()
        profile_page.click_to_button_order_history()
        assert EXPECTED_HISTORY_CLASS_TEXT in order_history_page.get_element_attribute_class()

    @allure.title('Проверка выхода из личного кабинета')
    @allure.description(
        'Выполняется авторизация, нажатие на кнопку "Выход" и проверка заголовка страницы после выхода.')
    def test_exit_from_personal_page(self, driver):
        login_page = LoginPage(driver)
        login_page.open_url(LOGIN_URL)
        login_page.set_email(self.payload['email'])
        login_page.set_password(self.payload['password'])
        login_page.click_to_button_enter()
        main_page = MainPage(driver)
        main_page.click_to_button_personal_page()
        profile_page = ProfilePage(driver)
        profile_page.click_to_button_exit()
        assert login_page.get_title_page() == EXPECTED_LOGIN_TITLE

    @classmethod
    def teardown_class(cls):
        requests.delete(API_USER_URL, headers={'Authorization': cls.user_token})
