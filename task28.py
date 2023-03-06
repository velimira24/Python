def recsum(a, b):
    if b == 0:
        return a
    return 1 + recsum(a, b - 1)

a = int(input('Введите первое число: '))
b = int(input('Введите второе число: '))
print(recsum(a, b))