# Sprint_5

Подгтовлено 13 тестов, распределенных по функциональности на 5 файлов:
1. Тесты на регистрацию нового пользователя (файл test_registartion_form.py):
1.1. Проверка успешной регистрации пользователя - test_success_registration.
1.2.Проверка валидации поля "Пароль" при вводе некорректного пароля (5 символов) - test_unsuccess_registration_with_invalid_password.

2. Тесты на проверку входа в аккаунт зарегестрированного пользователя (файл test_sing_in_account.py):
2.1. Проверка входа по кнопке "Войти в аккаунт" на главной - test_success_sign_click_on_sign_in_account.
2.2. Проверка входа через кнопку "личный кабинет" - test_success_sign_click_on_sign_in_personal_account.
2.3. Проверка входа через кнопку в форме регистрации - test_success_sign_click_on_sign_sing_in_form_of_registration.
2.4. Проверка входа через кнопку в форме восстановления пароля - test_success_sign_click_on_sign_sing_in_forgot_password_form.

3. Тест на проверку перехода в личный кабинет (файл test_enter_in_personal_account_profile.py):
3.1. Проверка перехода по клику на "Личный кабинет" - test_success_sign_click_on_enter_in_personal_account.

4. Тесты на проверку перехода из личного кабинета в конструктор (файл test_switch_to_constructor.py):
4.1. Проверка перехода по клику на "Конструктор" - test_success_sign_click_on_switch_to_constructor.
4.2. Проверка перехода по клику на логотип Stellar Burgers - est_success_sign_click_on_switch_on_logo_stellar_burgers.

5. Тест на проверку выхода из аккаунта (файл test_logout_of_account.py):
5.1. Проверка выхода по кнопке "Выйти" в личном кабинете - test_success_exit_with_click_on_button_in_personal_account.

6. Тесты на проверку переходов по разделам "Конструктора" (файл test_in_constructor_go_to_sections.py):
6.1. Проверка перехода в раздел "Начинки" - test_success_in_constructor_go_to_section_staffing.
6.2. Проверка перехода в раздел "Соусы" - test_success_in_constructor_go_to_section_sauce.
6.3. Проверка перехода в раздел "Булки" - test_success_in_constructor_go_to_section_bread.

Файл conftest.py - фикстура открытия и закрытия браузера Chrome

Файл curl.py - ссылки на страницы приложения

Файл data.py - данные зарегестрированного пользователя

Файл helper.py - генератор имени, почты и пароля для проверки формы регистрации нового пользователя

Файл locators.py - локаторы элементов на страницах для тестов