from selenium.webdriver.common.by import By


class Locators:
    # Локаторы для регистрации
    REGISTER_BUTTON = (By.XPATH, "//button[contains(text(),'Зарегистрироваться')]")
    NAME_REGISTER = (By.XPATH, "//label[contains(text(),'Имя')]/following-sibling::input")
    EMAIL_REGISTER = (By.XPATH, "//label[contains(text(),'Email')]/following-sibling::input")
    PASSWORD_REGISTER = (By.XPATH, "//label[contains(text(),'Пароль')]/following-sibling::input")
    INVALID_PASSWORD_POPUP = (By.XPATH, "//p[contains(text(),'Некорректный пароль')]")

    # Локаторы для входа
    SIGN_BUTTON = (By.XPATH, "//button[contains(text(),'Войти')]")
    SIGN_IN_ACCOUNT_BUTTON = (By.XPATH, "//button[contains(text(),'Войти в аккаунт')]")
    EMAIL_SIGN = (By.XPATH, "//label[contains(text(),'Email')]/following-sibling::input")
    PASSWORD_SIGN = (By.XPATH, "//label[contains(text(),'Пароль')]/following-sibling::input")
    PLACE_AN_ORDER = (By.XPATH, "//button[contains(text(),'Оформить заказ')]")
    SIGN_IN_PERSONAL_ACCOUNT_BUTTON = (By.XPATH, "//p[contains(text(),'Личный Кабинет')]")
    SIGN_IN_REGISTER_BUTTON = (By.XPATH, "//a[contains(text(),'Войти')]")