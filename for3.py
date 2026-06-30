a = int(input("a= "))
b = int(input("b= "))

soni = 0

for i in reversed(range(a+1,b)):
    print(i)
    soni+=1
print("soni= ",soni)
