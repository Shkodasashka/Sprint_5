from selenium.webdriver.common.by import By


class Locators:
    # Локаторы для регистрации
    REGISTER_BUTTON = (By.XPATH, "//button[contains(text(),'Зарегистрироваться')]")
    NAME = (By.XPATH, "//label[contains(text(),'Имя')]/following-sibling::input")
    EMAIL = (By.XPATH, "//label[contains(text(),'Email')]/following-sibling::input")
    PASSWORD = (By.XPATH, "//label[contains(text(),'Пароль')]/following-sibling::input")
    INVALID_PASSWORD_POPUP = (By.XPATH, "//p[contains(text(),'Некорректный пароль')]")

    # Локаторы для входа
    SIGN_BUTTON = (By.XPATH, "//button[contains(text(),'Войти')]")