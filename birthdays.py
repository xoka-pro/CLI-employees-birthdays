from datetime import datetime, timedelta

employees = [{'name': 'Ivan', 'birthday': '1988-11-10'},
             {'name': 'Vasyl', 'birthday': '1990-11-11'},
             {'name': 'Nik', 'birthday': '1995-11-13'},
             {'name': 'Vlad', 'birthday': '1983-11-05'},
             {'name': 'Alex', 'birthday': '1985-11-06'},
             {'name': 'Anna', 'birthday': '1977-11-08'},
             {'name': 'Olga', 'birthday': '1988-11-09'},
             {'name': 'Vika', 'birthday': '1982-11-20'}, ]


def get_birthdays_per_week(users: list) -> None:
    checked = {'Monday': [], 'Tuesday': [], 'Wednesday': [], 'Thursday': [], 'Friday': []}

    today = datetime.now().date()
    next_monday = (today + timedelta(days=7 - today.weekday()))
    next_friday = (today + timedelta(days=11 - today.weekday()))
    last_saturday = (next_monday - timedelta(days=2))

    for user in users:
        birthday = user['birthday'].split('-')
        user_birthday = datetime(year=today.year, month=int(birthday[1]), day=int(birthday[2])).date()
        if last_saturday <= user_birthday < next_monday:
            checked['Monday'].append(user['name'])
        elif next_monday <= user_birthday <= next_friday:
            checked[user_birthday.strftime('%A')].append(user['name'])
    for day, celebrators in checked.items():
        if not celebrators:
            continue
        else:
            str_names = ', '.join(celebrators)
            print(f'{day}: {str_names}')


get_birthdays_per_week(employees)
