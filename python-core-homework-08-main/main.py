from datetime import date, timedelta, datetime 



def get_birthdays_per_week(users):
    # Створюємо порожні списки для кожного дня тижня
    users = {
        'Monday': [],
        'Tuesday': [],
        'Wednesday': [],
        'Thursday': [],
        'Friday': []
    }

    if not users:
        return users

    # Отримуємо сьогоднішню дату
    current_date = date.today()

    # Знаходимо номер поточного дня тижня (0 - понеділок, 1 - вівторок, ..., 6 - неділя)
    current_weekday = current_date.weekday()

    # Знаходимо різницю між поточним днем тижня і понеділком (переводимо на поточний день)
    days_until_monday = (current_weekday - 1) % 7  # Змінено з (current_weekday + 1) % 7

    # Знаходимо дату наступного понеділка
    next_monday = current_date + timedelta(days=days_until_monday)

    # Знаходимо дату наступної неділі
    next_sunday = next_monday + timedelta(days=6)

    # Перевіряємо, чи є користувачі з днями народження у наступному тижні
    for user in users:
        name = user['name']
        birthday = user['birthday']

         # Перевірка, чи день народження вже минув у поточному році
        if birthday < current_date:
            # Додаємо 1 рік до дати народження
            birthday = birthday.replace(year=current_date.year + 1)

        if next_monday <= birthday <= next_sunday:
            # Отримуємо день тижня для дня народження
            birthday_weekday = birthday.strftime('%A')


        # Додаємо ім'я користувача до відповідного дня тижня
        users[birthday_weekday].append(name)

    return users


if __name__ == "__main__":
    users = [
        {"name": "Jan Koum", "birthday": datetime(1976, 1, 1).date()},
    ]

    result = get_birthdays_per_week(users)
    print(result)
    # Виводимо результат
    for day_name, names in result.items():
        print(f"{day_name}: {', '.join(names)}")