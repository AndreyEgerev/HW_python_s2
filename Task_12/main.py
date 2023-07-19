# Задача 12: Петя и Катя – брат и сестра. Петя – студент, 
# а Катя – школьница. Петя помогает Кате по математике. 
# Он задумывает два натуральных числа X и Y (X,Y≤1000), 
# а Катя должна их отгадать. Для этого Петя делает две подсказки. 
# Он называет сумму этих чисел S и их произведение P. 
# Помогите Кате отгадать задуманные Петей числа.
maxRange = 1000
minRange = 0
while True:
    nSum = int(input('Введите сумму чисел -> '))
    if nSum > maxRange:
        print ('Введено слишком большое число')
    else:
        break
while True:   
    nMult = int(input('Введите произведение чисел -> '))
    if nMult > maxRange:
        print ('Введено слишком большое число')
    else:
        break
x, y = 0, 0
# x+y=S -> y=S-x
# x*y=P -> x*(S-x)=P
# while x <= maxRange-1:
#     if x*(nSum-x) == nMult:
#         break
#     x += 1

# while x*(nSum-x) != nMult:
#     x += 1
#y = nSum - x
while x <= maxRange:
    while y <= maxRange:
        if x+y == nSum and x*y == nMult:
            break
        y += 1
    if x+y == nSum and x*y == nMult:
        break
    x += 1
    y = minRange
    
if x == maxRange+1 and y == minRange:
    print ('Решения нет')
else:
    print (f'Загаданные числа {x} и {y}')