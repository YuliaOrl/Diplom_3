import pytest
import allure
from data import *
from helpers import *
from pages.main_page import MainPage
from pages.orders_feed_page import OrdersFeedPage


class TestMainFunctional:

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

    @allure.title('Проверка перехода по клику на кнопку "Конструктор"')
    @allure.description('Выполняется клик на "Конструктор" со страницы авторизации и проверяется заголовок страницы.')
    def test_enter_in_constructor_from_login_page(self, driver):
        main_page = MainPage(driver)
        main_page.open_url(MAIN_URL)
        main_page.click_to_button_personal_page()
        main_page.click_to_button_constructor()
        assert main_page.get_title_page() == EXPECTED_MAIN_TITLE

    @allure.title('Проверка перехода по клику на кнопку "Лента заказов"')
    @allure.description('Выполняется клик на кнопку "Лента заказов" и проверяется заголовок страницы.')
    def test_enter_in_order_feed_from_main_page(self, driver):
        main_page = MainPage(driver)
        orders_feed_page = OrdersFeedPage(driver)
        main_page.open_url(MAIN_URL)
        main_page.click_to_button_order_feed()
        assert orders_feed_page.get_title_page() == EXPECTED_ORDER_FEED_TITLE

    @allure.title('Проверка открытия всплывающего окна с деталями по клику на ингредиент')
    @allure.description('Выполняется клик на ингредиент и проверяется открытие окна с деталями.')
    @pytest.mark.parametrize('ingredient', INGREDIENTS)
    def test_open_ingredient_details_window(self, driver, ingredient):
        main_page = MainPage(driver)
        main_page.open_url(MAIN_URL)
        main_page.click_to_ingredient_with_presence(ingredient)
        assert EXPECTED_OPEN_WINDOW_CLASS_TEXT in main_page.get_class_details_window(ingredient)

    @allure.title('Проверка закрытия всплывающего окна с деталями ингредиента')
    @allure.description('Выполняется клик на кнопку-крестик и проверяется закрытие окна с деталями.')
    @pytest.mark.parametrize('ingredient', INGREDIENTS)
    def test_close_ingredient_details_window(self, driver, ingredient):
        main_page = MainPage(driver)
        main_page.open_url(MAIN_URL)
        main_page.click_to_ingredient_with_presence(ingredient)
        main_page.click_to_button_window_close()
        assert EXPECTED_OPEN_WINDOW_CLASS_TEXT not in main_page.get_class_details_window_with_presence(ingredient)

    @allure.title('Проверка каунтера ингредиента при добавлении его в заказ')
    @allure.description('Выполняется добавление ингредиента и проверяется увеличение его каунтера.')
    def test_counter_ingredient(self, driver):
        main_page = MainPage(driver)
        main_page.open_url(MAIN_URL)
        bun_counter = int(main_page.get_counter_value(INGREDIENTS[0]))
        sauce_counter = int(main_page.get_counter_value(INGREDIENTS[1]))
        filling_counter = int(main_page.get_counter_value(INGREDIENTS[2]))
        main_page.add_ingredient(INGREDIENTS[0])
        main_page.add_ingredient(INGREDIENTS[1])
        main_page.add_ingredient(INGREDIENTS[2])
        assert int(main_page.get_counter_value(INGREDIENTS[0])) == 2 * (bun_counter + 1) \
               and int(main_page.get_counter_value(INGREDIENTS[1])) == sauce_counter + 1 \
               and int(main_page.get_counter_value(INGREDIENTS[2])) == filling_counter + 1

    @allure.title('Проверка оформления заказа залогиненным пользователем')
    @allure.description('Выполняется авторизация, оформление заказа и проверяется открытие окна подтверждения заказа.')
    def test_create_order(self, driver):
        main_page = MainPage(driver)
        main_page.open_url(MAIN_URL)
        driver.execute_script("window.localStorage.setItem('accessToken', arguments[0]);", self.user_token)
        main_page.click_to_button_enter_account()
        main_page.click_to_button_constructor()
        main_page.add_ingredient(INGREDIENTS[0])
        main_page.add_ingredient(INGREDIENTS[1])
        main_page.add_ingredient(INGREDIENTS[2])
        main_page.click_to_button_create_order()
        assert EXPECTED_OPEN_WINDOW_CLASS_TEXT in main_page.get_class_order_confirm_window()


    @classmethod
    def teardown_class(cls):
        requests.delete(API_USER_URL, headers={'Authorization': cls.user_token})

