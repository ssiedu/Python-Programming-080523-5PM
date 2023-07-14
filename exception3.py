try:
    x=int(input("Enter any number upto 100: "))
    if x>100:
        raise ValueError
except ValueError:
    print(x,"is out of range ")
else:
    print(x,"is in range")
