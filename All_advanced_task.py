import math
import cmath
import os
from functools import reduce

def read_from_file():
    f = open(r'./input.txt', "r")
    data = f.read()
    f.close()
    return data

def first_prog():
    print('''
    Hello Maxim Toropov!!!
    You do very good webinars!
    ''')

def equation():
    def diskriminant(a,b,c):
        return b*b-4*a*c
    print('Выберите: \n 1. Если у вас коэффиценты не комплексные числа.\n 2. Если у вас коэффиценты комплексные числа.')
    check = input()
    if check.isdigit() and int(check) == 1:
        a = int(input("Введите коэффицент A: " ))
        b = int(input("Введите коэффицент B: " ))
        c = int(input("Введите коэффицент C: " ))
        print("Уравнение: (",a,")x^2 + (",b,")x + (",c,") = 0")
        if a == 0 and b !=0:
            x = -1*c/b
            if x == 0:
                print('Бесконечное множество корней')
            else:
                print('Один корень: ',x)
        elif b == 0 and a == 0 and c == 0:
            print('Бесконечное множество корней')
        elif b == 0 and a == 0 and c != 0:
            print(c," != 0")
            print('Некорректные данные')
        else:
            d = diskriminant(a,b,c)
            if d < 0:
                print('Дискриминант < 0, поэтому возможны только комплесные корни: ',end='')
                x = complex(math.sqrt(-d), 1)
                print(f'{-b/2*a} +/- {x/2*a}')
            elif d == 0:
                x = -1*b/2/a
                print('Один корень: ',x)
            else:
                x1 = (-1*b+math.sqrt(d))/2/a
                x2 = (-1*b-math.sqrt(d))/2/a
                print('Два корня: ',x1,x2)
    elif check.isdigit() and int(check) == 2:
        print('Введите коэффицент А:')
        a1, a2 = input('Введите действительную часть и коэффицент перед мнимой частью через пробел: ').split()
        print('Введите коэффицент B:')
        b1, b2 = input('Введите действительную часть и коэффицент перед мнимой частью через пробел: ').split()
        print('Введите коэффицент C:')
        c1, c2 = input('Введите действительную часть и коэффицент перед мнимой частью через пробел: ').split()
    # Проверку на не числа убрал, потому что не пропускает отрицательные коэффиценты.
    #if a1.isdigit() and b1.isdigit() and c1.isdigit() and a2.isdigit() and b2.isdigit() and c2.isdigit():
        A = complex(int(a1),int(a2))
        B = complex(int(b1),int(b2))
        C = complex(int(c1),int(c2))
        print(f'Уравнение: {A}x^2 + {B}x + {C} = 0')
        x1 = (-1*B+cmath.sqrt(diskriminant(A,B,C)))/2/A
        x2 = (-1*B-cmath.sqrt(diskriminant(A,B,C)))/2/A
        print(f'Два комплексных корня: {x1}  {x2}')
    else:
        print('Введен неверный символ')

def xor(stroka,key):
    s = ""
    for symbol in stroka:
        s += chr(ord(symbol) ^ key)
    return s
#print(xor('cdscewdcsf',3))

def usedigits(start,end):
    st = ''
    for s in range(start,end+1):
        st += str(s)
    print(f'Записываем значения в одну строку: {st}')
    for i in range (0,10):
        print(f"Число {i} встречается {st.count(str(i))} раз(a)")

def usealpha(stroka):
    #stroka = str(stroka)
    print(f'Введенная строка: {stroka}')
    while len(stroka) != 0:
        print(f'Символ {stroka[0]} встречается {stroka.count(stroka[0])} раз(а)')
        stroka = stroka.replace(stroka[0],'')

def delem(arr):
    return list(set(arr))

def check_brackets(string):
    stack = []
    brackets = {'(': ')', '[': ']', '{': '}', '<': '>'}
    flag = True
    for symbol in string:
        if symbol in brackets.keys():
            print(f"Скобку '{symbol}'', добавляю в стек.")
            stack.append(symbol)
        elif symbol in brackets.values():
            if stack:
                print(f"Следующая скобка '{symbol}'', сравниваю ее с последней из стека")
                bracket = stack.pop()
                #print(f"Извлек скобку '{bracket}'', сравниваю с '{symbol}''.")
                if brackets.get(bracket) != symbol:
                    print("Не та скобка!")
                    flag = False
                    break
                else:
                    print("Успешно!")
            else:
                print(f"Стек пустой, а у меня '{symbol}''... Не катит")
                flag = False
                break
    if flag:
        print("Текст закончился...")
    if stack:
        print(f"Стек не пустой...")
        flag = False
    print(f"Скобки расставлены {'' if flag else 'не '}правильно!")

def calc():
    helper = ['+','-','*','**','/','+-','abs',"",'c']
    def in_put():
        while True:
            try:
                t = int(input('Введите число: '))
            except ValueError:
                print("Не число, в следующий раз вводите число")
                continue
            except Exception:
                print("Что-то пошло не так")
                continue
            else:
                print('Корректные данные.\n')
                input('Для продолженя нажмите enter')
                break
        return t

    plus = lambda n,t: n + t
    minus = lambda n,t: n - t
    power = lambda n,t: n ** t
    multiplication = lambda n,t: n * t
    division = lambda n,t: n / t if t else math.inf

    print('''
Калькулятор для базовых оперций.
      Инструкция по вводу.
1.Вводите первое число больше 0 - enter
2.Выбираете операцию(если вам изначально надо было отрицательное число, меняете знак) - enter
3.При необходимости вводите число для операции - enter
4.Вы считаете новое число и снова выбираете операцию (2.)

P.S. В моем случае ошибка может быть только ValueError, других я не могу найти, потому что я отдельно ввожу операцию и отдельно число к ней.
    ''')
    input('Для продолженя нажмите enter')
    os.system("cls")
    n = in_put()
    os.system("cls")
    while True:
        os.system("cls")
        print(f'Число - {n} ')
        while True:
            operation = input('''
    Выберете операцию или введите число:
    '+' - сложение
    '-' - вычитание 
    '*' - умножение
    '/' - деление
    '**' - возведение в стемень
    '+-' - смена знака числа
    'abs' - модуль числа
    'c' - сброс
    Пустой ввод - выход
        ''')
            if operation not in helper:
                print('Вы выбрали несуществующую операцию. Попробуйте еще раз!')
                input('Для продолженя нажмите enter')
                continue
            break
        if operation == '+':
            t = in_put()
            n = plus(n,t)
        if operation == '-':
            t = in_put()
            n = minus(n,t)
        if operation == '*':
            t = in_put()
            n = multiplication(n,t)
        if operation == '/':
            while True:
                try:
                    t = in_put()
                    n = division(n,t)
                # except ZeroDivisionError:
                #     print("Деление на ноль, попробуйте другое число")
                #     continue
                except ValueError:
                    print("Не число")
                    continue
                break
        if operation == '**':
            t = in_put()
            n = power(n,t)
        if operation == '+-':
            n = -n
        if operation == 'abs':
            n = abs(n)
        if operation == 'c':
            n = n - n
        if operation == '':
            print('Goodbye!')
            break
        os.system("cls")

while True:
    os.system("cls")
    n = input('''
    Выберете:
    1.* Написать первую программу(была сделана)
    2.* Напишите скрипт решения квадратного уравнения(была сделана)
    3.* XOR шифрование(была сделана)
    4.* Частота использования цифр в диапазоне чисел(была сделана)
    5.* Частота использования символов в тексте(была сделана)
    6.* Удалить из списка элементы, значения которых уже встречались в этом же списке в предыдущих элементах(была сделана через цикл, а тут с помощью set())
    7.* Вводится текст, содержащий различные скобки, необходимо определить, все ли скобки расставлены корректно(была сделана без использования стека, но здесь переделал)
    8.* Вычисление факториала числа с использованием lambda (не рекурсия)(была сделана)
    9.* Написать программу подсчета частоты вхождений символов в текст с использованием lambda(была сделана, но некорректно)
    10.* Написать калькулятор для базовых операций сложения, вычитания, умножения, деления, возведения в степень.(была сделана)
    Пустой ввод - выход.
    ''')
    if n == '1':
        os.system("cls")
        first_prog()
        input('Для продолженя нажмите enter')
    if n == '2':
        os.system("cls")
        equation()
        input('Для продолженя нажмите enter')
    if n == '3':
        os.system("cls")
        try:
            str = input("Введите текст: ")
            if not str:
                str = read_from_file()
            key = int(input("Введите ключ: "))
        except:
            print('Еще раз')
            continue
        temp = xor(str, key)
        print(f'Зашифрованный/расшифрованный текст: {temp}')
        input('Для продолженя нажмите enter')
    if n == '4':
        os.system("cls")
        try:
            start = int(input("Введите начало диапазона: "))
            end = int(input("Введите конец диапазона: "))
        except:
            print('Еще раз')
            continue
        usedigits(start,end)
        input('Для продолженя нажмите enter')
    if n == '5':
        os.system("cls")
        stroka = input("Введите текст: ")
        if not stroka:
            stroka = read_from_file()
        stroka = str(stroka)
        usealpha(stroka)
        input('Для продолженя нажмите enter')
    if n == '6':
        os.system("cls")
        _list = [i for i in input('Введите значения элементов массива через пробел ').split()]
        print(f'После удаления повторяющихся элементов получим получим: {delem(_list)}')
        input('Для продолженя нажмите enter')
    if n == '7':
        os.system("cls")
        str = input("Введите текст: ")
        if not str:
            str = read_from_file()
        check_brackets(str)
        input('Для продолженя нажмите enter')
    if n == '8':
        os.system("cls")
        while True:
            try:
                a = int(input('Введите число факториал которого хотите узнать: '))
            except:
                print('Еще раз!')
                continue
            if a < 0:
                print('Еще раз!')
                continue
            break
        print(f'Факториал {a} равен {reduce(lambda x,y:x*y,range(1,a+1))}')
        input('Для продолженя нажмите enter')
    if n == '9':
        os.system("cls")
        string = input("Введите текст: ")
        if not string:
            string = read_from_file()
        count = list(map(lambda x: {x: string.count(x)}, set(string)))
        for i in range(0,len(count)-1):
            print(count[i])
            input('Для продолженя нажмите enter')
    if n == '10':
        os.system("cls")
        calc()
    if n == '':
        print('Goodbye!')
        break