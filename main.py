from datetime import date, datetime, timedelta



def get_birthdays_per_week(users):
    birthdays_per_week = {
        'Monday': [],
        'Tuesday': [],
        'Wednesday': [],
        'Thursday': [],
        'Friday': []
    }

    if not users:
        return {}

    today = date.today()

    for user in users:
        user_birthday = user["birthday"]

        if user_birthday < today:
            user_birthday = user_birthday.replace(year=2024) 

        if user_birthday <= today + timedelta(days=7):  # Перевірка наступного тижня
            if user_birthday.weekday() > 4:  # Якщо день народження вихідний
                if (user_birthday).year != today.year:  # Якщо наступний тиждень в наступному році
                    birthdays_per_week[user_birthday.strftime("%A")].append(user["name"])
                else:
                    birthdays_per_week['Monday'].append(user["name"])
            else:
                birthdays_per_week[user_birthday.strftime("%A")].append(user["name"])

    birthdays_per_week = {day: names for day, names in birthdays_per_week.items() if names}

    return birthdays_per_week


if __name__ == "__main__": 
    users = [
        {   
            "name" : "Jan",
            "birthday" : datetime(2023, 3, 9).date()
        },
        {   
            "name" : "Bob",
            "birthday" : datetime(2024, 3, 16).date()
        },
        {   
            "name" : "Hoop",
            "birthday" : datetime(2024, 3, 9).date()
        }
    ]
 
    result = get_birthdays_per_week(users)
    # Виводимо результат
    for day_name, names in result.items():
        print(f"{day_name}: {', '.join(names)}")
