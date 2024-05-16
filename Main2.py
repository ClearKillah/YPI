def convert_number(number):
    octal_representation = oct(number)
    hexadecimal_representation = hex(number)

    report = f"""
    Вводимое значение: {number}

    Восьмиричное представление: {octal_representation}
    Шестнадцатеричное представление: {hexadecimal_representation}
    """

    return report


# Пример использования функции
number = 12345
print(convert_number(number))
