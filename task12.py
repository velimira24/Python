print('Введите сумму двух чисел: ')
x = int(input())
print('Введите произведение двух чисел: ')
y = int(input())
for i in range(x):
  for j in range(y):
     if x == i + j and y == i * j:
      print(f'Первое число: {i}, второе число:{j}')