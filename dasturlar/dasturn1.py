
##### dasturn1 dasturi


buyruq = 'stop'
while buyruq != 'start':
    buyruq = input("Buyruqni kiriting:")

print("Bu dastur ma'lum bir oraliqdagi sonlarning darajalarini qaytaruvchi dastur")

n = input("1 va 5 oraliqdagi bitta darajani tanlang:  ")
n = int(n)

if n == 2:
    k = input("10 dan 80 gacha bo'lgan soningizni kiriting: ")
    k = int(k)
    for i in range(k, k+20):
        print(f"{i} sonining kvadrati {i**2} ga teng!")
elif n == 3:
    k = input("10 dan 80 gacha bo'lgan soningizni kiriting: ")
    k = int(k)
    for i in range(k, k+20):
        print(f"{i} sonining kubi {i**3} ga teng!")    
else:
    print("Qoidaga amal qilmadingiz, kod toxtadi, qayta ishlatish uchun F5 tugmasini bosing")


print("Dastur ishni yakunladi, hizmatingiz uchun rahmat")






    
        



