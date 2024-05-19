# ---------------------------------
n = []
for i in range(4):
    k = input("Matn kiriting:  ")
    n.append(k)

def bosh_harf(son):
    while n:
        l = n.pop()
        print(l.title())
        
bosh_harf(n)