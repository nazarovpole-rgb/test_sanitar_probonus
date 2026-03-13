# locators.py
import re


class LocatorTypes:
    """Типы локаторов"""
    ROLE = "role"
    TEXT = "text"
    LABEL = "label"
    LOCATOR = "locator"
    ID = "id"
    

class RoleTypes:
    """Типы ролей"""
    TEXTBOX = "textbox"
    BUTTON = "button"
    LINK = "link"
    CELL = "cell"
    COLUMNHEADER = "columnheader"
    BANNER = "banner"
    HEADING = "heading"
    SWITCH = "switch"
    MAIN = "main"
    TABLE = "table"
    FORM = "form"


class Locators:
    """База переменных для хранения всех локаторов ProBonus"""
    
    # ========== Базовые элементы ==========
    # Логин
    LOGIN_FIELD = {LocatorTypes.ROLE: RoleTypes.TEXTBOX, "name": "Логин"}
    PASSWORD_FIELD = {LocatorTypes.ROLE: RoleTypes.TEXTBOX, "name": "Пароль"}
    LOGIN_BUTTON = {LocatorTypes.ROLE: RoleTypes.BUTTON, "name": "Войти"}
    
    # Заголовок после входа
    PROBONUS_HEADER = {LocatorTypes.ROLE: RoleTypes.BANNER, LocatorTypes.TEXT: "ProBonus"}
    APP_TEXT = {LocatorTypes.TEXT: "app:"}
    DB_TEXT = {LocatorTypes.TEXT: "db:"}
    USER_TEXT = {LocatorTypes.TEXT: "user"}
    
    # Лицензия
    LICENSE_BUTTON = {LocatorTypes.ROLE: RoleTypes.BUTTON, "name": "Лицензия до:"}
    LICENSE_INFO_TEXT = {LocatorTypes.TEXT: "Информация о лицензии"}
    
    # Первая переменная в лицензии, вторая на кнопке r_keeper
    LICENSE_CLOSE_BUTTON1= {
    LocatorTypes.LOCATOR: "//div[.//span[text()='Информация о лицензии']]//div[@class='v-card__actions']//button[.//span[text()='Закрыть']]",
    "nth": 0
}
    LICENSE_CLOSE_BUTTON2 = {
    LocatorTypes.LOCATOR: "//div[contains(@class, 'v-dialog--active')]//span[contains(text(), 'r_keeper')]//ancestor::div[contains(@class, 'v-card')]//button[contains(@class, 'v-btn--icon')]",
}
    
    # R-Keeper соединение
    RKEEPER_OK_BUTTON = {LocatorTypes.ROLE: RoleTypes.BUTTON, "name": "r_keeper ок"}
    RKEEPER_CONNECTION_TEXT_MAIN = {LocatorTypes.TEXT: "Соединение с r_keeper", "exact": True}
    RKEEPER_SUCCESS_TEXT = {LocatorTypes.TEXT: "Соединение с r_keeper успешно установлено"}
    RKEEPER_CHECK_BUTTON = {LocatorTypes.ROLE: RoleTypes.BUTTON, "name": "Проверить соединение"}
    
    
    # ========== Тексты ==========
    # Дашборд тексты
    DASHBOARD_TEXT = {LocatorTypes.TEXT: "Дашборд"}
    SUMMARY_METRICS_TEXT = {LocatorTypes.TEXT: "Суммарные показатели"}
    DYNAMICS_METRICS_TEXT = {LocatorTypes.TEXT: "Динамика показателей"}
    GUEST_BASE_CHARACTERISTICS_TEXT = {LocatorTypes.TEXT: "Характеристики гостевой базы"}
    CHECKS_COUNT_TEXT = {LocatorTypes.TEXT: "Количество чеков", "exact": True}
    CHECKS_SUM_TEXT = {LocatorTypes.TEXT: "Сумма чеков"}
    AVERAGE_CHECK_TEXT = {LocatorTypes.TEXT: "Средний чек"}
    DISCOUNTS_SUM_TEXT = {LocatorTypes.TEXT: "Сумма скидок"}
    BONUSES_ACCRUED_TEXT = {LocatorTypes.TEXT: "Бонусов начислено"}
    BONUSES_SPENT_TEXT = {LocatorTypes.TEXT: "Бонусов потрачено"}
    BASE_VOLUME_TEXT = {LocatorTypes.TEXT: "Объем базы"}
    BASE_GROWTH_TEXT = {LocatorTypes.TEXT: "Прирост базы"}
    ACTIVE_CLIENTS_TEXT = {LocatorTypes.TEXT: "Активных клиентов"}
    LOYALTY_PENETRATION_TEXT = {LocatorTypes.TEXT: "Проникновение системы лояльности"}
    ACCOUNT_GROUPS_DIVISION_TEXT = {LocatorTypes.TEXT: "Деление по группам счетов"}
    GENDER_TEXT = {LocatorTypes.TEXT: "Пол", "exact": True}
    AGE_TEXT = {LocatorTypes.TEXT: "Возраст"}
    START_DATE_TEXT = {LocatorTypes.TEXT: "Начало"}
    END_DATE_TEXT = {LocatorTypes.TEXT: "Конец", "exact": True}
    
    # Wallet file

    FILE_INPUT_WALLET = {
        LocatorTypes.LOCATOR: "xpath=//label[normalize-space()='Сертификат Wallet загружен на сервер']"
    }
    FILE_PRIVATE_KEY = {
        LocatorTypes.LOCATOR: "xpath=//label[contains(text(), 'Приватный ключ сертификата Wallet загружен на сервер')]"
    }
    FILE_SERT_APPLE = {
        LocatorTypes.LOCATOR: "xpath=//label[contains(text(), 'Сертификат WWDR от Apple загружен на сервер')]"
    }






    TYPE_COUP_TEXT610 = {
    LocatorTypes.LOCATOR: 'xpath=//input[@test-tag="tag-610"]'
}
    # Навигация тексты
    MANAGEMENT_TEXT = {LocatorTypes.TEXT: "Управление"}
    ACTIONS_TEXT = {LocatorTypes.TEXT: "Акции"}
    SEGMENTS_TEXT = {LocatorTypes.TEXT: "Сегменты"}
    MAILINGS_TEXT = {LocatorTypes.TEXT: "Рассылки"}
    WALLET_TEXT = {LocatorTypes.TEXT: "Wallet"}
    ANTIFRAUD_TEXT = {LocatorTypes.TEXT: "Антифрод"}
    IMPORT_TEXT = {LocatorTypes.TEXT: "Импорт"}
    REPORTS_TEXT = {LocatorTypes.TEXT: "Отчеты"}
    SETTINGS_TEXT = {LocatorTypes.TEXT: "Настройки"}
    PROBONUS_API_TEXT = {LocatorTypes.TEXT: "ProBonus API"}
    HELP_TEXT = {LocatorTypes.TEXT: "Помощь"}
    EXIT_TEXT = {LocatorTypes.TEXT: "Выход"}
    
    # ========== Кнопки навигации ==========
    MANAGEMENT_BUTTON = {LocatorTypes.ROLE: RoleTypes.BUTTON, "name": "Управление"}
    ACTIONS_BUTTON = {LocatorTypes.ROLE: RoleTypes.BUTTON, "name": "Акции"}
    SEGMENTS_BUTTON = {LocatorTypes.ROLE: RoleTypes.BUTTON, "name": "Сегменты"}
    MAILINGS_BUTTON = {LocatorTypes.ROLE: RoleTypes.BUTTON, "name": "Рассылки"}
    WALLET_BUTTON = {LocatorTypes.ROLE: RoleTypes.BUTTON, "name": "Wallet"}
    ANTIFRAUD_BUTTON = {LocatorTypes.ROLE: RoleTypes.BUTTON, "name": "Антифрод"}
    IMPORT_BUTTON = {LocatorTypes.ROLE: RoleTypes.BUTTON, "name": "Импорт"}
    REPORTS_BUTTON = {LocatorTypes.ROLE: RoleTypes.BUTTON, "name": "Отчеты"}
    SETTINGS_BUTTON = {LocatorTypes.ROLE: RoleTypes.BUTTON, "name": "Настройки"}
    PROBONUS_API_LINK = {LocatorTypes.ROLE: RoleTypes.LINK, "name": "ProBonus API"}
    HELP_LINK = {LocatorTypes.ROLE: RoleTypes.LINK, "name": "Помощь"}
    EXIT_BUTTON = {LocatorTypes.LOCATOR: "div", "has_text": re.compile(r"^Выход$"), "nth": 1}
    
    # ========== Управление -> Счета ==========
    ACCOUNTS_LINK = {LocatorTypes.ROLE: RoleTypes.LINK, "name": "Счета"}
    GROUP_OPERATIONS_BUTTON = {LocatorTypes.ROLE: RoleTypes.BUTTON, "name": "Групповые операции"}
    TABLE_SETTINGS_BUTTON = {
    LocatorTypes.LOCATOR: "//button[contains(@class, 'v-btn') and contains(@class, 'blue') and contains(@class, 'darken-3')]"
                          "[.//span[contains(@class, 'v-btn__content') and normalize-space(.)='Настройки таблицы']]",
}
    TABLE_SETTINGS_TEXT = {
        LocatorTypes.LOCATOR: "//div[contains(@class, 'v-card__title')][contains(normalize-space(.), 'Настройки таблицы')]"
    }    
    APPLY_BUTTON = {LocatorTypes.ROLE: RoleTypes.BUTTON, "name": "Применить"}
    DEFAULT_BUTTON = {LocatorTypes.ROLE: RoleTypes.BUTTON, "name": "По умолчанию"}
    CANCEL_BUTTON = {LocatorTypes.ROLE: RoleTypes.BUTTON, "name": "Отмена"}
    CANCEL_GROUP_BUTTON = {
    LocatorTypes.LOCATOR: "button[test-tag='tag-545']:has-text('Отмена')"
}
    CANCEL_BUTTON_MANUAL = {
    LocatorTypes.LOCATOR: "//button[contains(@class, 'v-btn') and contains(@class, 'blue--text') and contains(@class, 'text--darken-1') and .//span[text()='Отмена']]"
}

    # На странице присутсвует ПОИСК
    SEARCH_FIELD1 = {  
        LocatorTypes.LOCATOR: "(//input[@type='text'])[1]"
    }

    SEARCH_FIELD = {
    LocatorTypes.LOCATOR: "//div[contains(@class, 'v-text-field__slot')]//input[preceding-sibling::label[text()='Поиск']]"
}
    ROWS_PER_PAGE_TEXT = {
    LocatorTypes.LOCATOR: "//div[contains(@class,'v-data-table')]//div[contains(@class,'v-data-footer__select')]"
}
    ADD_ACCOUNT_BUTTON = {LocatorTypes.ROLE: RoleTypes.BUTTON, "name": "Добавить счёт"}
    # ==========Кнопки сохранить в файл/Выгрузить в xlsx==========
    SAVE_TO_FILE_BUTTON49 = {
    LocatorTypes.LOCATOR: "//button[@test-tag='tag-49']"
}    
    SAVE_TO_FILE_BUTTON174 = {
    LocatorTypes.LOCATOR: "//button[@test-tag='tag-174']"
}    

    # ========== Управление -> Группы Счетов ==========
    ACCOUNT_GROUPS_LINK = {LocatorTypes.ROLE: RoleTypes.LINK, "name": "Группы Счетов"}
    ADD_ACCOUNT_GROUP_BUTTON = {LocatorTypes.ROLE: RoleTypes.BUTTON, "name": "Добавить Группу счетов"}
    
    # ========== Управление -> Составные скидки/бонусы ==========
    COMPOUND_DISCOUNTS_LINK = {LocatorTypes.ROLE: RoleTypes.LINK, "name": "Составные скидки/бонусы"}
    ADD_MANUALLY_BUTTON = {LocatorTypes.ROLE: RoleTypes.BUTTON, "name": "Добавить Вручную"}
    
    # ========== Управление -> Пользователи ==========
    USERS_LINK = {LocatorTypes.ROLE: RoleTypes.LINK, "name": "Пользователи"}
    ADD_USER_BUTTON = {LocatorTypes.TEXT: "Добавить Пользователя", "exact": True}
    ADD_API_USER_BUTTON = {LocatorTypes.TEXT: "Добавить Пользователя API", "exact": True}
    
    # ========== Управление -> Роли ==========
    ROLES_LINK = {LocatorTypes.ROLE: RoleTypes.LINK, "name": "Роли"}
    ADD_ROLE_BUTTON = {
    LocatorTypes.LOCATOR: "button[test-tag='tag-518']:has-text('Добавить роль')"
}

    # ========== Управление -> Отзывы ==========
    REVIEWS_LINK = {LocatorTypes.ROLE: RoleTypes.LINK, "name": "Отзывы"}
    APPLY_FILTER_BUTTON = {LocatorTypes.ROLE: RoleTypes.BUTTON, "name": "Применить фильтр"}
    
    # ========== Управление -> Товарные купоны ==========
    PRODUCT_COUPONS_LINK = {LocatorTypes.ROLE: RoleTypes.LINK, "name": "Товарные купоны"}
    ADD_PRODUCT_COUPON_BUTTON = {LocatorTypes.ROLE: RoleTypes.BUTTON, "name": "Добавление товарного купона"}
    
    # ========== Управление -> Теги счетов ==========
    ACCOUNT_TAGS_LINK = {LocatorTypes.ROLE: RoleTypes.LINK, "name": "Теги счетов"}
    ADD_TAG_BUTTON = {LocatorTypes.ROLE: RoleTypes.BUTTON, "name": "Добавить Тег"}
    ADD_GROUP_BUTTON = {LocatorTypes.ROLE: RoleTypes.BUTTON, "name": "Добавить группу"}
    
    # ========== Акции -> Штампики ==========
    STAMPS_LINK = {LocatorTypes.ROLE: RoleTypes.LINK, "name": "Штампики (N+1)"}
    ADD_STAMP_ACTION_BUTTON = {
    LocatorTypes.LOCATOR: "//button[@test-tag='tag-415']"
}
    
    # ========== Акции -> Сегментные акции ==========
    SEGMENT_ACTIONS_LINK = {LocatorTypes.ROLE: RoleTypes.LINK, "name": "Сегментные акции"}
    ADD_SEGMENT_ACTION_BUTTON = {LocatorTypes.ROLE: RoleTypes.BUTTON, "name": "Добавить акцию"}
    
    # ========== Акции -> Промокоды ==========
    PROMOCODES_LINK = {LocatorTypes.ROLE: RoleTypes.LINK, "name": "Промокоды"}
    ADD_PROMOCODE_BUTTON = {LocatorTypes.ROLE: RoleTypes.BUTTON, "name": "Добавить промокод"}
    
    # ========== Акции -> Триггерные акции ==========
    TRIGGER_ACTIONS_LINK = {LocatorTypes.ROLE: RoleTypes.LINK, "name": "Триггерные акции"}
    ADD_TRIGGER_ACTION_BUTTON = {LocatorTypes.ROLE: RoleTypes.BUTTON, "name": "Добавить триггерную акцию"}
    
    # ========== Акции -> Логи акций ==========
    ACTION_LOGS_LINK = {LocatorTypes.ROLE: RoleTypes.LINK, "name": "Логи акций"}
    EXPORT_TO_XLSX_BUTTON430= {LocatorTypes.LOCATOR: "//button[@test-tag='tag-430']"}    
    EXPORT_TO_XLSX_BUTTON454= {LocatorTypes.LOCATOR: "//button[@test-tag='tag-454']"}    
    # ========== Акции -> История акций ==========
    ACTION_HISTORY_LINK = {LocatorTypes.ROLE: RoleTypes.LINK, "name": "История акций"}
    
    # ========== Акции -> Реферальная программа ==========
    REFERRAL_PROGRAM_LINK = {LocatorTypes.ROLE: RoleTypes.LINK, "name": "Реферальная программа"}
    
    # ========== Сегменты -> Список сегментов ==========
    SEGMENTS_LIST_LINK = {LocatorTypes.ROLE: RoleTypes.LINK, "name": "Список сегментов"}
    ADD_SEGMENT_BUTTON530 = {LocatorTypes.LOCATOR: "//button[@test-tag='tag-530']"}    

    # ========== Рассылки -> Новая рассылка ==========
    NEW_MAILING_LINK = {LocatorTypes.ROLE: RoleTypes.LINK, "name": "Новая рассылка"}
    
    # ========== Рассылки -> Настройки ==========
    MAILING_SETTINGS_LINK = {LocatorTypes.ROLE: RoleTypes.LINK, "name": "Настройки"}
    CHECK_AND_SAVE_BUTTON = {LocatorTypes.ROLE: RoleTypes.BUTTON, "name": "Проверить и сохранить"}
    
    # ========== Рассылки -> История ==========
    MAILING_HISTORY_LINK = {LocatorTypes.ROLE: RoleTypes.LINK, "name": "История"}
    
    # ========== Wallet -> Основные настройки ==========
    WALLET_MAIN_SETTINGS_LINK = {LocatorTypes.ROLE: RoleTypes.LINK, "name": "Основные настройки"}
    
    # ========== Wallet -> Настройки анкеты гостя ==========
    WALLET_GUEST_FORM_SETTINGS_LINK = {LocatorTypes.ROLE: RoleTypes.LINK, "name": "Настройки анкеты гостя"}
    
    # ========== Wallet -> Макеты карт ==========
    WALLET_CARD_TEMPLATES_LINK = {LocatorTypes.ROLE: RoleTypes.LINK, "name": "Макеты карт"}
    ADD_TEMPLATE_BUTTON = {LocatorTypes.ROLE: RoleTypes.BUTTON, "name": "Добавить макет"}
    
    # ========== Wallet -> Баланс ==========
    WALLET_BALANCE_LINK = {LocatorTypes.ROLE: RoleTypes.LINK, "name": "Баланс"}
    REQUEST_INVOICE_BUTTON = {LocatorTypes.ROLE: RoleTypes.BUTTON, "name": "Запросить счет для пополнения баланса"}
    
    # ========== Wallet -> Geo push ==========
    WALLET_GEO_PUSH_LINK = {LocatorTypes.ROLE: RoleTypes.LINK, "name": "Geo push"}
    ADD_LOCATION_BUTTON = {LocatorTypes.ROLE: RoleTypes.BUTTON, "name": "Добавить локацию"}
    
    # ========== Антифрод -> Настройки ==========
    ANTIFRAUD_SETTINGS_LINK = {LocatorTypes.ROLE: RoleTypes.LINK, "name": "Настройки"}
    MAIN_SETTINGS_BUTTON = {LocatorTypes.ROLE: RoleTypes.BUTTON, "name": "Основные настройки"}
    EMAIL_NOTIFICATIONS_BUTTON = {LocatorTypes.ROLE: RoleTypes.BUTTON, "name": "Email-оповещения"}
    TELEGRAM_NOTIFICATIONS_BUTTON = {LocatorTypes.ROLE: RoleTypes.BUTTON, "name": "Telegram-оповещения"}
    EXCEPTIONS_BUTTON = {LocatorTypes.ROLE: RoleTypes.BUTTON, "name": "Исключения"}
    
    # ========== Антифрод -> Отчёт ==========
    ANTIFRAUD_REPORT_LINK = {LocatorTypes.ROLE: RoleTypes.LINK, "name": "Отчёт"}
    
    # ========== Импорт -> Импорт Счетов ==========
    IMPORT_ACCOUNTS_LINK = {LocatorTypes.ROLE: RoleTypes.LINK, "name": "Импорт Счетов"}
    
    # ========== Импорт -> Импорт Потрат ==========
    IMPORT_SPENDS_LINK = {LocatorTypes.ROLE: RoleTypes.LINK, "name": "Импорт Потрат"}
    
    # ========== Отчеты -> Питание с дотациями ==========
    SUBSIDIZED_MEALS_LINK = {LocatorTypes.ROLE: RoleTypes.LINK, "name": "Питание с дотациями"}
    
    # ========== Отчеты -> Суммовой ==========
    TOTAL_REPORT_LINK = {LocatorTypes.ROLE: RoleTypes.LINK, "name": "Суммовой"}
    
    # ========== Отчеты -> Транзакции ==========
    TRANSACTIONS_REPORT_LINK = {LocatorTypes.ROLE: RoleTypes.LINK, "name": "Транзакции"}
    
    # ========== Отчеты -> Идентификаторы ==========
    IDENTIFIERS_REPORT_LINK = {LocatorTypes.ROLE: RoleTypes.LINK, "name": "Идентификаторы"}
    
    # ========== Отчеты -> Потраты по дням ==========
    SPENDS_BY_DAY_LINK = {LocatorTypes.ROLE: RoleTypes.LINK, "name": "Потраты по дням"}
    
    # ========== Отчеты -> Дни рождения ==========
    BIRTHDAYS_REPORT_LINK = {LocatorTypes.ROLE: RoleTypes.LINK, "name": "Дни рождения"}
    
    # ========== Отчеты -> Бездействующие счета ==========
    INACTIVE_ACCOUNTS_LINK = {LocatorTypes.ROLE: RoleTypes.LINK, "name": "Бездействующие счета"}
    
    # ========== Отчеты -> Потерянные гости ==========
    LOST_GUESTS_LINK = {LocatorTypes.ROLE: RoleTypes.LINK, "name": "Потерянные гости"}
    
    # ========== Отчеты -> Прирост гостевой базы ==========
    GUEST_BASE_GROWTH_LINK = {LocatorTypes.ROLE: RoleTypes.LINK, "name": "Прирост гостевой базы"}
    TOP_GUESTS_NAV_LINK = {LocatorTypes.ROLE: RoleTypes.LINK, "name": "Топ гостей"}
    
    # ========== Отчеты -> Топ гостей ==========
    TOP_GUESTS_LINK = {LocatorTypes.ROLE: RoleTypes.MAIN, LocatorTypes.TEXT: "Топ гостей", "exact": True}
    
    # ========== Отчеты -> Оборот товарных купонов ==========
    PRODUCT_COUPONS_TURNOVER_LINK = {LocatorTypes.ROLE: RoleTypes.LINK, "name": "Оборот товарных купонов"}
    
    # ========== Отчеты -> Отчет Штампики ==========
    STAMPS_REPORT_LINK = {LocatorTypes.ROLE: RoleTypes.LINK, "name": "Отчет \"Штампики\""}
    
    # ========== Отчеты -> Отчет Промокоды ==========
    PROMOCODES_REPORT_LINK = {LocatorTypes.ROLE: RoleTypes.LINK, "name": "Отчет \"Промокоды\""}
    
    # ========== Отчеты -> Дашборд ==========
    DASHBOARD_REPORT_LINK = {LocatorTypes.ROLE: RoleTypes.LINK, "name": "Дашборд"}
    
    # ========== Отчеты -> Реферальная программа ==========
    REFERRAL_PROGRAM_REPORT_LINK = {LocatorTypes.ROLE: RoleTypes.LINK, "name": "Реферальная программа"}
    SHOW_CHART_BUTTON = {LocatorTypes.ROLE: RoleTypes.BUTTON, "name": "Показать график"}
    
    # ========== Отчеты -> Выгрузка счетов ==========
    ACCOUNTS_EXPORT_LINK = {LocatorTypes.ROLE: RoleTypes.LINK, "name": "Выгрузка счетов"}
    EXPORT_ACCOUNTS_TO_XLSX_BUTTON = {LocatorTypes.ROLE: RoleTypes.BUTTON, "name": "Выгрузить информацию по счетам в XLSX"}
    
    # ========== Настройки -> Соединение с БД ==========
    DB_CONNECTION_LINK = {LocatorTypes.ROLE: RoleTypes.LINK, "name": "Соединение с БД"}
    ASSISTANT_BUTTON = {LocatorTypes.ROLE: RoleTypes.BUTTON, "name": "Помощник"}
    
    # ========== Настройки -> R_Keeper ==========
    RKEEPER_SETTINGS_LINK = {LocatorTypes.ROLE: RoleTypes.LINK, "name": "R_Keeper"}
    SAVE_BUTTON = {LocatorTypes.ROLE: RoleTypes.BUTTON, "name": "Сохранить", "exact": True}
    
    # ========== Настройки -> Настройки сервера ==========
    SERVER_SETTINGS_LINK = {LocatorTypes.ROLE: RoleTypes.LINK, "name": "Настройки сервера"}
    
    # ========== Настройки -> Настройки ProBonus ==========
    PROBONUS_SETTINGS_LINK = {LocatorTypes.ROLE: RoleTypes.LINK, "name": "Настройки ProBonus"}
    
    # ========== Настройки -> Регистрация с кассы ==========
    CASH_REGISTRATION_LINK = {LocatorTypes.ROLE: RoleTypes.LINK, "name": "Регистрация с кассы"}
    ADD_REGISTRATION_BUTTON = {LocatorTypes.ROLE: RoleTypes.BUTTON, "name": "Добавить"}
    
    # ========== Настройки -> Инфокиоск ==========
    INFO_KIOSK_LINK = {LocatorTypes.ROLE: RoleTypes.LINK, "name": "Инфокиоск"}
    
    # ========== Настройки -> Типы идентификаторов ==========
    IDENTIFIER_TYPES_LINK = {LocatorTypes.ROLE: RoleTypes.LINK, "name": "Типы идентификаторов"}
    ADD_IDENTIFIER_TYPE_BUTTON = {LocatorTypes.ROLE: RoleTypes.BUTTON, "name": "Добавить Тип Идентификатора"}
    
    # ========== Настройки -> Рестораны ==========
    RESTAURANTS_LINK = {LocatorTypes.ROLE: RoleTypes.LINK, "name": "Рестораны"}
    ADD_RESTAURANT_BUTTON = {LocatorTypes.ROLE: RoleTypes.BUTTON, "name": "Добавить Ресторан"}
    
    # ========== Настройки -> Telegram-Бот ==========
    TELEGRAM_BOT_LINK = {LocatorTypes.ROLE: RoleTypes.LINK, "name": "Telegram-Бот"}
    
    # ========== Настройки -> Описание и политики ==========
    DESCRIPTION_POLICIES_BUTTON = {LocatorTypes.ROLE: RoleTypes.BUTTON, "name": "Описание и политики"}
    
    # ========== Настройки -> Фразы ==========
    PHRASES_BUTTON = {LocatorTypes.ROLE: RoleTypes.BUTTON, "name": "Фразы"}
    
    # ========== Дополнительные тексты ==========
    WORK_WITH_REVIEWS_TEXT = {LocatorTypes.TEXT: "Работа с отзывами гостей"}
    RESTAURANT_TEXT = {LocatorTypes.TEXT: "Ресторан", "exact": True}
    ACTIONS_TEXT = {LocatorTypes.TEXT: "Действия"}
    ID_TEXT = {LocatorTypes.TEXT: "id"}
    NAME_TEXT = {LocatorTypes.TEXT: "Наименование"}
    ACCOUNT_GROUP_NAME_FIELD = ACCOUNT_GROUP_NAME_FIELD = {LocatorTypes.LOCATOR: "//div[contains(@class, 'v-dialog')]//input[@id=//label[text()='Наименование']/@for]"}
    DISCOUNT_BONUS_TEXT = {LocatorTypes.TEXT: "Скидка/бонус", "exact": True}
    MASTER_ADDITION_BUTTON = {LocatorTypes.LOCATOR: "//button[.//span[text()='Мастер Добавления']]"}
    BALANCE_TEXT = {LocatorTypes.TEXT: "Баланс"}
    ACTION_TEXT = {LocatorTypes.TEXT: "Действие"}
    LOGIN_TEXT = {LocatorTypes.TEXT: "Логин"}
    USER_TYPE_TEXT = {LocatorTypes.TEXT: "Тип пользователя"}
    DISCOUNT_CODE_TEXT = {LocatorTypes.TEXT: "Код скидки"}
    DISH_NAME_TEXT = {LocatorTypes.TEXT: "Название блюда:"}
    TAG_NAME_TEXT = {LocatorTypes.TEXT: "Название"}
    TAG_GROUP_TEXT = {LocatorTypes.TEXT: "Группа"}
    STAMP_NAME_TEXT = {LocatorTypes.TEXT: "Наименование"}
    START_DATE_INPUT = {LocatorTypes.TEXT: "Начало"}
    END_DATE_INPUT = {LocatorTypes.TEXT: "Конец"}
    PORTIONS_BUY = {LocatorTypes.ROLE: "spinbutton", "name": "Порций купить"}
    GIFT_PORTIONS = {LocatorTypes.ROLE: "spinbutton", "name": "Подарочных порций"}
    DISCOUNT_CODE_INPUT = {LocatorTypes.ROLE: "spinbutton", "name": "Код скидки"}
    PROMOTIONAL_DISHES_TEXT = {LocatorTypes.TEXT: "Акционные блюда"}
    GIFT_DISHES_TEXT = {LocatorTypes.TEXT: "Подарочные блюда"}
    SEGMENT_NAME_TEXT = {LocatorTypes.TEXT: "Название сегмента"}
    SEGMENT_TYPE_TEXT = {LocatorTypes.TEXT: "Тип сегмента"}
    START_DATE_SEGMENT_TEXT = {LocatorTypes.TEXT: "Дата начала"}
    START_DATE_SEGMENT = {
        LocatorTypes.ROLE: RoleTypes.TEXTBOX,
        LocatorTypes.TEXT: "Дата начала"          
    }

    END_DATE_SEGMENT_TEXT = {LocatorTypes.TEXT: "Дата окончания", "exact": True}
    DATE_END_FIELD = {
        LocatorTypes.LABEL: "Дата окончания",
        "exact": True
    }
    
    FREQUENCY_TEXT = {LocatorTypes.TEXT: "Периодичность"}
    LAST_TRIGGER_TEXT = {LocatorTypes.TEXT: "Последнее срабатывание заняло времени (сек.)"}
    NEXT_TRIGGER_TEXT = {LocatorTypes.TEXT: "Следующее срабатывание"}
    PROMOCODE_TYPE_TEXT = {LocatorTypes.TEXT: "Тип"}
    INPUT_PHRASE_TEXT = {LocatorTypes.TEXT: "Фраза для ввода"}
    DONT_SHOW_ENDED_TEXT = {LocatorTypes.TEXT: "Не показывать закончившиеся"}
    ACCOUNT_GROUP_TEXT = {LocatorTypes.TEXT: "Группа счетов"}
    ACTION_ACTIVE_TEXT = {LocatorTypes.TEXT: "Акция активна"}
    ACTION_LOGS_TEXT = {LocatorTypes.TEXT: "Логи применения акций"}
    ACTION_HISTORY_TEXT = {LocatorTypes.TEXT: "История применения акций"}
    REFERRAL_ENABLE_TEXT = {LocatorTypes.TEXT: "Включить реферальную программу?"}
    REFERRER_TEXT = {LocatorTypes.TEXT: "Приглашающий"}
    BONUS_TYPE_TEXT = {
    LocatorTypes.LOCATOR: '[test-tag="tag-612"]'
    }
    REFERRAL_REWARD_TYPE_FIELD = {
        LocatorTypes.LOCATOR: '//label[normalize-space(.) = "Тип вознаграждения"]/following-sibling::div[contains(@class, "v-select__selections")]/input'
    }
    ACCRUAL_SUM_TEXT = {LocatorTypes.TEXT: "Сумма начисления"}
    CONDITION_TEXT613 = {
    LocatorTypes.LOCATOR: '[test-tag="tag-613"]'
}
    CONDITION_TEXT615 = {
    LocatorTypes.LOCATOR: '[test-tag="tag-615"]'
}
    BOT_BUTTON_TEXT_TEXT = {LocatorTypes.TEXT: "Текст на кнопке бота"}
    REFERRAL_DESCRIPTION_TEXT = {LocatorTypes.TEXT: "Описание реферальной программы"}
    FRIEND_REG_MESSAGE_TEXT = {LocatorTypes.TEXT: "Сообщение о регистрации друга"}
    REFERRAL_GROUP_CREATE_FIELD = {
    LocatorTypes.LOCATOR: '[test-tag="tag-77"]'
}
    REFERRAL_REWARD_MESSAGE_TEXT = {LocatorTypes.TEXT: "Сообщение о получении вознаграждения за друга"}
    REFERRED_GUEST_TEXT = {LocatorTypes.TEXT: "Приведенный гость"}
    GUEST_REG_MESSAGE_TEXT = {LocatorTypes.TEXT: "Сообщение для гостя после регистрации"}
    REFERRED_REWARD_MESSAGE_TEXT = {LocatorTypes.TEXT: "Сообщение о получении вознаграждения", "exact": True}
    FOREVER_TEXT = {LocatorTypes.TEXT: "Бессрочно"}
    ACCOUNTS_COUNT_TEXT = {LocatorTypes.TEXT: "Кол-во счетов"}
    PERCENT_TEXT = {LocatorTypes.TEXT: "%"}
    LAST_RECALCULATION_TEXT = {LocatorTypes.TEXT: "Дата/время последнего пересчета"}
    SAVE_TEXT = {LocatorTypes.TEXT: "Сохранить"}
    TOUCH_SWITCH = {
    LocatorTypes.LOCATOR: '[test-tag="tag-671"]'
}
    SAVE_TEXT523 = {
    LocatorTypes.LOCATOR: '[test-tag="tag-523"]'
}
    SAVE_AND_CLOSE_TEXT = {LocatorTypes.TEXT: "Сохранить и закрыть"}
    SAVE_AND_CLOSE_TEXT524 = {
    LocatorTypes.LOCATOR: '[test-tag="tag-524"]'
}
    ADD_SINGLE_MAILING_TEXT = {LocatorTypes.TEXT: "Добавить разовую рассылку"}
    NAME_EXACT_TEXT = {LocatorTypes.TEXT: "Название", "exact": True}
    TRIGGER_DATE_TEXT = {LocatorTypes.TEXT: "Дата срабатывания"}
    TRIGGER_TIME_TEXT = {LocatorTypes.TEXT: "Время срабатывания"}
    PARAMETERS_TEXT = {LocatorTypes.TEXT: "Параметры"}
    MAILING_CHANNELS_TEXT = {LocatorTypes.TEXT: "Каналы для рассылки"}
    EXTERNAL_SYSTEM_TEXT = {LocatorTypes.TEXT: "Внешняя система"}
    SEND_MODE_BUTTON = {LocatorTypes.ROLE: RoleTypes.BUTTON, "name": "Режим отправки"}
    IMAGE_FIELD = {LocatorTypes.ROLE: RoleTypes.TEXTBOX, "name": "Картинка"}
    EMAIL_MAILING_TEXT = {LocatorTypes.TEXT: "Рассылка на почту"}
    ENABLE_EMAIL_MAILING_TEXT = {LocatorTypes.TEXT: "Включить рассылку на почту?"}
    SMTP_SERVER_FIELD = {LocatorTypes.ROLE: RoleTypes.TEXTBOX, "name": "Адрес SMTP-Сервера"}
    SMTP_PORT_TEXT = {LocatorTypes.TEXT: "Порт SMTP-Сервера"}
    SMTP_USER_FIELD = {LocatorTypes.ROLE: RoleTypes.TEXTBOX, "name": "Имя пользователя SMTP-Сервера"}
    SMTP_PASSWORD_FIELD = {LocatorTypes.ROLE: RoleTypes.TEXTBOX, "name": "Здесь сохранен пароль пользователя, но скрыт по соображениям безопасности"}
    MAILING_HISTORY_TEXT = {LocatorTypes.TEXT: "История рассылок"}
    MAILING_TYPE_TEXT = {LocatorTypes.TEXT: "Тип применения акцииРазовая, Периодическая"}
    CREATION_DATE_TEXT = {LocatorTypes.TEXT: "Дата/время создания"}
    MAILING_NAME_TEXT = {LocatorTypes.TEXT: "Название акции"}
    TOTAL_MESSAGES_TEXT = {LocatorTypes.TEXT: "Общее число сообщений"}
    AWAITING_SEND_TEXT = {LocatorTypes.TEXT: "Ожидает отправки"}
    SENT_MESSAGES_TEXT = {LocatorTypes.TEXT: "Отправлено сообщений"}
    SEND_ERROR_TEXT = {LocatorTypes.TEXT: "Ошибка отправки"}
    SEND_CANCELED_TEXT = {LocatorTypes.TEXT: "Отправка отменена"}
    SEND_SPEED_TEXT = {LocatorTypes.TEXT: "Скорость, шт/мин."}
    END_DATE_TIME_TEXT = {LocatorTypes.TEXT: "Дата/время окончания"}
    WALLET_ENABLE_TEXT = {LocatorTypes.TEXT: "Включить Wallet?"}
    PRIVATE_KEY_PASSWORD_FIELD = {LocatorTypes.ROLE: RoleTypes.TEXTBOX, "name": "Здесь сохранен пароль от приватного ключа, но скрыт по соображениям безопасности"}
    PASSTYPE_IDENTIFIER_TEXT = {LocatorTypes.TEXT: "passTypeIdentifier от Apple"}
    TEAM_IDENTIFIER_TEXT = {LocatorTypes.TEXT: "teamIdentifier от Apple"}
    GUEST_FORM_TEXT = {LocatorTypes.TEXT: "Анкета"}
    OBJECT_TEXT = {LocatorTypes.TEXT: "xpath=//th[text()='Объект']"}
    USE_TEXT = {LocatorTypes.TEXT: "Использовать"}
    REQUIRED_TEXT = {LocatorTypes.TEXT: "Обязательное"}
    ADDITIONAL_TEXT = {LocatorTypes.TEXT: "Доп"}
    LOGO_FIELD = {LocatorTypes.ROLE: RoleTypes.TEXTBOX, "name": "Лого"}
    BACKGROUND_FIELD = {LocatorTypes.ROLE: RoleTypes.TEXTBOX, "name": "Подложка"}
    ACCEPT_POLICY_TEXT = {LocatorTypes.TEXT: "Принимать политику обработки перс. данных? - Да"}
    ACCEPT_PRIVACY_TEXT = {LocatorTypes.TEXT: "Принимать политику конфиденциальности? - Да"}
    REGISTRATION_TEXT = {LocatorTypes.TEXT: "Регистрация"}
    UTM_TAGS_TEXT = {LocatorTypes.TEXT: "UTM-Метки"}
    FORM_PREVIEW_TEXT = {LocatorTypes.TEXT: "Предпросмотр анкеты"}
    CARD_SETTINGS_TEXT = {LocatorTypes.TEXT: "Общие настройки карты"}
    TEMPLATE_NAME_EXACT_TEXT = {LocatorTypes.TEXT: "Название макета", "exact": True}
    CARD_DESCRIPTION_TEXT = {LocatorTypes.TEXT: "Описание карты (ресторана)"}
    WILL_BE_SHOWN_TEXT = {LocatorTypes.TEXT: "Будет показано в заголовке"}
    CARD_NAME_TEXT = {LocatorTypes.TEXT: "Название карты (ресторана)"}
    ALLOW_SHARE_TEXT = {LocatorTypes.TEXT: "Разрешить делиться"}
    PUSH_APPEARANCE_TEXT = {LocatorTypes.TEXT: "Настройка внешнего вида PUSH"}
    PUSH_LOGO_FIELD = {LocatorTypes.ROLE: RoleTypes.TEXTBOX, "name": "Логотип для PUSH уведомлений"}
    RESTAURANT_NAME_CAPS_TEXT = {LocatorTypes.TEXT: "НАЗВАНИЕ РЕСТОРАНА"}
    FRONT_SIDE_TEXT = {LocatorTypes.TEXT: "Лицевая сторона"}
    SHOW_ACCOUNT_LEVEL_TEXT = {LocatorTypes.TEXT: "Показывать уровень счета"}
    FIELD_TITLE_TEXT = {LocatorTypes.TEXT: "Заголовок поля"}
    SHOW_OWNER_DATA_TEXT = {LocatorTypes.TEXT: "Показывать данные владельца"}
    SHOW_BALANCE_DATA_TEXT = {LocatorTypes.TEXT: "Показывать данные о балансе"}
    BG_COLOR_BUTTON = {LocatorTypes.ROLE: RoleTypes.BUTTON, "name": "Цвет фона"}
    TITLE_COLOR_BUTTON = {LocatorTypes.ROLE: RoleTypes.BUTTON, "name": "Цвет заголовков"}
    TEXT_COLOR_BUTTON = {LocatorTypes.ROLE: RoleTypes.BUTTON, "name": "Цвет текста"}
    LOGO_EXACT_FIELD = {LocatorTypes.ROLE: RoleTypes.TEXTBOX, "name": "Логотип", "exact": True}
    BIG_LOGO_FIELD = {LocatorTypes.ROLE: RoleTypes.TEXTBOX, "name": "Большой логотип"}
    BACK_SIDE_TEXT = {LocatorTypes.TEXT: "Оборотная сторона"}
    BACK_SIDE_TEXT_FIELD = {LocatorTypes.ROLE: RoleTypes.TEXTBOX, "name": "Текст оборотной стороны"}
    TEMPLATE_NAME_HEADER = {LocatorTypes.TEXT: "Название Макета"}
    TRANSACTIONS_TEXT = {LocatorTypes.TEXT: "Транзакции"}
    DATE_EXACT_TEXT = {LocatorTypes.TEXT: "Дата", "exact": True}
    SUM_HEADER = {LocatorTypes.TEXT: "Сумма"}
    REASON_HEADER = {LocatorTypes.TEXT: "Причина"}
    USER_HEADER = {LocatorTypes.TEXT: "Пользователь"}
    AMOUNT_LABEL = {LocatorTypes.TEXT: "Сумма"}
    INN_FIELD = {LocatorTypes.ROLE: RoleTypes.TEXTBOX, "name": "ИНН ЮЛ плательщика"}
    INVOICE_EMAIL_FIELD = {LocatorTypes.ROLE: RoleTypes.TEXTBOX, "name": "Почта на которую направить счет"}
    CONTACT_PERSON_FIELD = {LocatorTypes.ROLE: RoleTypes.TEXTBOX, "name": "ФИО контактного лица"}
    CONTACT_PHONE_FIELD = {LocatorTypes.ROLE: RoleTypes.TEXTBOX, "name": "Контактный телефон"}
    INVOICE_REQUEST_TEXT = {LocatorTypes.TEXT: "Запрос счета для пополнения баланса"}
    LOCATION_NAME_TEXT = {LocatorTypes.TEXT: "Название точки"}
    MESSAGE_HEADER = {LocatorTypes.TEXT: "Сообщение"}
    COORDINATES_HEADER = {LocatorTypes.TEXT: "Координаты"}
    ENABLE_ANTIFRAUD_TEXT = {LocatorTypes.TEXT: "Включить Антифрод"}
    CONTROL_DAILY_TEXT = {LocatorTypes.TEXT: "Контролировать количество применений в день"}
    CONTROL_WEEKLY_TEXT = {LocatorTypes.TEXT: "Контролировать количество применений в неделю"}
    CONTROL_MONTHLY_TEXT = {LocatorTypes.TEXT: "Контролировать количество применений в месяц"}
    EMAIL_NOTIFICATIONS_ENABLE_TEXT = {LocatorTypes.TEXT: "Получать уведомления на Email"}
    EMAIL_ADDRESSES_TEXT = {LocatorTypes.TEXT: "Адреса эл. почт для оповещений"}
    CUSTOM_SMTP_TEXT = {LocatorTypes.TEXT: "Использовать собственный SMTP-сервер"}
    TELEGRAM_NOTIFICATIONS_ENABLE_TEXT = {LocatorTypes.TEXT: "Получать уведомления в"}
    BOT_REG_LINK_TEXT = {LocatorTypes.TEXT: "Ссылка для регистрации в боте"}
    BOT_RECIPIENTS_TEXT = {LocatorTypes.TEXT: "Получатели, зарегистрированные в боте"}
    FULL_NAME_TEXT = {LocatorTypes.TEXT: "ФИО"}
    PHONE_HEADER = {LocatorTypes.TEXT: "Телефон"}
    REGISTERED_HEADER = {LocatorTypes.TEXT: "Зарегистрирован"}
    EXCLUDED_GROUPS_TEXT = {LocatorTypes.TEXT: "Исключенные группы счетов"}
    EXCLUDED_ACCOUNTS_TEXT = {LocatorTypes.TEXT: "Исключенные счета"}
    CARDS_IDENTIFIERS_TEXT = {LocatorTypes.TEXT: "Идентификаторы: карты"}
    PHONES_IDENTIFIERS_TEXT = {LocatorTypes.TEXT: "Идентификаторы: телефоны"}
    OTHER_IDENTIFIERS_TEXT = {LocatorTypes.TEXT: "Идентификаторы: другие"}
    CHECK_AND_SAVE_ANTIFRAUD_BUTTON = {LocatorTypes.ROLE: RoleTypes.BUTTON, "name": "Проверить и сохранить"}
    PARSING_RESULTS_TEXT = {LocatorTypes.TEXT: "Результаты парсинга"}
    ROW_HEADER = {LocatorTypes.TEXT: "Строка"}
    CARD_HEADER = {LocatorTypes.TEXT: "Карта"}
    FIRST_NAME_HEADER = {LocatorTypes.TEXT: "Имя"}
    LAST_NAME_HEADER = {LocatorTypes.TEXT: "Фамилия"}
    PATRONYMIC_HEADER = {LocatorTypes.TEXT: "Отчество"}
    GENDER_HEADER = {LocatorTypes.TEXT: "Пол"}
    BALANCE_HEADER = {LocatorTypes.TEXT: "Баланс"}
    DISCOUNT_CODE_HEADER = {LocatorTypes.TEXT: "Код скидки"}
    BONUS_TYPE_CODE_HEADER = {LocatorTypes.TEXT: "Код типа бонусов"}
    PHONE1_HEADER = {LocatorTypes.TEXT: "Телефон1"}
    PHONE2_HEADER = {LocatorTypes.TEXT: "Телефон2"}
    EMAIL_HEADER = {LocatorTypes.TEXT: "Почта"}
    BIRTHDAY_HEADER = {LocatorTypes.TEXT: "День рождения"}
    INFO_HEADER = {LocatorTypes.TEXT: "Информация"}
    SCREEN_MESSAGE_HEADER = {LocatorTypes.TEXT: "Сообщение для экрана"}
    PRINT_MESSAGE_HEADER = {LocatorTypes.TEXT: "Сообщение для печати"}
    WALLET_HEADER = {LocatorTypes.TEXT: "Wallet"}
    SEPARATOR_TEXT = {LocatorTypes.TEXT: "Разделитель; точка с запятой"}
    RECOGNIZE_FILE_TEXT = {LocatorTypes.TEXT: "Попытаться распознать файл"}
    IDENTIFIER_HEADER = {LocatorTypes.TEXT: "Идентификатор"}
    SPEND_AMOUNT_HEADER = {LocatorTypes.TEXT: "Сумма потрат (коп.)"}
    SUBSIDIZED_MEALS_REPORT_TEXT = {LocatorTypes.TEXT: "Отчёт \"Питание с дотациями\""}
    DAILY_SUBSIDY_TEXT = {LocatorTypes.TEXT: "Ежедневная дотация"}
    MARK_HEADER = {LocatorTypes.TEXT: "Метка"}
    COUNT_TEXT = {LocatorTypes.TEXT: "Кол-во"}
    ORGANIZATION_DEDUCTION_HEADER = {LocatorTypes.TEXT: "Вычет организация"}
    EMPLOYEE_DEDUCTION_HEADER = {LocatorTypes.TEXT: "Вычет сотрудник"}
    TOTAL_REPORT_TEXT = {LocatorTypes.TEXT: "Отчёт \"Суммовой\""}
    ALL_TAGS_TEXT = {LocatorTypes.TEXT: "Теги: все (15)"}
    ACCOUNT_GROUP_HEADER = {LocatorTypes.TEXT: "Группа счетов"}
    TAGS_TABLE_TEXT = {LocatorTypes.TEXT: "Теги"}
    DISCOUNT_HEADER = {LocatorTypes.TEXT: "Скидка"}
    SPENT_FROM_ACCOUNT_HEADER = {LocatorTypes.TEXT: "Потрачено со счета"}
    ACCRUED_TO_ACCOUNT_HEADER = {LocatorTypes.TEXT: "Начислено на счет"}
    CHECKS_SUM_HEADER = {LocatorTypes.TEXT: "Сумма чеков"}
    REMAINDER_HEADER = {LocatorTypes.TEXT: "Остаток"}
    TRANSACTIONS_REPORT_TEXT = {LocatorTypes.TEXT: "Отчёт \"Транзакции\""}
    DATETIME_HEADER = {LocatorTypes.TEXT: "Дата/Время"}
    IDENTIFIER_TYPE_HEADER = {LocatorTypes.TEXT: "Тип идентификатора"}
    IDENTIFIER_EXACT_TEXT = {LocatorTypes.TEXT: "Идентификатор", "exact": True}
    CASH_REGISTER_HEADER = {LocatorTypes.TEXT: "Касса"}
    CHECK_HEADER = {LocatorTypes.TEXT: "Чек"}
    OPERATION_HEADER = {LocatorTypes.TEXT: "Операция"}
    IDENTIFIERS_REPORT_TEXT = {LocatorTypes.TEXT: "Идентификаторы"}
    SPENDS_BY_DAY_REPORT_TEXT = {LocatorTypes.TEXT: "Отчёт \"Потраты по дням\""}
    CODE_HEADER = {LocatorTypes.TEXT: "Код"}
    TYPE_HEADER = {LocatorTypes.TEXT: "Тип"}
    COUNT_HEADER = {LocatorTypes.TEXT: "Кол-во"}
    BIRTHDAYS_REPORT_TEXT = {LocatorTypes.TEXT: "Отчёт \"Дни рождения\""}
    ADDITIONAL_FIELDS_TEXT = {LocatorTypes.TEXT: "Доп. поля"}
    TODAY_TEXT = {LocatorTypes.TEXT: "Сегодня"}
    TOMORROW_TEXT = {LocatorTypes.TEXT: "Завтра"}
    CURRENT_MONTH_TEXT = {LocatorTypes.TEXT: "Текущий месяц"}
    NEXT_MONTH_TEXT = {LocatorTypes.TEXT: "Следующий месяц"}
    NEXT_10_DAYS_TEXT = {LocatorTypes.TEXT: "Ближайшие 10 дней"}
    NEXT_30_DAYS_TEXT = {LocatorTypes.TEXT: "Ближайшие 30 дней"}
    BIRTH_DATE_HEADER = {LocatorTypes.TEXT: "Дата рождения"}
    AGE_HEADER = {LocatorTypes.TEXT: "Возраст"}
    INACTIVE_ACCOUNTS_REPORT_TEXT = {LocatorTypes.TEXT: "Отчёт \"Бездействующие счета\""}
    LOST_GUESTS_REPORT_TEXT = {LocatorTypes.TEXT: "Отчёт \"Потерянные гости\""}
    CHECK_PERIOD_START_TEXT = {LocatorTypes.TEXT: "Начало периода проверки", "exact": True}
    INACTIVITY_PERIOD_START_TEXT = {LocatorTypes.TEXT: "Начало периода проверки неактивности", "exact": True}
    PERIOD_END_TEXT = {LocatorTypes.TEXT: "Конец периода", "exact": True}
    TOTAL_CHECKS_PERIOD_HEADER = {LocatorTypes.TEXT: "Всего чеков за период"}
    AVG_CHECKS_MONTH_HEADER = {LocatorTypes.TEXT: "В среднем чеков в месяц"}
    AVG_CHECKS_DAY_HEADER = {LocatorTypes.TEXT: "В среднем чеков в день"}
    TOTAL_SPENDS_PERIOD_HEADER = {LocatorTypes.TEXT: "Всего потрат за период"}
    AVG_CHECK_HEADER = {LocatorTypes.TEXT: "Средний чек"}
    LAST_CHECK_DATE_HEADER = {LocatorTypes.TEXT: "Дата последнего чека"}
    ACCOUNT_TURNOVER_REPORT_TEXT = {LocatorTypes.TEXT: "Отчёт \"Оборот по счетам\""}
    START_EXACT_TEXT = {LocatorTypes.TEXT: "Начало", "exact": True}
    END_EXACT_TEXT = {LocatorTypes.TEXT: "Конец", "exact": True}
    BALANCE_END_TEXT = {LocatorTypes.TEXT: "Остаток на конец"}
    BALANCE_START_HEADER = {LocatorTypes.TEXT: "Остаток на начало"}
    GUEST_BASE_GROWTH_REPORT_TEXT = {LocatorTypes.TEXT: "Прирост гостевой базы"}
    GUEST_BASE_DYNAMICS_TEXT = {LocatorTypes.TEXT: "Динамика гостевой базы"}
    REG_SOURCES_DYNAMICS_TEXT = {LocatorTypes.TEXT: "Динамика гостей базы по источникам регистраций (UTM-метки)"}
    DATE_HEADER = {LocatorTypes.TEXT: "Дата"}
    TOTAL_ALL_SOURCES_HEADER = {LocatorTypes.TEXT: "Суммарно по всем источникам"}
    PAGE_TOTAL_TEXT = {LocatorTypes.TEXT: "Итого на странице:"}
    TOTAL_TEXT = {LocatorTypes.TEXT: "Итого:"}
    TOP_GUESTS_REPORT_TEXT = {LocatorTypes.TEXT: "Топ гостей"}
    PHONES_HEADER = {LocatorTypes.TEXT: "Телефоны"}
    CHECKS_COUNT_HEADER = {LocatorTypes.TEXT: "Кол-во чеков"}
    VISITS_COUNT_HEADER = {LocatorTypes.TEXT: "Кол-во посещений"}
    SPENDS_SUM_HEADER = {LocatorTypes.TEXT: "Сумма потрат"}
    DISCOUNTS_SUM_HEADER = {LocatorTypes.TEXT: "Сумма скидок"}
    PRODUCT_COUPONS_TURNOVER_REPORT_TEXT = {LocatorTypes.TEXT: "Оборот товарных купонов"}
    COUPON_HEADER = {LocatorTypes.TEXT: "Купон"}
    START_BALANCE_HEADER = {LocatorTypes.TEXT: "Остаток на начало"}
    ACCRUED_HEADER = {LocatorTypes.TEXT: "Начислено"}
    REDEEMED_HEADER = {LocatorTypes.TEXT: "Погашено"}
    BURNED_BEFORE_REDEMPTION_HEADER = {LocatorTypes.TEXT: "Сгорело до гашения"}
    END_BALANCE_HEADER = {LocatorTypes.TEXT: "Остаток на конец"}
    STAMPS_REPORT_TEXT = {LocatorTypes.TEXT: "Отчёт \"Штампики\""}
    PROMOCODES_REPORT_TEXT = {LocatorTypes.TEXT: "Отчет \"Промокоды\""}
    DASHBOARD_REPORT_TEXT = {LocatorTypes.TEXT: "Дашборд"}
    REFERRAL_PROGRAM_REPORT_TEXT = {LocatorTypes.TEXT: "Реферальная программа"}
    REFERRERS_WITH_REG_TEXT = {LocatorTypes.TEXT: "Гости, по реферальным ссылкам которых есть регистрации"}
    REFERRED_WITH_REG_TEXT = {LocatorTypes.TEXT: "Гости, зарегистрировавшиеся по реферальным ссылка"}
    REFERRED_WITH_PURCHASE_TEXT = {LocatorTypes.TEXT: "Приведённые гости, совершившие хотя бы одну покупку"}
    PROGRAM_EFFECTIVENESS_TEXT = {LocatorTypes.TEXT: "Эффективность программы"}
    REFERRALS_GROWTH_CHART_TEXT = {LocatorTypes.TEXT: "График прироста рефералов"}
    GUEST_ATTRACTION_DYNAMICS_TEXT = {LocatorTypes.TEXT: "Динамика привлечения гостей"}
    ACCOUNTS_EXPORT_REPORT_TEXT = {LocatorTypes.TEXT: "Отчёт \"Выгрузка счетов\""}
    DB_INFO_TEXT = {LocatorTypes.TEXT: "Информация о базе данных"}
    NAME_CELL_TEXT = {LocatorTypes.TEXT: "Имя"}
    CURRENT_VERSION_TEXT = {LocatorTypes.TEXT: "Текущая версия"}
    REQUIRED_VERSION_TEXT = {LocatorTypes.TEXT: "Необходимая версия"}
    DB_CONNECTION_FIELD = {LocatorTypes.ROLE: RoleTypes.TEXTBOX, "name": "Здесь сохранены данные подключения к БД, но спрятаны по соображениям безопасност"}
    CONNECTION_STRING_CREATION_TEXT = {LocatorTypes.TEXT: "Создание строки подключения"}
    DRIVER_FIELD = {LocatorTypes.ROLE: RoleTypes.TEXTBOX, "name": "Драйвер Microsoft ODBC для"}
    SERVER_FIELD = {LocatorTypes.ROLE: RoleTypes.TEXTBOX, "name": "Сервер"}
    DB_USER_FIELD = {LocatorTypes.ROLE: RoleTypes.TEXTBOX, "name": "Имя пользователя"}
    DB_PASSWORD_FIELD = {LocatorTypes.ROLE: RoleTypes.TEXTBOX, "name": "Пароль"}
    CONNECTION_STRING_HEADER = {LocatorTypes.ROLE: RoleTypes.HEADING, "name": "Строка подключения"}
    RKEEPER_CONNECTION_TEXT = {LocatorTypes.TEXT: "Подключение к R_Keeper"}
    MID_REF_SERVER_TEXT = {LocatorTypes.TEXT: "Адрес mid или ref сервера"}
    XML_USER_TEXT = {LocatorTypes.TEXT: "Имя пользователя XML"}
    XML_PASSWORD_TEXT = {LocatorTypes.TEXT: "Пароль пользователя XML"}
    RKEEPER_ADDITIONAL_PARAMS_TEXT = {LocatorTypes.TEXT: "Дополнительные параметы R_Keeper", "exact": True}
    ZERO_DISCOUNT_CODE_TEXT = {LocatorTypes.TEXT: "Код нулевой скидки"}
    FROM_RKEEPER_BUTTON = {LocatorTypes.ROLE: RoleTypes.BUTTON, "name": "Из R_Keeper"}
    SERVER_EXACT_TEXT = {LocatorTypes.TEXT: "Сервер", "exact": True}
    TOKEN_VALIDITY_TEXT = {LocatorTypes.TEXT: "Время действия токенов"}
    LOG_EXACT_TEXT = {LocatorTypes.TEXT: "Лог", "exact": True}
    REQUIRED_FIELDS_TEXT = {LocatorTypes.TEXT: "Обязательные поля"}
    TEMP_IDENTIFIER_TEXT = {LocatorTypes.TEXT: "Временный идентификатор"}
    LOCALIZATION_TEXT = {LocatorTypes.TEXT: "Локализация"}
    DAY_CHANGE_TIME_TEXT = {LocatorTypes.TEXT: "Время смены суток"}
    BIRTHDAY_DISPLAY_TEXT = {LocatorTypes.TEXT: "Отображение дня рождения гостя на кассе"}
    SPECIAL_CASES_SETTINGS_TEXT = {LocatorTypes.TEXT: "Настройки для особых случаев"}
    GENDER_REQUIRED_TEXT = {LocatorTypes.TEXT: "Пол обязателен ? - Да"}
    PHONE_REQUIRED_TEXT = {LocatorTypes.TEXT: "Телефон обязателен ? - Да"}
    TEMP_ID_VALIDITY_TEXT = {LocatorTypes.TEXT: "Время действия временного идентификатора (мин)"}
    TEMP_ID_LENGTH_TEXT = {LocatorTypes.TEXT: "Длина временного идентификатора"}
    LANGUAGE_TEXT = {LocatorTypes.TEXT: "ЯзыкРусский"}
    DAY_CHANGE_TIME_VALUE_TEXT = {LocatorTypes.TEXT: "Время смены суток17:00"}
    SHOW_ON_CASH_TEXT = {LocatorTypes.TEXT: "Показывать на кассе ? - Да"}
    DAYS_BEFORE_TEXT = {LocatorTypes.TEXT: "Дней до"}
    DAYS_AFTER_TEXT = {LocatorTypes.TEXT: "Дней после"}
    CASH_REG_SETTINGS_TEXT = {LocatorTypes.TEXT: "Настройки"}
    TOKEN_TEXT = {LocatorTypes.TEXT: "Токен"}
    CASH_USER_TEXT = {LocatorTypes.TEXT: "Пользователь"}
    CASH_LINK_EXACT_TEXT = {LocatorTypes.TEXT: "Кассовая ссылка", "exact": True}
    OLD_BOT_MIGRATION_TEXT = {LocatorTypes.TEXT: "Перенос данных из старого бота ProBonus"}
    DB_MIGRATION_BUTTON = {LocatorTypes.ROLE: RoleTypes.BUTTON, "name": "Миграция базы данных"}
    SETTINGS_MIGRATION_BUTTON = {LocatorTypes.ROLE: RoleTypes.BUTTON, "name": "Миграция настроек"}
    POLICIES_MIGRATION_BUTTON = {LocatorTypes.ROLE: RoleTypes.BUTTON, "name": "Миграция описания и политик"}
    DESCRIPTION_EXACT_TEXT = {LocatorTypes.TEXT: "Описание", "exact": True}
    PERSONAL_DATA_POLICY_TEXT = {LocatorTypes.TEXT: "Политики обработки перс. данных"}
    SHOW_PERSONAL_DATA_POLICY_TEXT = {LocatorTypes.TEXT: "Показывать политику обработки перс. данных? - Да"}
    PRIVACY_POLICY_EXACT_TEXT = {LocatorTypes.TEXT: "Политика конфиденциальности", "exact": True}
    SHOW_PRIVACY_POLICY_TEXT = {LocatorTypes.TEXT: "Показывать политику конфиденциальности? - Да"}
    AGE_RESTRICTIONS_TEXT = {LocatorTypes.TEXT: "Ограничения по возрасту"}
    AGE_CONFIRMATION_TEXT = {LocatorTypes.TEXT: "Подтверждение возраста? - Нет"}
    AGE_REQUEST_TEXT_MODIFICATION_TEXT = {LocatorTypes.TEXT: "Текст запроса возраста можно изменить в настройках фраз"}
    DATE_START_FIELD = {LocatorTypes.LABEL: "Дата начала", "exact": True}
    SAVE_BUTTON_LOGO = {
        LocatorTypes.LOCATOR: 'button[test-tag="tag-159"] >> nth=0'
    }
    SAVE_BUTTON_BACKGROUND = {
        LocatorTypes.LOCATOR: 'button[test-tag="tag-159"] >> nth=1'
    }
    CANCEL_BUTTON_LOGO = {
        LocatorTypes.LOCATOR: 'button[test-tag="tag-160"] >> nth=0'
    }
    CANCEL_BUTTON_BACKGROUND = {
        LocatorTypes.LOCATOR: 'button[test-tag="tag-160"] >> nth=1'
    }
    TEXT_ACCUMULATION828 = {
    LocatorTypes.LOCATOR: 'input[type="number"][test-tag="tag-828"]'
}
    TEXT_ACCUMULATION829 = {
    LocatorTypes.LOCATOR: 'input[type="number"][test-tag="tag-829"]'
}
    WORK_GRADE =  {
    LocatorTypes.LOCATOR: "//div[contains(@class, 'v-select') and .//label[normalize-space()='Оценка']]//input[@test-tag='tag-630']"
}

#Для WALLET

    CARD_SETTINGS_TEXT = {
        LocatorTypes.LOCATOR: "text='Общие настройки карты'"
    }
    
    TEMPLATE_NAME_EXACT_TEXT = {
        LocatorTypes.LOCATOR: "text='Название макета'"
    }
    
    CARD_DESCRIPTION_TEXT = {
    LocatorTypes.LOCATOR: 'input[type="number"][test-tag="tag-915"]'
}
    
    CARD_NAME_TEXT = {
        LocatorTypes.LOCATOR: "text='Название карты'"
    }
    
    ALLOW_SHARE_TEXT = {
        LocatorTypes.LOCATOR: "text='Разрешить делиться'"
    }
    
    PUSH_APPEARANCE_TEXT = {
        LocatorTypes.LOCATOR: "text='Внешний вид пуша'"
    }
    
    RESTAURANT_NAME_CAPS_TEXT = {
        LocatorTypes.LOCATOR: "text='НАЗВАНИЕ РЕСТОРАНА (В КАПСЕ)'"
    }
    
    FRONT_SIDE_TEXT = {
        LocatorTypes.LOCATOR: "text='Лицевая сторона'"
    }
    
    SHOW_ACCOUNT_LEVEL_TEXT = {
        LocatorTypes.LOCATOR: "text='Показывать уровень счета'"
    }
    
    SHOW_OWNER_DATA_TEXT = {
        LocatorTypes.LOCATOR: "text='Показывать данные владельца'"
    }
    
    SHOW_BALANCE_DATA_TEXT = {
        LocatorTypes.LOCATOR: "text='Показывать данные баланса'"
    }
    
    BACK_SIDE_TEXT = {
        LocatorTypes.LOCATOR: "text='Оборотная сторона'"
    }
    
    BACK_SIDE_TEXT_FIELD = {
        LocatorTypes.LOCATOR: "text='Текст оборотной стороны'"
    }
    
    TEMPLATE_NAME_HEADER = {
        LocatorTypes.LOCATOR: "h2:has-text('Название макета')"
    }
    
    # Поля ввода по ID (они уже были, но добавим для полноты)
    INPUT_540 = {
        LocatorTypes.LOCATOR: "#input-540"
    }
    
    INPUT_545 = {
        LocatorTypes.LOCATOR: "#input-545"
    }
    
    INPUT_550 = {
        LocatorTypes.LOCATOR: "#input-550"
    }



class LocatorTemplates:
    """Шаблоны для создания сложных локаторов"""
    
    @staticmethod
    def cell(name):
        """Создать локатор для ячейки таблицы"""
        return {LocatorTypes.ROLE: RoleTypes.CELL, "name": name}
    
    @staticmethod
    def columnheader(name):
        """Создать локатор для заголовка столбца"""
        return {LocatorTypes.ROLE: RoleTypes.COLUMNHEADER, "name": name}
    
    @staticmethod
    def label_filter(label, text):
        """Создать локатор для фильтрации по метке"""
        return {LocatorTypes.LABEL: label, LocatorTypes.TEXT: text}
    
    @staticmethod
    def css_selector(selector, **kwargs):
        """Создать локатор по CSS селектору"""
        return {LocatorTypes.LOCATOR: selector, **kwargs}
    
    @staticmethod
    def div_with_text(pattern, nth=0):
        """Создать локатор для div с текстом по регулярному выражению"""
        return {LocatorTypes.LOCATOR: "div", "has_text": re.compile(pattern), "nth": nth}
    
    @staticmethod
    def form_with_text(text):
        """Создать локатор для формы с текстом"""
        return {LocatorTypes.ROLE: RoleTypes.FORM, LocatorTypes.TEXT: text}
    
    @staticmethod
    def table_with_text(text):
        """Создать локатор для таблицы с текстом"""
        return {LocatorTypes.ROLE: RoleTypes.TABLE, LocatorTypes.TEXT: text}
    
    @staticmethod
    def main_with_text(text, exact=False):
        """Создать локатор для main с текстом"""
        return {LocatorTypes.ROLE: RoleTypes.MAIN, LocatorTypes.TEXT: text, "exact": exact}