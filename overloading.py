from multipledispatch import dispatch

@dispatch(int,int)
def Addition(num1,num2):
    add=num1+num2
    print("Addition of two int value :",add)

@dispatch(int,int,int)
def Addition(num1,num2,num3):
    add=num1+num2+num3
    print("Addition of three int value :",add)

@dispatch(int,float)
def Addition(num1,num2):
    add=num1+num2
    print("Addition of two diff value :",add)

@dispatch(float,float)
def Addition(num1,num2):
    add=num1+num2
    print("Addition of two float value :",add)

Addition(100,200)
Addition(100,12.33)
Addition(200,10,20)
Addition(2.3,4.5)




    
