
# def malumot_ber(ism, yosh, joriy_yil=2020):
#     """Foydalanuvchi yoshini so`rab unga malumot beruvchi funksiya"""
#     print(f"{ism.title()} {joriy_yil-yosh} - yilda tug'ilgan.")
    
# isml = input("Ismingizni kiriting:  ")
# yoshl = int(input("Yoshingizni kiriting:  "))

# malumot_ber(isml, yoshl)

# ---------------------------------------

def darajaga_oshir(son):
    """Foydalanuvchidan son so`rab uning darajalariga oshiruvchi funksiya"""
    print(f"{son} sonining kvadrati {son**2} ga teng. Uning kubi esa {son**3} ga teng.")
    
n = int(input("Son kiriting:  "))
darajaga_oshir(n)