from datetime import datetime

# тестовий список
users = [
    {'name': 'Ivan', 'birthday': '18-05-1990'},
    {'name': 'Bohdan', 'birthday': '17-05-1990'},
    {'name': 'Sviatoslav', 'birthday': '22-05-1990'},
    {'name': 'Halyna', 'birthday': '17-05-1990'},
    {'name': 'Mariya', 'birthday': '22-05-1990'},
    {'name': 'Hanna', 'birthday': '20-05-1990'}]


def get_birthdays_per_week(users: list):
    li_names = []  # для зберігання іменинників
    li_birthday = []  # для зберігання ДН в рядках
    for i in users:
        li_names.append(i['name'])  # наповнюю список іменинниками
        li_birthday.append(i['birthday'])  # наповнюю список ДН в рядках

    today = get_today()  # дізнаюся сьогоднішній день
    rez_dict = {'Monday': [], 'Tuesday': [], 'Wednesday': [],
                'Thursday': [], 'Friday': [], 'Saturday': [], 'Sunday': []}
    # словник для зберігання списків іменинників цього тижня
    for j in range(len(li_birthday)):
        # переводжу день і місяць народження в datetime
        a = datetime.strptime(li_birthday[j], '%d-%m-%Y').date()
        # якщо місяць == нинішньому і день == сьогодні+7 -> додаю в словник
        if today.day <= a.day <= (today.day + 7) and today.month == a.month:
            rez_dict[a.strftime('%A')].append(li_names[j])
    # виведення результату
    rez_li = []
    for key in rez_dict:
        # відсіюю дні коли не треба вітати когось
        if rez_dict[key]:
            temp_str = ''
            # виключення для вихідних
            if key == 'Saturday' or key == 'Sunday':
                temp_str += 'Monday' + ': ' + ', '.join(rez_dict[key])
            else:
                temp_str += key + ': ' + ', '.join(rez_dict[key])
            rez_li.append(temp_str)
    return '\n'.join(rez_li)
    pass


def get_today():
    return datetime.now().date()
    pass


print(get_birthdays_per_week(users))
