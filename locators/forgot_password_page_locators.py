from selenium.webdriver.common.by import By


class ForgotPasswordPageLocators:
    PASSWORD_RECOVERY_TITLE = By.XPATH, './/div[@class="Auth_login__3hAey"]/h2'  # Заголовок страницы восстановления пароля
    RECOVERY_BUTTON = By.XPATH, './/button[text()="Восстановить"]'  # Кнопка "Восстановить"
    EMAIL_INPUT = By.XPATH, './/label[text()="Email"]/following-sibling::input'  # Форма ввода email пользователя