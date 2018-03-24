def olivie():
    ludi = (int(input("Введите колво человек")))
    ingr = ("Картофель ", "лук ", "колбаса", "майонез", "соленные огурцы", "морковь")
    gramm = (50, 20, 100, 15, 30, 30) * ludi
    for i in range(0, 5+1):
        print(ingr[i] + " - " + str(gramm[i] * ludi) + "гр.")
   
olivie()
