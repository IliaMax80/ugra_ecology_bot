dialogs = {
    'intro': {
        'start': {
            'hello': 'Привет! Ты попал в чат бота АО «Югра-Экология» '
                     'Здесь ты можешь получить информацию о точках раздельного сбора отходов на переработку твоего города и '
                     'узнать как правильно сортировать отходы.',

            'usage_statistic': 'Скибиди доб доб',
            'confirm_button': 'Поехали заполнять!',
            'points_of_city_button': 'Пункты приема',
            'eco_lesson_button': 'Экоурок',
            'recycling_tips_button': 'Справочник отходов',
            'eco_piggy_bank_button': 'ЭКО-копилка',
            'useful_links_button': 'Полезные ссылки'
        },
        'about_info': 'Расскажи о себе:',
        'roles': '  Выберите роль',
        'target': 'Расскажите, какой проект вы хотите сделать',
        'complete': 'Спасибо, теперь вы можете подыскать себе команду или создать новую! Для этого нажмите на /teams',
        'profile_info': 'Вы ранее заполняли:\n\nО Себе: {about}, Роль: {role}\n\nЦель: {target}\n\n'
                        'Если хотите заново заполнить информацию о себе, можете нажать /start'
    },
    'admin': {
        'manage_articles_button': 'Управлять статьями',
        'post_news_button': 'Выложить новость',
        'get_statistic_button': 'Статистика',
        'password': 'Введите пароль администратора'}
}


async def get_point_text(closest_point):
    return f"""{closest_point['title']}
        
{closest_point['description']}

{closest_point['address']}
Номер телефона: {closest_point['phone_number']}

{closest_point['schedule']}

Принимается:
{closest_point['types_of_garbage']}"""


async def get_point_request_text(point):
    return f"""{point.title}

{point.description}

{point.address}

Принимается: {point.types_of_garbage}

Номер телефона: {point.phone_number}

Автор запроса: {point.author}"""
