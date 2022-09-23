# задача 1
my_file = open('test.txt', 'w')
l = input('Введите текст \n')
while l:
    my_file.writelines(l)
    l = input('Введите текст \n')
    if l == '':
        break
my_file.close()


# задача 2
with open('test1.txt', 'r') as my_file:
    lines = 0
    words = 0
    symbols = 0
    for line in my_file:
        lines += 1
        words += len(line.split())
        symbols += len(line.strip('\n'))
print("Lines:", lines)
print("Words:", words)
print("Symbols:", symbols)
my_file.close()

# задача 3
with open('test2.txt', 'r') as my_file:
    a = []
    b = []
    my_list = my_file.read().split('\n')
    for i in my_list:
        i = i.split()
        if int(i[1]) < 20000:
           b.append(i[0])
        a.append(i[1])
print(f'Оклад меньше 20.000 {b}, средний оклад {sum(map(int, a)) / len(a)}')

# задача 4

a = {'One' : 'Один', 'Two' : 'Два', 'Three' : 'Три', 'Four' : 'Четыре'}
new_file = []
with open('test3.txt', 'r') as f2:
       for i in f2:
        i = i.split(' ', 1)
        new_file.append(a[i[0]] + '  ' + i[1])
    print(new_file)

# задача 5

f = open('test4.txt', 'w')
print("Введите набор чисел, разделенных пробелами: ")
f = open('test4.txt', 'r')
list = f.read().split()
total = 0
for elem in list:
    total += float(elem)
print("Сумма чисел в файле: ", total)
f.close()