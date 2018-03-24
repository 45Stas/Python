def vibor():
    print("1)Добавить доходы")
    print("2)Добавить расходы")
    print("3)Удалить доходы")
    print("4)Удалить росходы")
    print("5)Отсчет")
    a = int(input("Цифарку скази"))
    vb(a)
def vb(a):
    spisokdoxod = []
    spisokrasxod = []
    if a == 1:
        for i in range (1, 12+1):
            doxod = str(i) + "месяц"
            spisokdoxod.append(int(input("Введите Доход" + str(i) + "Месяц")))
        print(spisokdoxod)
    elif a == 2:
        for i in range (1, 12+1):
            doxod = str(i) + "месяц"
            spisokrasxod.append(int(input("Введите Расход" + str(i) + "Месяц")))
        print(spisokrasxod)
    elif a == 3:
        if
        for i in range (1, 12+1):
            doxod = str(i) + "месяц"
            print(spisokdoxod)
            spisokdoxod.pop(int(input("Какой по счету доход")))
            print(spisokdoxod)

    
vibor()

        
