try:
    x=100
    y=a
    z=x/y
    print("value of z :",z)
except TypeError:
    print("Unsupported operation")
except ZeroDivisionError:
    print("Division by zero not allowed")
except:
    print("404 Error:Server not found")
