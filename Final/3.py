# На обработку поступает натуральное число. 
# Нужно написать программу, которая выводит на экран сумму четных цифр этого числа или 0, 
# если четных цифр в записи нет. Программист торопился и написал программу неправильно. 
# Найди все ошибки в этой программе (их может быть одна или несколько). 
# Известно, что каждая ошибка затрагивает только одну строку и может быть исправлена без изменения других строк

n = input()
s = 0
while n > 10:
    if n % 2 == 1:
        s = n % 10
    n //= 10
print(s)