// Internationalization (i18n) support

const translations = {
    ru: {
        // Navigation
        app_title: 'Трекер Расходов',
        nav_dashboard: 'Главная',
        nav_transactions: 'Транзакции',
        nav_recurring: 'Регулярные',
        nav_budgets: 'Бюджеты',
        nav_goals: 'Цели',
        nav_profile: 'Профиль',
        nav_logout: 'Выход',

        // Landing page
        hero_title: '📊 Трекер Расходов и Доходов',
        hero_subtitle: 'Контролируйте свои финансы легко и удобно',
        feature_stats_title: 'Статистика',
        feature_stats_desc: 'Полная аналитика ваших расходов и доходов с красивыми графиками',
        feature_transactions_title: 'Транзакции',
        feature_transactions_desc: 'Отслеживайте все ваши финансовые операции в одном месте',
        feature_budgets_title: 'Бюджеты',
        feature_budgets_desc: 'Устанавливайте лимиты расходов и следите за их соблюдением',
        feature_goals_title: 'Цели',
        feature_goals_desc: 'Создавайте финансовые цели и достигайте их',

        // Common
        save: 'Сохранить',
        save_btn: 'Сохранить',
        delete: 'Удалить',
        cancel: 'Отмена',
        cancel_btn: 'Отмена',
        close: 'Закрыть',
        add: 'Добавить',
        edit: 'Редактировать',
        add_btn: '+ Добавить',
        actions: 'Действия',
        back_btn: 'Назад',

        // Transactions
        transactions: 'Транзакции',
        add_transaction: 'Добавить транзакцию',
        transaction_added: 'Транзакция добавлена',
        error_adding_transaction: 'Ошибка при добавлении транзакции',
        confirm_delete_transaction: 'Вы уверены, что хотите удалить эту транзакцию?',
        no_transactions: 'Нет транзакций',
        error_loading: 'Ошибка загрузки',
        type: 'Тип',
        category: 'Категория',
        amount: 'Сумма',
        description: 'Описание',
        date: 'Дата',
        income: 'Доход',
        expense: 'Расход',
        income_label: 'Доход',
        expense_label: 'Расход',

        // Filters
        filters: 'Фильтры',
        date_range: 'Период',
        filter_all: 'Все время',
        filter_7days: 'Последние 7 дней',
        filter_30days: 'Последние 30 дней',
        filter_90days: 'Последние 90 дней',
        filter_year: 'Последний год',
        filter_custom: 'Произвольный период',
        start_date: 'Начало',
        end_date: 'Конец',

        // Export
        export_csv: 'CSV',
        export_pdf: 'PDF',

        // Profile
        profile: 'Профиль',
        profile_settings: 'Настройки профиля',
        profile_updated: 'Профиль обновлён',
        email: 'Email',
        first_name: 'Имя',
        last_name: 'Фамилия',
        currency: 'Валюта',
        currency_usd: 'Доллар',
        currency_eur: 'Евро',
        currency_usd_full: '$ Доллар',
        currency_eur_full: '€ Евро',
        theme: 'Тема',
        light: 'Светлая',
        dark: 'Тёмная',

        // Password
        change_password: 'Смена пароля',
        change_password_btn: 'Изменить пароль',
        current_password: 'Текущий пароль',
        new_password: 'Новый пароль',
        confirm_new_password: 'Повтор пароля',
        password_changed: 'Пароль изменён',
        error_changing_password: 'Ошибка при изменении пароля',
        passwords_dont_match: 'Пароли не совпадают',
        password_min_length: 'Минимальная длина пароля - 8 символов',

        // Categories
        manage_categories: 'Управление категориями',
        category_name: 'Название категории',
        category_type: 'Тип',
        category_icon: 'Выберите иконку',
        add_category: 'Добавить категорию',
        your_categories: 'Ваши категории',
        no_custom_categories: 'У вас пока нет своих категорий',
        no_categories: 'Нет категорий',
        please_select_icon: 'Пожалуйста, выберите иконку',
        category_added: 'Категория добавлена',
        error_adding_category: 'Ошибка при добавлении категории',
        confirm_delete_category: 'Вы уверены, что хотите удалить эту категорию?',
        category_deleted: 'Категория удалена',
        error_deleting_category: 'Ошибка при удалении категории',

        // Dashboard
        dashboard: 'Главная панель',
        income_month: 'Доходы за месяц',
        expense_month: 'Расходы за месяц',
        balance: 'Баланс',
        expense_by_category: 'Расходы по категориям',
        income_expense_trend: 'Тренд доходов и расходов',
        recent_transactions: 'Последние транзакции',
        loading: 'Загрузка...',
        error_loading_data: 'Ошибка загрузки данных',
        no_data: 'Нет данных',

        // Budgets
        budgets: 'Бюджеты',
        add_budget: 'Добавить бюджет',
        budget_name: 'Название бюджета',
        budget_amount: 'Сумма бюджета',
        period: 'Период',
        monthly: 'Ежемесячно',
        no_budgets: 'Нет бюджетов',
        budget_added: 'Бюджет добавлен',
        error_adding_budget: 'Ошибка при добавлении бюджета',
        confirm_delete_budget: 'Вы уверены, что хотите удалить этот бюджет?',
        budget_deleted: 'Бюджет удалён',
        error_deleting_budget: 'Ошибка при удалении бюджета',

        // Goals
        goals: 'Цели',
        add_goal: 'Добавить цель',
        goal_name: 'Название цели',
        target_amount: 'Целевая сумма',
        current_amount: 'Текущая сумма',
        deadline: 'Срок',
        no_goals: 'Нет целей',
        goal_added: 'Цель добавлена',
        error_adding_goal: 'Ошибка при добавлении цели',
        confirm_delete_goal: 'Вы уверены, что хотите удалить эту цель?',
        goal_deleted: 'Цель удалена',
        error_deleting_goal: 'Ошибка при удалении цели',
        contribute: 'Пополнить',
        contribution_amount: 'Сумма пополнения',

        // Recurring
        recurring: 'Регулярные транзакции',
        add_recurring: 'Добавить регулярную',
        add_recurring_btn: '+ Добавить регулярный платёж',
        frequency: 'Частота',
        interval: 'Интервал',
        interval_help: 'Каждые X дней/недель/месяцев/лет',
        daily: 'Ежедневно',
        weekly: 'Еженедельно',
        biweekly: 'Раз в 2 недели',
        biweekly_alt: 'Каждые 2 недели',
        freq_daily: 'Ежедневно',
        freq_weekly: 'Еженедельно',
        freq_monthly: 'Ежемесячно',
        freq_yearly: 'Ежегодно',
        start_date: 'Дата начала',
        end_date: 'Дата окончания',
        active: 'Активна',
        inactive: 'Неактивна',
        status: 'Статус',
        no_recurring: 'Нет регулярных транзакций',
        recurring_added: 'Регулярная транзакция добавлена',
        error_adding_recurring: 'Ошибка при добавлении регулярной транзакции',
        confirm_delete_recurring: 'Вы уверены, что хотите удалить эту регулярную транзакцию?',
        recurring_deleted: 'Регулярная транзакция удалена',
        error_deleting_recurring: 'Ошибка при удалении регулярной транзакции',

        // Auth pages
        login_btn: 'Войти',
        register_btn: 'Зарегистрироваться',
        register: 'Регистрация',
        have_account: 'Уже есть аккаунт?',
        no_account: 'Нет аккаунта?',
        password: 'Пароль',
        password_confirm: 'Подтверждение пароля',
        back_to_login: 'Вернуться к входу',
        forgot_password: 'Забыли пароль?',

        // Password Reset
        password_reset: 'Восстановление пароля',
        password_reset_title: 'Восстановление пароля',
        reset_password_btn: 'Сбросить пароль',
        choose_reset_method: 'Выберите способ восстановления',
        reset_with_admin: 'Через код администратора',
        reset_with_code: 'Через временный код',
        reset_with_security: 'Через секретный вопрос',
        contact_admin_btn: 'Связаться с администратором',
        request_code_btn: 'Запросить код',
        admin_info: 'Восстановление через администратора',
        admin_info_text: 'Администратор может предоставить вам код для сброса пароля',
        admin_code_label: 'Код от администратора',
        admin_code_hint: 'Введите код, полученный от администратора',
        admin_code_info: 'Информация',
        admin_code_info_text: 'Свяжитесь с администратором для получения кода восстановления',
        code_info: 'Временный код',
        code_info_text: 'Код отправлен на вашу почту',
        temp_code_label: 'Временный код',
        temp_code_hint: 'Введите код из письма',
        new_password_label: 'Новый пароль',
        confirm_password_label: 'Подтвердите пароль',
        security_recovery: 'Восстановление через секретный вопрос',
        your_security_question: 'Ваш секретный вопрос',
        security_question: 'Секретный вопрос',
        security_question_hint: 'Выберите секретный вопрос',
        security_answer: 'Ответ на вопрос',
        security_answer_label: 'Ответ',
        security_answer_hint: 'Введите ответ на секретный вопрос',
        security_note: 'Примечание',
        security_note_text: 'Запомните ответ - он потребуется для восстановления пароля',

        // Password reset messages
        code_sent_success: 'Код успешно отправлен на вашу почту',
        code_request_error: 'Ошибка при отправке кода',
        error_connection: 'Ошибка подключения к серверу',
        passwords_mismatch: 'Пароли не совпадают',
        password_reset_success: 'Пароль успешно изменён! Теперь вы можете войти с новым паролем.',
        reset_error: 'Ошибка при сбросе пароля',
        admin_request_sent: 'Запрос отправлен администратору',
        admin_request_email: 'Ваш email',
        admin_request_instructions: 'Администратор свяжется с вами и предоставит код для сброса пароля',

        // Password reset methods
        method_security_question: 'Секретный вопрос',
        method_security_desc: 'Ответьте на секретный вопрос для восстановления доступа',
        method_temp_code: 'Временный код',
        method_temp_code_desc: 'Получите временный код для сброса пароля',
        method_admin_support: 'Связаться с поддержкой',
        method_admin_support_desc: 'Обратитесь к администратору для помощи в восстановлении',

        // Placeholders
        email_placeholder: 'Введите ваш email',
        password_placeholder: 'Введите ваш пароль',
        first_name_placeholder: 'Введите ваше имя',
        last_name_placeholder: 'Введите вашу фамилию',
        security_answer_placeholder: 'Введите ответ на секретный вопрос',
        new_password_placeholder: 'Минимум 8 символов',
        confirm_password_placeholder: 'Повторите новый пароль',
        security_question_placeholder: 'Например: Кличка первого питомца?',

        // Recurring specific
        recurring_page_title: 'Регулярные платежи',
        end_date_help: 'Оставьте пустым для бессрочного',

        // Budgets specific
        create_budget: 'Создать бюджет',

        // Goals specific
        create_goal: 'Создать цель',
    },
    en: {
        // Navigation
        app_title: 'Expense Tracker',
        nav_dashboard: 'Dashboard',
        nav_transactions: 'Transactions',
        nav_recurring: 'Recurring',
        nav_budgets: 'Budgets',
        nav_goals: 'Goals',
        nav_profile: 'Profile',
        nav_logout: 'Logout',

        // Landing page
        hero_title: '📊 Expense and Income Tracker',
        hero_subtitle: 'Control your finances easily and conveniently',
        feature_stats_title: 'Statistics',
        feature_stats_desc: 'Complete analytics of your expenses and income with beautiful charts',
        feature_transactions_title: 'Transactions',
        feature_transactions_desc: 'Track all your financial operations in one place',
        feature_budgets_title: 'Budgets',
        feature_budgets_desc: 'Set spending limits and monitor compliance',
        feature_goals_title: 'Goals',
        feature_goals_desc: 'Create financial goals and achieve them',

        // Common
        save: 'Save',
        save_btn: 'Save',
        delete: 'Delete',
        cancel: 'Cancel',
        cancel_btn: 'Cancel',
        close: 'Close',
        add: 'Add',
        edit: 'Edit',
        add_btn: '+ Add',
        actions: 'Actions',
        back_btn: 'Back',

        // Transactions
        transactions: 'Transactions',
        add_transaction: 'Add Transaction',
        transaction_added: 'Transaction added',
        error_adding_transaction: 'Error adding transaction',
        confirm_delete_transaction: 'Are you sure you want to delete this transaction?',
        no_transactions: 'No transactions',
        error_loading: 'Error loading',
        type: 'Type',
        category: 'Category',
        amount: 'Amount',
        description: 'Description',
        date: 'Date',
        income: 'Income',
        expense: 'Expense',
        income_label: 'Income',
        expense_label: 'Expense',

        // Filters
        filters: 'Filters',
        date_range: 'Date Range',
        filter_all: 'All Time',
        filter_7days: 'Last 7 Days',
        filter_30days: 'Last 30 Days',
        filter_90days: 'Last 90 Days',
        filter_year: 'Last Year',
        filter_custom: 'Custom Range',
        start_date: 'Start',
        end_date: 'End',

        // Export
        export_csv: 'CSV',
        export_pdf: 'PDF',

        // Profile
        profile: 'Profile',
        profile_settings: 'Profile Settings',
        profile_updated: 'Profile updated',
        email: 'Email',
        first_name: 'First Name',
        last_name: 'Last Name',
        currency: 'Currency',
        currency_usd: 'Dollar',
        currency_eur: 'Euro',
        currency_usd_full: '$ Dollar',
        currency_eur_full: '€ Euro',
        theme: 'Theme',
        light: 'Light',
        dark: 'Dark',

        // Password
        change_password: 'Change Password',
        change_password_btn: 'Change Password',
        current_password: 'Current Password',
        new_password: 'New Password',
        confirm_new_password: 'Confirm Password',
        password_changed: 'Password changed',
        error_changing_password: 'Error changing password',
        passwords_dont_match: 'Passwords do not match',
        password_min_length: 'Minimum password length is 8 characters',

        // Categories
        manage_categories: 'Manage Categories',
        category_name: 'Category Name',
        category_type: 'Type',
        category_icon: 'Select Icon',
        add_category: 'Add Category',
        your_categories: 'Your Categories',
        no_custom_categories: 'You have no custom categories yet',
        no_categories: 'No categories',
        please_select_icon: 'Please select an icon',
        category_added: 'Category added',
        error_adding_category: 'Error adding category',
        confirm_delete_category: 'Are you sure you want to delete this category?',
        category_deleted: 'Category deleted',
        error_deleting_category: 'Error deleting category',

        // Dashboard
        dashboard: 'Dashboard',
        income_month: 'Income this month',
        expense_month: 'Expenses this month',
        balance: 'Balance',
        expense_by_category: 'Expenses by Category',
        income_expense_trend: 'Income & Expense Trend',
        recent_transactions: 'Recent Transactions',
        loading: 'Loading...',
        error_loading_data: 'Error loading data',
        no_data: 'No data',

        // Budgets
        budgets: 'Budgets',
        add_budget: 'Add Budget',
        budget_name: 'Budget Name',
        budget_amount: 'Budget Amount',
        period: 'Period',
        monthly: 'Monthly',
        no_budgets: 'No budgets',
        budget_added: 'Budget added',
        error_adding_budget: 'Error adding budget',
        confirm_delete_budget: 'Are you sure you want to delete this budget?',
        budget_deleted: 'Budget deleted',
        error_deleting_budget: 'Error deleting budget',

        // Goals
        goals: 'Goals',
        add_goal: 'Add Goal',
        goal_name: 'Goal Name',
        target_amount: 'Target Amount',
        current_amount: 'Current Amount',
        deadline: 'Deadline',
        no_goals: 'No goals',
        goal_added: 'Goal added',
        error_adding_goal: 'Error adding goal',
        confirm_delete_goal: 'Are you sure you want to delete this goal?',
        goal_deleted: 'Goal deleted',
        error_deleting_goal: 'Error deleting goal',
        contribute: 'Contribute',
        contribution_amount: 'Contribution Amount',

        // Recurring
        recurring: 'Recurring Transactions',
        add_recurring: 'Add Recurring',
        add_recurring_btn: '+ Add Recurring Payment',
        frequency: 'Frequency',
        interval: 'Interval',
        interval_help: 'Every X days/weeks/months/years',
        daily: 'Daily',
        weekly: 'Weekly',
        biweekly: 'Bi-weekly',
        biweekly_alt: 'Every 2 weeks',
        freq_daily: 'Daily',
        freq_weekly: 'Weekly',
        freq_monthly: 'Monthly',
        freq_yearly: 'Yearly',
        start_date: 'Start Date',
        end_date: 'End Date',
        active: 'Active',
        inactive: 'Inactive',
        status: 'Status',
        no_recurring: 'No recurring transactions',
        recurring_added: 'Recurring transaction added',
        error_adding_recurring: 'Error adding recurring transaction',
        confirm_delete_recurring: 'Are you sure you want to delete this recurring transaction?',
        recurring_deleted: 'Recurring transaction deleted',
        error_deleting_recurring: 'Error deleting recurring transaction',

        // Auth pages
        login_btn: 'Login',
        register_btn: 'Register',
        register: 'Registration',
        have_account: 'Already have an account?',
        no_account: 'No account?',
        password: 'Password',
        password_confirm: 'Confirm Password',
        back_to_login: 'Back to Login',
        forgot_password: 'Forgot password?',

        // Password Reset
        password_reset: 'Password Recovery',
        password_reset_title: 'Password Recovery',
        reset_password_btn: 'Reset Password',
        choose_reset_method: 'Choose recovery method',
        reset_with_admin: 'Via admin code',
        reset_with_code: 'Via temporary code',
        reset_with_security: 'Via security question',
        contact_admin_btn: 'Contact Administrator',
        request_code_btn: 'Request Code',
        admin_info: 'Recovery via Administrator',
        admin_info_text: 'Administrator can provide you with a password reset code',
        admin_code_label: 'Admin Code',
        admin_code_hint: 'Enter code received from administrator',
        admin_code_info: 'Information',
        admin_code_info_text: 'Contact administrator to get recovery code',
        code_info: 'Temporary Code',
        code_info_text: 'Code sent to your email',
        temp_code_label: 'Temporary Code',
        temp_code_hint: 'Enter code from email',
        new_password_label: 'New Password',
        confirm_password_label: 'Confirm Password',
        security_recovery: 'Recovery via Security Question',
        your_security_question: 'Your Security Question',
        security_question: 'Security Question',
        security_question_hint: 'Choose security question',
        security_answer: 'Answer',
        security_answer_label: 'Answer',
        security_answer_hint: 'Enter answer to security question',
        security_note: 'Note',
        security_note_text: 'Remember the answer - you will need it for password recovery',

        // Password reset messages
        code_sent_success: 'Code successfully sent to your email',
        code_request_error: 'Error sending code',
        error_connection: 'Server connection error',
        passwords_mismatch: 'Passwords do not match',
        password_reset_success: 'Password successfully changed! You can now login with your new password.',
        reset_error: 'Error resetting password',
        admin_request_sent: 'Request sent to administrator',
        admin_request_email: 'Your email',
        admin_request_instructions: 'Administrator will contact you and provide a password reset code',

        // Password reset methods
        method_security_question: 'Security Question',
        method_security_desc: 'Answer your security question to recover access',
        method_temp_code: 'Temporary Code',
        method_temp_code_desc: 'Get a temporary code to reset your password',
        method_admin_support: 'Contact Support',
        method_admin_support_desc: 'Contact administrator for help with recovery',

        // Placeholders
        email_placeholder: 'Enter your email',
        password_placeholder: 'Enter your password',
        first_name_placeholder: 'Enter your first name',
        last_name_placeholder: 'Enter your last name',
        security_answer_placeholder: 'Enter answer to security question',
        new_password_placeholder: 'Minimum 8 characters',
        confirm_password_placeholder: 'Repeat new password',
        security_question_placeholder: 'For example: First pet\'s name?',

        // Recurring specific
        recurring_page_title: 'Recurring Payments',
        end_date_help: 'Leave empty for unlimited',

        // Budgets specific
        create_budget: 'Create Budget',

        // Goals specific
        create_goal: 'Create Goal',
    },
    lv: {
        // Navigation
        app_title: 'Izdevumu Izsekotājs',
        nav_dashboard: 'Galvenā',
        nav_transactions: 'Transakcijas',
        nav_recurring: 'Regulārās',
        nav_budgets: 'Budžeti',
        nav_goals: 'Mērķi',
        nav_profile: 'Profils',
        nav_logout: 'Iziet',

        // Landing page
        hero_title: '📊 Izdevumu un ienākumu izsekotājs',
        hero_subtitle: 'Kontrolējiet savas finanses viegli un ērti',
        feature_stats_title: 'Statistika',
        feature_stats_desc: 'Pilnīga jūsu izdevumu un ienākumu analītika ar skaistām diagrammām',
        feature_transactions_title: 'Transakcijas',
        feature_transactions_desc: 'Izsekojiet visas savas finanšu operācijas vienā vietā',
        feature_budgets_title: 'Budžeti',
        feature_budgets_desc: 'Iestatiet izdevumu limitus un sekojiet to ievērošanai',
        feature_goals_title: 'Mērķi',
        feature_goals_desc: 'Izveidojiet finanšu mērķus un sasniedziet tos',

        // Common
        save: 'Saglabāt',
        save_btn: 'Saglabāt',
        delete: 'Dzēst',
        cancel: 'Atcelt',
        cancel_btn: 'Atcelt',
        close: 'Aizvērt',
        add: 'Pievienot',
        edit: 'Rediģēt',
        add_btn: '+ Pievienot',
        actions: 'Darbības',
        back_btn: 'Atpakaļ',

        // Transactions
        transactions: 'Transakcijas',
        add_transaction: 'Pievienot transakciju',
        transaction_added: 'Transakcija pievienota',
        error_adding_transaction: 'Kļūda pievienojot transakciju',
        confirm_delete_transaction: 'Vai tiešām vēlaties dzēst šo transakciju?',
        no_transactions: 'Nav transakciju',
        error_loading: 'Ielādes kļūda',
        type: 'Tips',
        category: 'Kategorija',
        amount: 'Summa',
        description: 'Apraksts',
        date: 'Datums',
        income: 'Ienākumi',
        expense: 'Izdevumi',
        income_label: 'Ienākumi',
        expense_label: 'Izdevumi',

        // Filters
        filters: 'Filtri',
        date_range: 'Periods',
        filter_all: 'Viss laiks',
        filter_7days: 'Pēdējās 7 dienas',
        filter_30days: 'Pēdējās 30 dienas',
        filter_90days: 'Pēdējās 90 dienas',
        filter_year: 'Pēdējais gads',
        filter_custom: 'Pielāgots periods',
        start_date: 'Sākums',
        end_date: 'Beigas',

        // Export
        export_csv: 'CSV',
        export_pdf: 'PDF',

        // Profile
        profile: 'Profils',
        profile_settings: 'Profila iestatījumi',
        profile_updated: 'Profils atjaunināts',
        email: 'E-pasts',
        first_name: 'Vārds',
        last_name: 'Uzvārds',
        currency: 'Valūta',
        currency_usd: 'Dolārs',
        currency_eur: 'Eiro',
        currency_usd_full: '$ Dolārs',
        currency_eur_full: '€ Eiro',
        theme: 'Tēma',
        light: 'Gaiša',
        dark: 'Tumša',

        // Password
        change_password: 'Mainīt paroli',
        change_password_btn: 'Mainīt paroli',
        current_password: 'Pašreizējā parole',
        new_password: 'Jaunā parole',
        confirm_new_password: 'Apstiprināt paroli',
        password_changed: 'Parole nomainīta',
        error_changing_password: 'Kļūda mainoties parolei',
        passwords_dont_match: 'Paroles nesakrīt',
        password_min_length: 'Minimālais paroles garums ir 8 simboli',

        // Categories
        manage_categories: 'Pārvaldīt kategorijas',
        category_name: 'Kategorijas nosaukums',
        category_type: 'Tips',
        category_icon: 'Izvēlieties ikonu',
        add_category: 'Pievienot kategoriju',
        your_categories: 'Jūsu kategorijas',
        no_custom_categories: 'Jums vēl nav pielāgotu kategoriju',
        no_categories: 'Nav kategoriju',
        please_select_icon: 'Lūdzu, izvēlieties ikonu',
        category_added: 'Kategorija pievienota',
        error_adding_category: 'Kļūda pievienojot kategoriju',
        confirm_delete_category: 'Vai tiešām vēlaties dzēst šo kategoriju?',
        category_deleted: 'Kategorija dzēsta',
        error_deleting_category: 'Kļūda dzēšot kategoriju',

        // Dashboard
        dashboard: 'Galvenā panelis',
        income_month: 'Ienākumi šajā mēnesī',
        expense_month: 'Izdevumi šajā mēnesī',
        balance: 'Bilance',
        expense_by_category: 'Izdevumi pēc kategorijām',
        income_expense_trend: 'Ienākumu un izdevumu tendence',
        recent_transactions: 'Pēdējās transakcijas',
        loading: 'Ielādē...',
        error_loading_data: 'Kļūda ielādējot datus',
        no_data: 'Nav datu',

        // Budgets
        budgets: 'Budžeti',
        add_budget: 'Pievienot budžetu',
        budget_name: 'Budžeta nosaukums',
        budget_amount: 'Budžeta summa',
        period: 'Periods',
        monthly: 'Mēneša',
        no_budgets: 'Nav budžetu',
        budget_added: 'Budžets pievienots',
        error_adding_budget: 'Kļūda pievienojot budžetu',
        confirm_delete_budget: 'Vai tiešām vēlaties dzēst šo budžetu?',
        budget_deleted: 'Budžets dzēsts',
        error_deleting_budget: 'Kļūda dzēšot budžetu',

        // Goals
        goals: 'Mērķi',
        add_goal: 'Pievienot mērķi',
        goal_name: 'Mērķa nosaukums',
        target_amount: 'Mērķa summa',
        current_amount: 'Pašreizējā summa',
        deadline: 'Termiņš',
        no_goals: 'Nav mērķu',
        goal_added: 'Mērķis pievienots',
        error_adding_goal: 'Kļūda pievienojot mērķi',
        confirm_delete_goal: 'Vai tiešām vēlaties dzēst šo mērķi?',
        goal_deleted: 'Mērķis dzēsts',
        error_deleting_goal: 'Kļūda dzēšot mērķi',
        contribute: 'Iemaksāt',
        contribution_amount: 'Iemaksas summa',

        // Recurring
        recurring: 'Regulārās transakcijas',
        add_recurring: 'Pievienot regulāru',
        add_recurring_btn: '+ Pievienot regulāro maksājumu',
        frequency: 'Biežums',
        interval: 'Intervāls',
        interval_help: 'Katras X dienas/nedēļas/mēneši/gadi',
        daily: 'Katru dienu',
        weekly: 'Katru nedēļu',
        biweekly: 'Reizi 2 nedēļās',
        biweekly_alt: 'Katras 2 nedēļas',
        freq_daily: 'Katru dienu',
        freq_weekly: 'Katru nedēļu',
        freq_monthly: 'Katru mēnesi',
        freq_yearly: 'Katru gadu',
        start_date: 'Sākuma datums',
        end_date: 'Beigu datums',
        active: 'Aktīva',
        inactive: 'Neaktīva',
        status: 'Statuss',
        no_recurring: 'Nav regulāru transakciju',
        recurring_added: 'Regulārā transakcija pievienota',
        error_adding_recurring: 'Kļūda pievienojot regulāru transakciju',
        confirm_delete_recurring: 'Vai tiešām vēlaties dzēst šo regulāro transakciju?',
        recurring_deleted: 'Regulārā transakcija dzēsta',
        error_deleting_recurring: 'Kļūda dzēšot regulāro transakciju',

        // Auth pages
        login_btn: 'Pieslēgties',
        register_btn: 'Reģistrēties',
        register: 'Reģistrācija',
        have_account: 'Jau ir konts?',
        no_account: 'Nav konta?',
        password: 'Parole',
        password_confirm: 'Apstipriniet paroli',
        back_to_login: 'Atpakaļ uz pieslēgšanos',
        forgot_password: 'Aizmirsāt paroli?',

        // Password Reset
        password_reset: 'Paroles atjaunošana',
        password_reset_title: 'Paroles atjaunošana',
        reset_password_btn: 'Atiestatīt paroli',
        choose_reset_method: 'Izvēlieties atjaunošanas metodi',
        reset_with_admin: 'Ar administratora kodu',
        reset_with_code: 'Ar pagaidu kodu',
        reset_with_security: 'Ar drošības jautājumu',
        contact_admin_btn: 'Sazināties ar administratoru',
        request_code_btn: 'Pieprasīt kodu',
        admin_info: 'Atjaunošana caur administratoru',
        admin_info_text: 'Administrators var sniegt jums paroles atiestatīšanas kodu',
        admin_code_label: 'Administratora kods',
        admin_code_hint: 'Ievadiet no administratora saņemto kodu',
        admin_code_info: 'Informācija',
        admin_code_info_text: 'Sazinieties ar administratoru, lai saņemtu atjaunošanas kodu',
        code_info: 'Pagaidu kods',
        code_info_text: 'Kods nosūtīts uz jūsu e-pastu',
        temp_code_label: 'Pagaidu kods',
        temp_code_hint: 'Ievadiet kodu no e-pasta',
        new_password_label: 'Jaunā parole',
        confirm_password_label: 'Apstipriniet paroli',
        security_recovery: 'Atjaunošana caur drošības jautājumu',
        your_security_question: 'Jūsu drošības jautājums',
        security_question: 'Drošības jautājums',
        security_question_hint: 'Izvēlieties drošības jautājumu',
        security_answer: 'Atbilde',
        security_answer_label: 'Atbilde',
        security_answer_hint: 'Ievadiet atbildi uz drošības jautājumu',
        security_note: 'Piezīme',
        security_note_text: 'Atcerieties atbildi - tā būs nepieciešama paroles atjaunošanai',

        // Password reset messages
        code_sent_success: 'Kods veiksmīgi nosūtīts uz jūsu e-pastu',
        code_request_error: 'Kļūda, nosūtot kodu',
        error_connection: 'Servera savienojuma kļūda',
        passwords_mismatch: 'Paroles nesakrīt',
        password_reset_success: 'Parole veiksmīgi nomainīta! Tagad varat ielogoties ar jauno paroli.',
        reset_error: 'Kļūda, atiestatot paroli',
        admin_request_sent: 'Pieprasījums nosūtīts administratoram',
        admin_request_email: 'Jūsu e-pasts',
        admin_request_instructions: 'Administrators ar jums sazināsies un sniegs paroles atiestatīšanas kodu',

        // Password reset methods
        method_security_question: 'Drošības jautājums',
        method_security_desc: 'Atbildiet uz drošības jautājumu, lai atgūtu piekļuvi',
        method_temp_code: 'Pagaidu kods',
        method_temp_code_desc: 'Saņemiet pagaidu kodu paroles atiestatīšanai',
        method_admin_support: 'Sazināties ar atbalstu',
        method_admin_support_desc: 'Sazinieties ar administratoru palīdzībai',

        // Placeholders
        email_placeholder: 'Ievadiet savu e-pastu',
        password_placeholder: 'Ievadiet savu paroli',
        first_name_placeholder: 'Ievadiet savu vārdu',
        last_name_placeholder: 'Ievadiet savu uzvārdu',
        security_answer_placeholder: 'Ievadiet atbildi uz drošības jautājumu',
        new_password_placeholder: 'Minimums 8 rakstzīmes',
        confirm_password_placeholder: 'Atkārtojiet jauno paroli',
        security_question_placeholder: 'Piemēram: Pirmā mājdzīvnieka vārds?',

        // Recurring specific
        recurring_page_title: 'Regulārie maksājumi',
        end_date_help: 'Atstājiet tukšu beztermiņa',

        // Budgets specific
        create_budget: 'Izveidot budžetu',

        // Goals specific
        create_goal: 'Izveidot mērķi',
    }
};

// Get current language from localStorage or default to 'ru'
function getCurrentLanguage() {
    return localStorage.getItem('language') || 'ru';
}

// Set current language
function setLanguage(lang) {
    if (translations[lang]) {
        localStorage.setItem('language', lang);
        updatePageTranslations();
        // Trigger language change event
        document.dispatchEvent(new CustomEvent('languageChanged', { detail: { lang } }));
    }
}

// Translate function
function t(key) {
    const lang = getCurrentLanguage();
    return translations[lang]?.[key] || translations['ru']?.[key] || key;
}

// Get category name based on current language
function getCategoryName(category) {
    const lang = getCurrentLanguage();
    if (category.name_translations && category.name_translations[lang]) {
        return category.name_translations[lang];
    }
    return category.name || category.name_en || category.name_ru || 'Unknown';
}

// Update all elements with data-i18n attribute
function updatePageTranslations() {
    const lang = getCurrentLanguage();

    // Handle data-i18n for text content or placeholder
    document.querySelectorAll('[data-i18n]').forEach(element => {
        const key = element.getAttribute('data-i18n');
        const translation = translations[lang]?.[key] || translations['ru']?.[key] || key;

        // Update text content or placeholder depending on element type
        if (element.tagName === 'INPUT' || element.tagName === 'TEXTAREA') {
            element.placeholder = translation;
        } else {
            element.textContent = translation;
        }
    });

    // Handle data-i18n-placeholder for placeholder-only translations
    document.querySelectorAll('[data-i18n-placeholder]').forEach(element => {
        const key = element.getAttribute('data-i18n-placeholder');
        const translation = translations[lang]?.[key] || translations['ru']?.[key] || key;
        element.placeholder = translation;
    });
}

// Initialize language selector
document.addEventListener('DOMContentLoaded', function() {
    const languageSelector = document.getElementById('language-selector');
    if (languageSelector) {
        // Set current language
        languageSelector.value = getCurrentLanguage();

        // Add change event listener
        languageSelector.addEventListener('change', function(e) {
            setLanguage(e.target.value);
        });
    }

    // Apply translations on page load
    updatePageTranslations();
});
