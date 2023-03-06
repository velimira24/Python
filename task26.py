def ABtimes(a, b):
    if b == 0:
        return 1
    return a * ABtimes(a, b - 1)

a = int(input('Введите число: '))
b = int(input('Введите степень: '))
print(ABtimes(a, b))