#На столе лежат n монеток. Некоторые из них лежат вверх
# решкой, а некоторые – гербом. Определите минимальное число
# монеток, которые нужно перевернуть, чтобы все монетки были
# повернуты вверх одной и той же стороной. Выведите минимальное
# количество монет, которые нужно перевернуть.

n = int(input('Введите количество монеток '))
orel = 0
reshka = 0
for i in range(n):
    x = int(input('орел(1) или решка(0)? '))
    if x == 1:
        orel += 1
    else:
        reshka += 1

print(min(reshka, orel))
