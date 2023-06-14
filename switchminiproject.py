print('''Enter any one choice-
1.Addition
2.Subtraction
3.Multiplication
4.Division
5.Modulus
 ''')
n1=int(input("Enter first Number :"))
ch=input("Enter operator :")
n2=int(input("Enter Second Number :"))
match ch:
    case '+':
        print("Addtion :", n1+n2)
    case '-':
        print("Subtraction :",n1-n2)
    case '*':
        print("Multiplication :", n1*n2)
    case '/':
        print("Division :", n1/n2)
    case '%':
        print("Modulus :", n1%n2)
    case _:
        print("Please Enter valid choice")
