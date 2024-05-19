

n = int(input("Son kiriting:"))
y = "Yoq"
h = "Ha"
flag = 0

if n == 1:
    print(y)
    flag += 1

for i in range(2, n-1):
    if n%i == 0:
        print(y)
        flag += 1
        break
    
if flag == 0 :
    print(h)


