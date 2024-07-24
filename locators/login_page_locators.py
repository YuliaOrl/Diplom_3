from selenium.webdriver.common.by import By


class LoginPageLocators:
    PASSWORD_RECOVERY_LINK = By.LINK_TEXT, 'Восстановить пароль'  # Ссылка для восстановления пароля
    LOGIN_PAGE_TITLE = By.XPATH, './/div[@class="Auth_login__3hAey"]/h2'  # Заголовок страницы авторизации
    EMAIL_INPUT = By.XPATH, './/label[text()="Email"]/following-sibling::input'  # Форма ввода email пользователя
    PASSWORD_INPUT = By.XPATH, './/label[text()="Пароль"]/following-sibling::input'  # Форма ввода пароля пользователя
    ENTER_BUTTON = By.XPATH, './/button[text()="Войти"]'  # Кнопка «Войти»
