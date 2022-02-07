import datetime

users = [
    {
        "name": "Bill",
        "birthday": "1998-02-08"
    },
    {
        "name": "Giil",
        "birthday": "1999-02-10"
    },
    {
        "name": "Till",
        "birthday": "2000-02-10"
    }
]

"""Monday: Bill, Jill
Friday: Kim, Jan"""


def get_birthdays(users_list):
    li_days = []
    li_names = []
    for i in users_list:
        current_year = datetime.datetime.today()
        current_year_int = int(current_year.strftime('%Y'))
        rez = i['birthday'].split('-')
        day_at_date = datetime.datetime(
            year=current_year_int, month=int(rez[1]), day=int(rez[2]))
        li_days.append(day_at_date.strftime('%A %d %B'))
        li_names.append(i['name'])
    return li_days, li_names


# rint(get_birthdays(users))


def get_birthdays_per_week():

    # дізнаюся сьогоднішню дату
    today = datetime.datetime.today()

    # створюю список дат наступного тижня
    nextweek_list = []
    for day in range(1, 8):
        a = today + datetime.timedelta(days=day)
        nextweek_list.append(a.strftime('%A %d %B'))

    rez_str = ''
    # список днів народжень
    birthdays_list = get_birthdays(users)[0]
    # список імен з індексами що == дням народження
    names_list = get_birthdays(users)[1]
    # словник ДН: Ім'я
    rez_di = dict(zip(birthdays_list, names_list))
    for day in nextweek_list:
        if day in birthdays_list:
            # день для привітання
            temp_day = day.split()[0]
            # день для привітання + імена іменинників
            rez_str += temp_day + ': '
            for key, value in rez_di.items():
                if key == day:
                    rez_str += value + ', '
            rez_str += '\n'

    return rez_str
    pass


print(get_birthdays_per_week())
