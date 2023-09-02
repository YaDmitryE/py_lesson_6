# https://github.com/YaDmitryE/py_lesson_6

# Вводим целые числа A и B
A = int(input("Введите число A: "))
B = int(input("Введите число B: "))

# Перебираем числа от A до B включительно
for num in range(A, B + 1):
    # Проверяем, является ли число четным
    if num % 2 == 0:
        # Выводим четное число
        print(num, end=" ")
