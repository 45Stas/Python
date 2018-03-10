sum = 0
while True:
    t = input("Введите число")
    if t != "":
        print ("Напиши что нибудь!!!")
        t1 = int(t)
    if t1 <= 0:
        print ("Ноль убери")
        continue
    sum += t1
    print ("Sum =" ,sum)
    
