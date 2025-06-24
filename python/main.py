def conventor(number, from_measuring_system, to_measuring_system):
    try:
        decimal_number = int(number, from_measuring_system) # представляем число в десятичной системе исчисления
    except ValueError:
        # Если ошибка, значит такого числа в данной системе не существует - неверный ввод от пользователя
        return "Вы неверно ввели данные о числе!"

    if decimal_number == 0:
        # Чтобы не было пустого вывода, обрабатываем нуль заранее
        return f"Ваше число {number} переведено из {from_measuring_system} в {to_measuring_system}! Результат: 0"

    systems = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ" # все символы в системах исчисления

    result = ""
    while decimal_number != 0:
        # Для перевода из десятичной системы (в которую мы ранее перевели число пользователя) в ту, которую он хочет
        # необходимо делить за нужную систему исчесления и записывать остатки при делении в обратном порядке

        # Первым этапом приписываем к концу результата остаток от деления:
        result = systems[decimal_number % to_measuring_system] + result
        # А затем уменьшаем наш decimal_number делением нацело:
        decimal_number //= to_measuring_system
    return f"Ваше число {number} переведено из {from_measuring_system} в {to_measuring_system}! Результат: {result}"

def main():
    user_input = input("Введите число: ").upper() # Переводим в верхний регистр для простоты

    try:
        from_measuring_system = int(input("Введите, из какой системы переводим: "))
        to_measuring_system = int(input("Введите, в какую систему переводим: "))
    except ValueError:
        # Обрабатываем случай, если пользователь введёт строку вместо числа в качестве системы исчисления
        return "Вы неверно ввели информацию о системе исчисления. Это должно быть число!"

    if not (2 <= from_measuring_system <= 36 and 2 <= to_measuring_system <= 36):
        return "Системы счисления должны быть в диапазоне от 2 до 36!"
    
    return conventor(user_input, from_measuring_system, to_measuring_system)

# Обрабатываем возможные ошибки
try:
    result = main()
except Exception as exception:
    result = str(exception)

print(result)