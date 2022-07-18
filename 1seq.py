count = int(input('Введите количеств элементов списка: '))
dig= []
for i in range(count):
    dig.append(input('Введите число: '))
dig.sort()
print(','.join(dig))