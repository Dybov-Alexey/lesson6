def xor(stroka,key):
    s = ""
    for symbol in stroka:
        s += chr(ord(symbol) ^ key)
    return s

def read_from_file():
    f = open(r'./input.txt', "r")
    data = f.read()
    f.close()
    return data

while True:
    try:
        n = int(input('''
      Выберете:
      1. Зашифровать.
      2. Расшифровать
      3. Выход. \n '''))
    except:
        print('Еще раз')
        continue
    if n == 1:
        try:
            str = input("Введите текст: ")
            if not str:
                str = read_from_file()
            key = int(input("Введите ключ: "))
        except:
            print('Еще раз')
            continue
        temp = xor(str, key)
        print(f'Зашифрованный текст: {temp}')
    if n == 2:
        try:
            str = input("Введите текст: ")
            if not str:
                str = read_from_file()
            key = int(input("Введите ключ: "))
        except:
            print('Еще раз')
            continue
        temp = xor(str, key)
        print(f'Расшифрованный текст: {temp}')
    if n == 3:
        print('Goodbye!')
        break