a = ['-', '-', '-',]
b = ['-', '-', '-',]
c = ['-', '-', '-',]


player = input("Игра Крестики-Нолики\n"
               "---------------------\n"
               "Вводите координаты по очереди,\n"
               "каждый занимает свою клетку\n"
               "------------------------------\n"
               "Отправьте любой символ для старта игры: ")


def place():
    print("  0 1 2")
    print('0', ' '.join(a))
    print('1', ' '.join(b))
    print('2', ' '.join(c))


def wins_x():
    if a == ['x', 'x', 'x']:
        return "You win"
    if b == ['x', 'x', 'x']:
        return "You win"
    if c == ['x', 'x', 'x']:
        return "You win"
    #------------------------
    if a[0] == 'x' and b[0] == 'x' and c[0] == 'x':
        return "You win"
    if a[1] == 'x' and b[1] == 'x' and c[1] == 'x':
        return "You win"
    if a[2] == 'x' and b[2] == 'x' and c[2] == 'x':
        return "You win"
    #------------------------
    if a[0] == 'x' and b[1] == 'x' and c[2] == 'x':
        return "You win"
    if a[2] == 'x' and b[1] == 'x' and c[0] == 'x':
        return "You win"


def wins_0():
    if a == ['0', '0', '0']:
        return "You win"
    if b == ['0', '0', '0']:
        return "You win"
    if c == ['0', '0', '0']:
        return "You win"
    #------------------------
    if a[0] == '0' and b[0] == '0' and c[0] == '0':
        return "You win"
    if a[1] == '0' and b[1] == '0' and c[1] == '0':
        return "You win"
    if a[2] == '0' and b[2] == '0' and c[2] == '0':
        return "You win"
    #------------------------
    if a[0] == '0' and b[1] == '0' and c[2] == '0':
        return "You win"
    if a[2] == '0' and b[1] == '0' and c[0] == '0':
        return "You win"


def hodim():
    if player == "0 0":
        a[0] = "x"
        return a
    if player == "0 1":
        a[1] = "x"
        return a
    if player == "0 2":
        a[2] = "x"
        return a
    #---------------------
    if player == "1 0":
        b[0] = "x"
        return b
    if player == "1 1":
        b[1] = "x"
        return b
    if player == "1 2":
        b[2] = "x"
        return b
    #-----------------------
    if player == "2 0":
        c[0] = "x"
        return c
    if player == "2 1":
        c[1] = "x"
        return c
    if player == "2 2":
        c[2] = "x"
        return c


def hodim_pc():
    if player == "0 0":
        a[0] = "0"
        return a
    if player == "0 1":
        a[1] = "0"
        return a
    if player == "0 2":
        a[2] = "0"
        return a
    #---------------------
    if player == "1 0":
        b[0] = "0"
        return b
    if player == "1 1":
        b[1] = "0"
        return b
    if player == "1 2":
        b[2] = "0"
        return b
    #-----------------------
    if player == "2 0":
        c[0] = "0"
        return c
    if player == "2 1":
        c[1] = "0"
        return c
    if player == "2 2":
        c[2] = "0"
        return c


mov = 0
while True:
    if hodim_pc() or hodim():
        mov += 1
    if mov == 9:
        place()
        print("Ничья")
        break
    if mov % 2 == 1:
        print("2-й игрок ходит\n"
              "--------")
        hodim_pc()
    else:
        print("1-й игрок ходит\n"
              "--------")
        hodim()
    if wins_x() or wins_0():
        place()
        print("Ты победил")
        break
    place()
    player = input("--------\n"
                   "Введите координаты: ")













