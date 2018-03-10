number = int(input ("Начальное число"))
numbe = int(input("Конечное число"))
numb = int(input("Диапазон числа"))
if number > numbe:
    print ("Поменьше поставь начальное!")
elif numbe <= 0:
    print ("Ноль убери")
elif numb <= 0:
    print ("Ноль убери") 
else: 
    while number <= numbe:
        print(number)
        number += numb
print ("Goodbye")
        


