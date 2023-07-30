from selenium.webdriver.common.by import By


class Locators:

    #Страница авторизации
    LOG_FIELD = (By.XPATH, "//fieldset[1]//input") #поле логина
    PASS_FIELD = (By.XPATH, "//fieldset[2]//input") #поле пароля
    LOG_BUTTON = (By.XPATH, "//button[contains(text(),'Войти')]") #кнопка Войти
    TRANS_REG_BUTTON = (By.XPATH, "//a[contains(text(),'Зарегистрироваться')]") #кнопка для перехода на страницу регистрации
    TRANS_PASS_REC_BUTTON = (By.XPATH, "//a[contains(text(),'Восстановить пароль')]") #кнопка для перехода на страницу восстановления пароля
    AUTH_PANEL = (By.XPATH, "//form[contains(@class, 'Auth_form')]") #парель с полями для авторизации

    #Главная страница
    CONST_BUTTON = (By.XPATH, ".//p[contains(text(),'Конструктор')]") #Кнопка "Конструктор"
    ORD_FEED_BUTTON = (By.XPATH, ".//p[contains(text(),'Лента Заказов')]") #Кнопка "Лента заказов"
    LOGO = (By.XPATH, "//div[contains(@class, 'AppHeader_header__logo')]") #Логотип
    PERS_ACC_BUTTON = (By.XPATH, "//p[contains(text(),'Личный Кабинет')]") #Кнопка "Личный кабинет"
    ENT_ACC_BUTTON = (By.XPATH, "//button[contains(@class,'button_button_type_primary')]") #Кнопка "Войти в аккаунт"
    MENU_BURG_INGR = (By.XPATH, "//div[contains(@class, 'BurgerIngredients_ingredients__menuContainer')]") #панелька с ингредиентами

    #Страница регистрации
    REG_HEADER = (By.XPATH, "//h2[contains(text(),'Регистрация')]") #заголовок 'Регистрация'
    REG_NAME_FIELD = (By.XPATH, "//fieldset[1]//input") #поле "Имя"
    REG_EMAIL_FIELD = (By.XPATH, "//fieldset[2]//input") #поле "Email"
    REG_PASS_FIELD = (By.XPATH, "//fieldset[3]//input") #поле "Пароль"
    REG_BUTTON = (By.XPATH, "//button[contains(text(),'Зарегистрироваться')]") #кнопка "Зарегистрироваться"
    REG_LOG_BUTTON = (By.XPATH, "//a[contains(text(),'Войти')]") #кнопка "Войти"
    INCORR_PASS = (By.XPATH, "//p[@class='input__error text_type_main-default']") #текст "Некорректный пароль"

    #Страница профиля
    PROF_NAME_FIELD = (By.XPATH, "//li[1]//input") #поле "Имя"
    PROF_EMAIL_FIELD = (By.XPATH, "//li[2]//input") #поле "Email"
    PROF_EXIT_BUTTON = (By.XPATH, "//button[contains(@class, 'Account_button')]") #кнопка "Выход"