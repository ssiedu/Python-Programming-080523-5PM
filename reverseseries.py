s=int(input("Enter start limit for reverse series :"))
e=int(input("Enter end limit for reverse series :"))

for i in range(s,e-1,-1):
    print(i,end=" ")


print()
for i in range(s,e-1,-1):
    if i%2==0:
        print(i,end=" ")


print()
for i in range(s,e-1,-1):
    if i%2!=0:
        print(i,end=" ")
