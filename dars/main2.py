# n = int(input("Juft son kiriting:  "))
# if n%2:
#     print("Bu son juft emas")
# else:
#     print("Rahmat!!")

# -------------------------------------------------------

# yosh = int(input("Yoshingizni kiriting:  "))

# if yosh < 4 or yosh > 60 :
#     print("Kirishingiz bepul!!")
# elif yosh < 18:
#     print("Kirish narxi 10000 so`m")
# elif yosh > 18:
#     print("Kirish narxi 20000 so`m")

# --------------------------------------------------------

# n1 = int(input("Birinchi sonni kiriting:  "))
# n2 = int(input("Ikkinchi sonni kiriting:  "))

# if n1 > n2:
#     print(f"{n1} > {n2}")
# elif n1 < n2:
#     print(f"{n1} < {n2}")
# else :
#     print("Bu sonlar teng")

# ----------------------------------------------------------------

bozorlik = ["Olma", "Anor", "Banan", "Uzum", "Mandarin", "Apelsin", "Lemon", "Shaftoli"]
savat = []
for n in range(5):
    savat.append(input("Mevani kiriting:  "))
for meva in savat:
    if meva in bozorlik:
        print(f"{meva} olindi")
    else:
        print(f"{meva} olinmadi")

