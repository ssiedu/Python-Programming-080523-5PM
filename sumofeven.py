n=int(input("enter any number :"))
i=1
sum=0
add=0
while i<=n:
    if i%2==0:
        sum=sum+i
    else:
        add=add+i
    i=i+1
print("Sum of even number series :", sum)
print("sum of odd number series :",add)
