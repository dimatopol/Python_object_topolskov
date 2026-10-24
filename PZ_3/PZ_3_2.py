x1 = input("Введите x1: ")
y1 = input("Введите y1: ")
x2 = input("Введите x2: ")
y2 = input("Введите y2: ")

while type(x1) != int:
    try:
        x1 = int(x1)
    except ValueError:
        print("Неправильно ввели!")
        x1 = input("Введите x1: ")

while type(y1) != int:
    try:
        y1 = int(y1)
    except ValueError:
        print("Неправильно ввели!")
        y1 = input("Введите y1: ")

while type(x2) != int:
    try:
        x2 = int(x2)
    except ValueError:
        print("Неправильно ввели!")
        x2 = input("Введите x2: ")

while type(y2) != int:
    try:
        y2 = int(y2)
    except ValueError:
        print("Неправильно ввели!")
        y2 = input("Введите y2: ")

if x1 == x2 or y1 == y2:
    print("Истина")
else:
    print("Ложь")
