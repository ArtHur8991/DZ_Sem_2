
#1. Напишите программу, которая принимает на вход два числа и проверяет, является ли одно число квадратом другого.   
#    *Примеры:*  
#    - 5, 25 -> да
#    - 4, 16 -> да
#    - 25, 5 -> да
#    - 8,9 -> нет

#Решение
#a = int(input("Введите число a: "))
#b = int(input("Введите число b: "))

#if a*a == b or b*b == a:
#    print('да')
#else:
#    print('нет')


# Альтерантивное решение
#try:
    #a = int(input("Введите число a: "))     b = int(input("Введите число b: "))
    #if a*a == b:
    #   print ("второе число является квадратом первого")
    #elif b*b == a:     
    #   print("первое число является квадратом второго")
    #else:
    #   print("квадраты отсутствуют")
#except:
    #print("надо вводить именно целые числа")


#def seek_squares(a,b):
#    if a*a == b:
#        print ("второе число является квадратом первого")
#    elif b*b == a:
#        print("первое число является квадратом второго")
#    else:
#        print("квадраты отсутствуют") 

#try:
#    x1 = int(input("Введите число a: "))     x2 = int(input("Введите число b: "))
#     seek_squares(x1,x2)
#except:
#    print("надо вводить именно целые числа")


 # С булевой с возвратом значения 


# def seek_squares(a,b):
#    seek = False
#    if a*a == b or b*b == a:
#        seek = True
#    return seek

#try:
#    x1 = int(input("Введите число a: "))
#    x2 = int(input("Введите число b: "))
#    if seek_squares(x1,x2):
#        print("Да")
#    else:
#        print("Нет")
#except:
#    print("надо вводить именно целые числа")



#Задача 2. Напишите программу, которая на вход принимает 5 чисел и находит максимальное из них.
    
#    Примеры:
    
#    - 1, 4, 8, 7, 5 -> 8
#    - 78, 55, 36, 90, 2 -> 90

#def numberArray():
#    listNumber = []
#    for _ in range(5):
#        number = int(input("введите число: "))
#        listNumber.append(number)
#    maxNumber = listNumber[0]
#    for num in listNumber:
#        if num > maxNumber:
#            maxNumber = num
#    return maxNumber

#print(numberArray())












#1. Напишите программу, которая будет на вход принимать число N и выводить числа от -N до N
    
#    *Примеры:* 
    
#    - 5 -> -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5


#n = int(input('Вести число : '))
#for i in range(n*2+1):
#    print(i-n, end=" ")

#Другой вариант 

#n = int(input("Введите число N: "))

#for i in range(-n, n+1):
#    print(i, end = ' ')
















#2. Напишите программу, которая будет принимать на вход дробь и показывать первую цифру дробной части числа.
    
#    *Примеры:*
    
#    - 6,78 -> 7
#    - 5 -> нет
#   - 0,34 -> 3



a = float(input("Введите дробь: "))
if a % 1 != 0:
    b = a * 10
    print(int(b % 10))
else:
    print("нет")

#Другой вариант



#def getX(n):
#    x = int(n % int(n) * 10)
#    if x == 0:
#        return 'Нет';
#    else:
#        return x


#n = float(input('Вести число : '))

#print(getX(n))
















#3. Напишите программу, которая принимает на вход число и проверяет, кратно ли оно 5 и 10 или 15, но не 30.

#try:
#    a = int(input("Введите число: "))

#    if( a % 5 == 0 and a % 10 == 0 or a % 15 == 0) and a % 30 != 0:
#        print("Кратно")
#    else:
#        print("не кратно")
#except:
#    print("некорректный ввод ")

