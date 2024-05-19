# odam = {"Yoshi": "66", "Manzil": "Obod Turmush", "Ismi": "Fayzulloh"}
# print(f"{odam['Ismi']} ning yoshi {odam['Yoshi']} da. U hozir {odam['Manzil']} mahallasida yashaydi ")

# --------------------------------------------------------------------------

# taom = {
#     "Aziz": "osh",
#     "Bittasi": "chumoli",
#     "Yana bittasi": "gosht",
#     "Farrux": "Kolbasa",
#     "Zahiriddin": "non"}

# print(f"Azizning sevimli taomi {taom['Aziz']}. \n Bitta qiz {taom['Bittasi']} go`shtini yeyishni juda yoqtiradi")

# --------------------------------------------------------------------------------------

# kod = {
#     "float": "o`nli kasr",
#     "integer": "butun son",
#     "string": "matn",
#     "if": "agar",
#     "else": "aks holda"
# }

# soz = input("Pythondagi kodni kiriting:  ")
# soz = soz.lower()

# print(kod.get(soz, "Bunday so`z mavjud emas").title())

#------------------------------------------------------------

# nima = {
#     "bolean": "mantiqiy qiymat",
#     "string": "matn",
#     "integer": "butun son",
#     "float": "o`nli kasr",
#     "print": "konsolga chiqarish",
#     "if": "shart",
#     "del": "elementni o`chiradi",
#     "appent": "yangi element qo`shish",
#     "range": "sonlar oralig'i"    
# }

# print("Pythondagi so`zlar ma`nosi")
# for n, m in nima.items():
#     print(f"{n.title()} so`zining ma`nosi {m} degani.")

# --------------------------------------------------------------------

# davlat = {
#     "turkiya": "istambul",
#     "o'zbekiston": "toshkent",
#     "qozog'iston": "astana",
#     "rossiya": "moskva",
#     "amerika": "vashington",
#     "xitoy": "pekin",
#     "misr": "keniya"
# }

# # print("Davlatlarning nomi")
# # for n in sorted(davlat.keys()):
# #     print(n.upper())

# # print("Davlatlarning poytaxlari")
# # for k in sorted(davlat.values()):
# #     print(k.title())

# j = input("Istalgan davlatingizni kiriting:   ")
# if j in davlat.keys():
#     print(f"{j} ning portaxti {davlat[j]}")

# -----------------------------------------------------------------

one = {
    "ism": "Abdulla",
    "familiya": "Qodiriy",
    "tyil": 820,
    "umri": 60
}

two = {
    "ism": "Abdulla",
    "familiya": "Avloniy",
    "tyil": 1890,
    "umri": 70
}

three = {
    "ism": "Mahmud",
    "familiya": "Zamaxshariy",
    "tyil": 1820,
    "umri": 65
}

four = {
    "ism": "Abdulla",
    "familiya": "Sosoniy",
    "tyil": 1920,
    "umri": 80
}

onef = [one, two, three, four]
for n in onef:
    print(f"{n['ism']} {n['familiya']}. {n['tyil']} - yili tug'ilgan. {n['umri']} yil umr ko`rgan")









