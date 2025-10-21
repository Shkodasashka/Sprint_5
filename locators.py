from selenium.webdriver.common.by import By


class Locators:
    # Локаторы на странице регистрации
    NAME_REGISTER = (By.XPATH, "//label[contains(text(),'Имя')]/following-sibling::input")  #поле ввода имени 
    EMAIL_REGISTER = (By.XPATH, "//label[contains(text(),'Email')]/following-sibling::input") #поле ввода почты
    PASSWORD_REGISTER = (By.XPATH, "//label[contains(text(),'Пароль')]/following-sibling::input") #поле ввода пароля
    INVALID_PASSWORD_POPUP = (By.XPATH, "//p[contains(text(),'Некорректный пароль')]")  #сообщение о введенном пользователем некорректном пароле
    REGISTER_BUTTON = (By.XPATH, "//button[contains(text(),'Зарегистрироваться')]")  #кнопка "Зарегестрироваться"
    SIGN_IN_REGISTER_BUTTON = (By.XPATH, "//a[contains(text(),'Войти')]")   #кнопка "Войти" на странице регистрации

    # Локаторы на странице с формой входа
    SIGN_BUTTON = (By.XPATH, "//button[contains(text(),'Войти')]") #кнопка "Войти"
    EMAIL_SIGN = (By.XPATH, "//label[contains(text(),'Email')]/following-sibling::input")  #поле ввода почты
    PASSWORD_SIGN = (By.XPATH, "//label[contains(text(),'Пароль')]/following-sibling::input")  #поле ввода пароля

    # Локаторы на главной странице
    PLACE_AN_ORDER = (By.XPATH, "//button[contains(text(),'Оформить заказ')]")  #кнопка "Оформить заказ" для авторизованного пользователя
    PERSONAL_ACCOUNT_BUTTON = (By.XPATH, "//p[contains(text(),'Личный Кабинет')]")  #кнопка "Личный кабинет"
    SIGN_IN_ACCOUNT_BUTTON = (By.XPATH, "//button[contains(text(),'Войти в аккаунт')]")  #кнопка "Войти в аккаунт" для неавторизованного пользователя
    BREAD_SWITCHER = (By.XPATH, "//span[contains(text(),'Булки')]") #тогл "Булки" в конструкторе
    SELECTED_BREAD_SWITCHER = (By.XPATH, "//span[contains(text(),'Булки')]/parent::div[@class='tab_tab__1SPyG tab_tab_type_current__2BEPc pt-4 pr-10 pb-4 pl-10 noselect']")  #выбранный тогл "Булки" в конструкторе
    SAUCE_SWITCHER = (By.XPATH, "//span[contains(text(),'Соусы')]")  #тогл "Соусы" в конструкторе
    SELECTED_SAUCE_SWITCHER = (By.XPATH, "//span[contains(text(),'Соусы')]/parent::div[@class='tab_tab__1SPyG tab_tab_type_current__2BEPc pt-4 pr-10 pb-4 pl-10 noselect']")  #выбранный тогл "Соусы" в конструкторе
    STAFFING_SWITCHER = (By.XPATH, "//span[contains(text(),'Начинки')]") #тогл "Начинки" в конструкторе
    SELECTED_STAFFING_SWITCHER = (By.XPATH, "//span[contains(text(),'Начинки')]/parent::div[@class='tab_tab__1SPyG tab_tab_type_current__2BEPc pt-4 pr-10 pb-4 pl-10 noselect']") #выбранный тогл "Начинки" в конструкторе

    # Локаторы на странице личного кабинета
    PROFILE = (By.XPATH, "//a[contains(text(),'Профиль')]") #кнопка "Профиль"
    EXIT_BUTTON = (By.XPATH, "//button[contains(text(),'Выход')]") #кнопка "Выход"

    #Локаторы для шапки страницы
    CONSTRUCTOR_BUTTON = (By.XPATH, "//p[contains(text(),'Конструктор')]") #кнопка "Конструктор"
    LOGO = (By.XPATH, "//div[@class='AppHeader_header__logo__2D0X2']") #кнопка с логотипом

    #Локаторы на странцие восстановления пароля
    SIGN_IN_FORGOT_PASSWORD_BUTTON = (By.XPATH, "//a[contains(text(),'Войти')]") #кнопка "Войти"
