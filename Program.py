# Найдите сумму цифр трехзначного числа.
# *Пример:*
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0) |


number = int(input("Введите трехзначное число: "))

sum = number // 100 + (number % 100 // 10) + number % 10
print (f"{number} -> {sum}")