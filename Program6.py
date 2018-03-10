
def main():
    sum=0
    count =int(input("Скоко бумажек у тебя в кошельке"))
    money = 0
    for i in range(1, count + 1, 1):
        money = int(input("Какая цифарка на бумажке"))
        while proverka(money) != True:
            sum+=money
         
        result(sum)


        
def proverka(money):
    if money == 200 or money == 500 or money == 1000 or money == 2000 or money == 5000 or money == 10000 or money == 20000:
        return True
    else:
        print("Ща полисию вызову")
        return False
def result(suma):
    print(suma)
    
    
main()

