#В некоторой школе решили набрать три новых мат класса и оорудовать кабинеты дя них новыми партами.
#За каждой партой может сидеть 2 учащихся. Известно кол-во учащихся в каждом из трех классов. Выведите наименьшее число парт,  которое нужно приобрести на них.

a = int(input("Введите кол-во учеников в 1-ом кабинете: "))
b = int(input("Введите кол-во учеников в 2-ом кабинете: "))
c = int(input("Введите кол-во учеников в 3-ом кабинете: "))

result = a //2 + a % 2 + b // 2 + b % 2  + c // 2 + c % 2
print(result)

#import math
#result = math.ceil(a/2) + math.ceil(b/2)+math.ceil(c/2) 