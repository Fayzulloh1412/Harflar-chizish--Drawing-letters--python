from transliterate import to_latin as tl, to_cyrillic as tc

x = input("Matn kiriting: ")
if x.isascii():
    print(tc(x))
else:
    print(tl(x))