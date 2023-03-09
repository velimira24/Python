import random
 
list_1=[]
n=int(input("Введите количество элементов в массиве: "))
for i in range(n):
    list_1.append(random.randint(0,100))
print(list_1)


min_number = int(input("Введите заданный минимум диапазона массива (оно должно быть не меньше 0):"))
if min_number < 0:
    print ('Введенное число меньше 0, попробуйте еще раз')
else:
    max_number = int(input("Введите заданный максимум диапазона массива (оно должно быть не больше 100):"))
    if max_number>100:
        print ('Введенное число больше 100, попробуйте еще раз')
    else:
         for i in range(len(list_1)):
             if min_number <= list_1[i] <= max_number:
                  print(i)