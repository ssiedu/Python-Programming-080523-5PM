import random

while True:
    ch=input('''Game Start :
1.Yes
2.No
''')
    if ch=='y' or ch=='Y':
        com_input=random.randrange(1,6)
        user_input=int(input("Enter your Number :"))
        if com_input>user_input:
            print("Computer Number :",com_input)
            print("your guess number is low")
        elif user_input>com_input:
            print("Computer number :",com_input)
            print("Your guess number is high")
        else:
            print("Computer Number :",com_input)
            print("Both are Equal")
    else:
        break;
    
