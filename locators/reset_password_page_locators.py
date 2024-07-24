from selenium.webdriver.common.by import By


class ResetPasswordPageLocators:
    PASSWORD_RESET_TITLE = By.XPATH, './/div[@class="Auth_login__3hAey"]/h2'  # Заголовок страницы сброса пароля
    PASSWORD_INPUT = By.XPATH, './/input[@name="Введите новый пароль"]'  # Форма ввода пароля пользователя
    SHOW_HIDE_BUTTON = By.XPATH, './/div[@class="input__icon input__icon-action"]'  # Кнопка "Показать/скрыть пароль"
    PASSWORD_INPUT_FIELD = By.XPATH, './/label[text()="Пароль"]/parent::div'  # Поле ввода пароля пользователя
