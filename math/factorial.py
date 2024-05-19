

a = 1

while True:
    n = int(input("Factorial sonni kiriting: >>>  "))
    for i in range(1,n+1):
        a *= i
    print(a)
    javob = input("Dastur to'xtasinmi(Yes/No):  >>>  ")
    if javob == "Yes":
        break
    a = 1