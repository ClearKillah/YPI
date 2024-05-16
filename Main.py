from datetime import datetime


def find_youngest_and_oldest(students):
    # Сортировка списка студентов по дате рождения
    students_sorted = sorted(students, key=lambda x: datetime.strptime(x['dob'], '%d.%m.%Y'))

    # Самый младший студент
    youngest = students_sorted[-1]

    # Самый старший студент
    oldest = students_sorted[0]

    report = f"""
    Самый младший студент:
    ФИО: {youngest['name']}
    Дата рождения: {youngest['dob']}

    Самый старший студент:
    ФИО: {oldest['name']}
    Дата рождения: {oldest['dob']}
    """

    return report


# Пример списка студентов
students = [
    {'name': 'Иванов Иван Иванович', 'dob': '15.02.2002'},
    {'name': 'Петров Петр Петрович', 'dob': '23.06.2000'},
    {'name': 'Сидорова Анна Ивановна', 'dob': '12.05.2001'},
    {'name': 'Кузнецов Михаил Сергеевич', 'dob': '01.09.1999'}
]

print(find_youngest_and_oldest(students))
