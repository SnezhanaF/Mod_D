#Напишите алгоритм, который определяет, содержит ли число цифры цифры, 5, 7 или 9:, но работает только с числом, не приводя его в строку
n= int(input("Введите число: "))
while n >= 1:
    if n%10 == 5:
        print("Число содержит цифру 5")
    if n%10 == 7:
        print("Число содержит цифру 7")
    if n%10 == 9:
        print("Число содержит цифру 9")
    n = n // 10

def correct_func(name_arg=None):
   if name_arg is None:
       name_arg = []
   print("Аргумент до изменения", name_arg)
   name_arg.append(2)
   print("Аргумент после изменения", name_arg)

# вызовем два раза одну и ту же функцию
correct_func()
print('-----')
correct_func()
print('-----')
correct_func([124])
