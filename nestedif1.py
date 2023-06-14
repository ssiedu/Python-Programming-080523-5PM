num=int(input("Enter any number :"))
if num%2==0:
    print("number is divisible by 2")
    if num%3==0:
        print("number is divisible by 3")
    else:
        print("number is not divisible by 3")
else:
    print("number is not divisible by 2")
