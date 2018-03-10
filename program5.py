t = int(input  ("Сколько будешь плюсовать"))
if t != "":
        print ("Напиши что нибудь!!!")
        t1 = int(t)        
sum = 0
for i in range(1, t1 + 1, 1):
    number = int(input("ведите число"))
    sum = number + sum  
print (sum)
