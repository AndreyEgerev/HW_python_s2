#Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, 
#а некоторые – гербом. Определите минимальное число монеток, которые нужно 
#перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной. 
#Выведите минимальное количество монет, которые нужно перевернуть
import random 

nCoin = int(input('Введите кол-во монеток  -> '))
nCoinTails = 0
nCoinEagle = 0
count = 1
while count < nCoin:
    nCoinFace = random.randint(0,1)
    print (f' {nCoinFace}', end='')
    if nCoinFace == 0:
        nCoinEagle += 1
    elif nCoinFace == 1:
        nCoinTails += 1
    count += 1
print()
if nCoinEagle > nCoinTails:
    print (f'Необходимо перевернуть {nCoinTails} монетки')
else:
    print (f'Необходимо перевернуть {nCoinEagle} монетки')