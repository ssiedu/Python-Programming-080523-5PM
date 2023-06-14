s=int(input("Enter start Limit :"))
E=int(input("Enter End limit :"))
sum=0
for i in range(s,E+1):
    sum=sum+i
print("Sum of natural Numbers : ",sum)

print()
sum=0
for i in range(s,E+1):
    if i%2==0:
        sum=sum+i
print("Sum of Even numbers :",sum)

print()
sum=0
for i in range(s,E+1):
    if i%2!=0:
        sum=sum+i
print("Sum of Even numbers :",sum)
