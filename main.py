# Домашнее задание_Условная консткурция. Операторы: if , elif , clse
# Ввод трех целых чисел
first = int(input("Введите первое число: "))
second = int(input("Введите второе число: "))
third = int(input("Введите третье число: "))

# Проверка на равенство чисел
if first == second == third:
    print(3)
elif first == second or first == third or second == third:
    print(2)
else:
    print(0)
