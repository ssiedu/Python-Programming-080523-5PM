try:
    print("Try Block")
    x=int(input("Enter First number :"))
    y=int(input("Enter Second number :"))
    z=x/y
except TypeError:
    print("Except Block")
    print("Some Error Occured(TypeError)")
except ZeroDivisionError:
    print("Except Block")
    print("Some Error Occured(ZeroDivisionError)")
else:
    print("Else Block")
    print("value of z :",z)
finally:
    print("Finally Block")
    print("Thank you")
    
