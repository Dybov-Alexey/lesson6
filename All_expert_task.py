import math
import cmath
import os

fizzbuzz = lambda n: print(f'FizzBuzz') if n % 3 == 0 and n % 5 == 0 else print(end='') or print(f'Fizz') if n % 3 == 0 else print(end='') or print(f'Buzz') if n % 5 == 0 else print(end='') or print(f'{n}')

fact = lambda x: 1 if x == 0 else x * fact(x-1)

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

class Node:
    def __init__(self, value):
        self.left = None
        self.value = value
        self.right = None

class Tree:
    def create(self, value):
        return Node(value)

    def add(self, node , value):
        if node is None:
            return self.create(value)
        if value < node.value:
            node.left = self.add(node.left, value)
        elif value > node.value:
            node.right = self.add(node.right, value)

        return node

def preorder(unit):
        if not unit:
            return
        stack = []
        stack.append(unit)
        while stack:
            unit = stack.pop()
            print(unit.value,end=' ')
            if unit.right:
                stack.append(unit.right)
            if unit.left:
                stack.append (unit.left)

def inorder(unit):
    stack = []
    while stack or unit:
        if unit:
            stack.append(unit)
            unit = unit.left
        else:
            unit = stack.pop()
            print(unit.value,end=' ')
            unit = unit.right

root = None
tree = Tree()
root = tree.add(root, 1)
tree.add(root, 2)
tree.add(root, 3)
tree.add(root, 4)
tree.add(root, 7)
tree.add(root, 6)
tree.add(root, 8)

def calculation(str):
    if correct(str):
        stack = []
        stack = str.split()
        postfix = []
        helper = []
        priority = {"(": 1, "-": 2, "+": 2, "/": 3, "*": 3}
        for i in stack:
            if is_digit(i):
                postfix.append(i)
            elif i == '(':
                helper.append(i)
            elif i == ')':
                temp = helper.pop()
                while temp != '(':
                    postfix.append(temp)
                    temp = helper.pop()
            else:
                while helper and priority[helper[len(helper) - 1]] >= priority[i]:
                    postfix.append(helper.pop())
                helper.append(i)
        while helper:
            postfix.append(helper.pop())
        stack = postfix
        print(f"Результат вычисления равен: {connection(stack)}")
    else:
        print('Скобки расставлены неверно.')
        return

def is_digit(number):
    if number.isdigit():
        return True
    elif number[0] == '-' and number[1:].isdigit():
        return True
    else:
        return False

def connection(stack):
    helper = []
    for i in stack:
        if is_digit(i):
            helper.append(int(i))
        else:
            a = helper.pop()
            b = helper.pop()
            res = operation(b, a, i)
            helper.append(res)
    return helper.pop()


def operation(a, b, sign):
    if sign == '+':
        return a + b
    elif sign == '-':
        return a - b
    elif sign == '*':
        return a * b
    elif sign == '/':
        return a / b

def correct(str):
    stack = []
    brackets = {'(': ')', '[': ']', '{': '}', '<': '>'}
    for i in str:
        if i in brackets.keys():
            stack.append(i)
        elif i in brackets.values():
            if stack:
                bracket = stack.pop()
                if brackets.get(bracket) != i:
                    return False
            else:
                return False
    if stack:
        return False
    return True

# try:
#     int(x)
# except ValueError:
#     print("Не число")
# except TypeError:
#     print("Строки нельзя делить на число")
# except ZeroDivisionError:
#     print("Деление на ноль")
# except Exception:
#     print("Что-то пошло не так")
# else:
#     print("Задача успешно завершена")
# finally:
#     print("Задача завершена")

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
    1. ** FizzBuzz от 0 до 100, требуется наименьшая длина кода.(была сделана)
    2. ** Решение квадратного уравнения с использованием комплексных чисел.(была сделана)
    3. ** Алгоритм обхода дерева без использования рекурсии.(была сделана)
    4. ** Вводится математический пример произвольной длины, необходимо решить пример.(была сделана)
    5. ** Вычисление факториала числа с использованием lambda (рекурсия).(была сделана)
    6. ** Написать калькулятор для всех возможных операций с максимально информативными сообщениями об ошибках(не делал)
    Пустой ввод - выход.
    ''')
    if n == '1':
        os.system("cls")
        for n in range(0, 101):
            fizzbuzz(n)
        input('Для продолженя нажмите enter')
    if n == '2':
        os.system("cls")
        equation()
        input('Для продолженя нажмите enter')
    if n == '3':
        os.system("cls")
        print('Центрированный обход: ',end='')
        inorder(root)
        print('\nПрямой обход: ',end='')
        preorder(root)
        input('Для продолженя нажмите enter')
    if n == '4':
        os.system("cls")
        try:
            calculation(input('Введите пример, в котором между каждыми символами пробел: '))
        except:
            print('Вы неверно ввели пример!')
        input('Для продолженя нажмите enter')
    if n == '5':
        os.system("cls")
        while True:
            try:
                a = int(input('Введите число для которого посчитать факториал: '))
            except:
                print('Еще раз!')
                continue
            if a < 0:
                print('Еще раз!')
                continue
            break
        print(f'Факториал {a} равен {fact(a)}')
        input('Для продолженя нажмите enter')
    if n == '6':
        os.system("cls")
        calc()
    if n == '':
        print('Goodbye!')
        break
