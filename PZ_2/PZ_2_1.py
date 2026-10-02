try:
    n = int(input("Введите количество секунд: "))
    minutes = n // 60
    print("Количество полных минут:", minutes)
except:
    print("Ошибка")
