n = input("Введите четырехзначное число: ")

while type(n) != int:
    try:
        n = int(n)
    except ValueError:
        print("Неправильно ввели!")
        n = input("Введите четырехзначное число: ")

a = n // 1000
b = n // 100 % 10
c = n // 10 % 10
d = n % 10

if a == d and b == c:
    print("Истина")
else:
    print("Ложь")
