from selenium.webdriver.common.by import By


class Locators:
    # Локаторы на странице регистрации
    NAME_REGISTER = (By.XPATH, "//label[contains(text(),'Имя')]/following-sibling::input")
    EMAIL_REGISTER = (By.XPATH, "//label[contains(text(),'Email')]/following-sibling::input")
    PASSWORD_REGISTER = (By.XPATH, "//label[contains(text(),'Пароль')]/following-sibling::input")
    INVALID_PASSWORD_POPUP = (By.XPATH, "//p[contains(text(),'Некорректный пароль')]")
    REGISTER_BUTTON = (By.XPATH, "//button[contains(text(),'Зарегистрироваться')]")
    SIGN_IN_REGISTER_BUTTON = (By.XPATH, "//a[contains(text(),'Войти')]")

    # Локаторы на странице с формой входа
    SIGN_BUTTON = (By.XPATH, "//button[contains(text(),'Войти')]")
    EMAIL_SIGN = (By.XPATH, "//label[contains(text(),'Email')]/following-sibling::input")
    PASSWORD_SIGN = (By.XPATH, "//label[contains(text(),'Пароль')]/following-sibling::input")


    # Локаторы на главной странице
    PLACE_AN_ORDER = (By.XPATH, "//button[contains(text(),'Оформить заказ')]")
    PERSONAL_ACCOUNT_BUTTON = (By.XPATH, "//p[contains(text(),'Личный Кабинет')]")
    SIGN_IN_ACCOUNT_BUTTON = (By.XPATH, "//button[contains(text(),'Войти в аккаунт')]")

    # Локаторы на странице личного кабинета
    PROFILE = (By.XPATH, "//a[contains(text(),'Профиль')]")
    EXIT_BUTTON = (By.XPATH, "//button[contains(text(),'Выход')]")

    #Локаторы для шапки страницы
    CONSTRUCTOR_BUTTON = (By.XPATH, "//p[contains(text(),'Конструктор')]")
    LOGO = (By.XPATH, "//div[@class='AppHeader_header__logo__2D0X2']")

    #Локаторы на странцие восстановления пароля
    SIGN_IN_FORGOT_PASSWORD_BUTTON = (By.XPATH, "//a[contains(text(),'Войти')]")
