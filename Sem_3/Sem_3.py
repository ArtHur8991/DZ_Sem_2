#def summa1(): #эта функця ничего не возвращает, только печатает на экран
#a=3
#b=6
#print(a+b)

##summa1()

#def summa2(): #эта функця уже возвращает значение
#a=int(input("Введите первое число "))
#b=int(input("Введите второе число "))
#return a+b

##print(summa2())

#x1=6
#x2=5

#def summa3(): #эта функця уже возвращает значение на основе глобальных переменных - не профессионально
#return x1 + x2

##print(summa3())
#sum = 0

#def summa4(): #эта функця изменяет глобальную переменную
#global sum
#a=int(input("Введите первое число "))
#b=int(input("Введите второе число "))
#sum = a + b

##summa4()
##print(sum)

#def summa5(a,b): #эта функция уже принимает на вход аргументы и возвращает значение
#return a+b

#try:
#a1=int(input("Введите первое число "))
#b1=int(input("Введите второе число "))
#print(summa5(a1, b1))
#except:
#print("надо было вводить именно целое число")






#16. Задайте список из n чисел последовательности (1 + 1/n)*n и выведите на экран их сумм



#def sequence(n):
#return (1 + 1/n)**n

#def feel_list(n):
#list = []
#for i in range(1, n+1):
#list.append(sequence(i))
#return list

#def main():
#n = int(input("Enter n: "))
#list_sequence = feel_list(n)
#print(list_sequence)
#print("Sum of sequence: ", sum(list_sequence))

#if __name__ == "__main__":
#main()

#17. Задайте список из N элементов, заполненных числами из промежутка [-N, N]. Найдите произведение элементов на указанных позициях. Позиции хранятся в файле file.txt в одной строке одно число.



#import random
#import os

#path = "Seminars\Seminar3\CWT2_input_data.txt"

#def fill_list(n):
#    list = []
#    for i in range(0, n):
#        list.append(random.randint(-n, n))
#    return list

#def read_file():
#    file = open(path, "r")
#    list = []
#    for line in file:
#        list.append(int(line))
#    file.close()
#    return list

#def multi_on_pos(list, pos):
#    result = 1
#    for i in range(0, len(list)):
#        result *= list[i]
#    return result

#def main():
#    n = int(input("Ведите N: "))
#    list = fill_list(n)
#    print(list)
#    positions = read_file()
#    print(positions)
#    print("Произведение элементов на указанных позициях: ", multi_on_pos(list, positions))

#if __name__ == "__main__":
#   main()





    #как из текстового файла получать инфу
#def read_file():
#    file = open(path, "r")
#    list = []
#    for line in file:
#        list.append(int(line))
#    file.close()
#    return list









#20. Задайте список. Напишите программу, которая определит, присутствует ли в заданном списке строк некое число.





#seq =["uhbnsfdhu", "ij8", "jsj", "10"]

#def sequence(number, seq):
#    result = False

#    for i in seq:
#        if str(number) in i:
#            result = True
#            break
#    return result

#print(sequence(8, seq))


def searchN(list1, n):
    global f
    for i in range(len(list1)):
        if n in list1[i]:
            f = 1
            break

try:
    n = int(input("Введите n: "))
except:
    print('Вводите числа!')
    exit()

f = 0
list1 = ['asd','qwwe','ddfgg','eeee','werwer3wewe34343w','4','233','wew']
searchN(list1,str(n))
if f == 1:
    print("есть")
else:
    print("нет")






#21. Напишите программу, которая определит позицию второго вхождения строки в списке либо сообщит, что её нет.

#*Пример:*

#- список: ["qwe", "asd", "zxc", "qwe", "ertqwe"], ищем: "qwe", ответ: 3
#- список: ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"], ищем: "йцу", ответ: 5
#- список: ["йцу", "фыв", "ячс", "цук", "йцукен"], ищем: "йцу", ответ: -1
#- список: ["123", "234", 123, "567"], ищем: "123", ответ: -1
#- список: [], ищем: "123", ответ: -1




list1 = ["qwe", "asd", "zxc", "qwe", "ertqwe"]
search = input("Enter: ")

def find_second(list1, search):
    result = -1
    count = 0
    for i in range(len(list1)):
        if list1[i] == search:
            count += 1
            if count == 2:
                result = i
    return result

print(find_second(list1, search))