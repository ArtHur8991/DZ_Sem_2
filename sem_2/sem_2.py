#sp = [2,True, "Hi",6666]
#sp.append(777)
#print(sp)

#sp.remove(2) #удалили по значению
#print(sp)

#sp.pop(-1) #удалили по индексу
#print(sp)

#slov = {}

#slov["Петр"] = 8927116646
#slov["Иван"] = 444444
#print(slov)
#print(slov.keys())
#for i in slov:
#print(i,slov[i])

#for x,y in slov.items():
#print(x,y)




#10. Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.

#*Пример:*

#- A (3,6); B (2,1) -> 5,09
#- A (7,-5); B (1,-1) -> 7,21




#x1 = int(input('Enter x1: '))
#y1 = int(input('Enter y1: '))
#x2 = int(input('Enter x2: '))
#y2 = int(input('Enter y2: '))

#rez = ((x2-x1)**2+(y2-y1)**2)**0.5

#print(round(rez,2))


#import math

#x1 = int(input('Введите кооринту x1: '))
#y1 = int(input('Введите кооринту y1: '))

#x2 = int(input('Введите кооринту x2: '))
#y2 = int(input('Введите кооринту y2: '))

#result = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
#print(round(result, 5))






#11. Напишите программу, которая принимает на вход число N и выдаёт последовательность из N членов.

#*Пример:*

#- Для N = 5: 1, -3, 9, -27, 81


#n = int(input('Введите N '))
#z = 1
#for i in range(n):
#print(z, end = " " )
#z = z * -3
#print()





#Рандом

#import random
#print(random.randint(-10,10) )

#Библиотека

#from random import randint
#print (randint(-5,3) )














#12. Для натурального n создать словарь индекс-значение, состоящий из элементов последовательности 3n + 1.

#*Пример:*

#- Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}



#def dictionare():
#print("Колличество элементов словоря: ")
#number = int(input("Введите значение: "))
#dict = {}
#for i in range(1, number + 1):
#dict[i] = 3 * i + 1
#print(dict)









#13. Напишите программу, в которой пользователь будет задавать две строки, а программа - определять количество вхождений одной строки в другой.

#str1 = input('Введите строку 1: ')
#str2 = input('Введите строку 2: ')
#counter = 0

#for i in range(len(str2)):
#if str1 == str2[i: i+len(str1)]:
#counter += 1
#print(counter)





#line1 = input("Введи 1 строку: ")
#line2 = input("Введи 2 строку: ")
#count = 0

#def fun(line1,line2):
#global count
#for i in range(len(line1) - len(line2) + 1):
#if line1[i:i+len(line2)] == line2:
#count += 1

#if len(line1) > len(line2):
#fun(line1,line2)
#else:
#fun(line2,line1)

#print(count)






