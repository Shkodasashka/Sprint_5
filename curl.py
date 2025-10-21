class url():
    main_site = 'https://stellarburgers.education-services.ru'  #главная страница для неавторизованного пользователя
    registration_site = f'{main_site}/register' #страница регистрации нового пользователя
    login_site = f'{main_site}/login' #страница входа заргестрированного пользователя
    sign_site = f'{main_site}/' #главная страница для авторизованного пользователя
    forgot_password_site = f'{main_site}/forgot-password' #страница восстановления пароля
    profile_site = f'{main_site}/account/profile' #страница профиля авторизованного пользователя