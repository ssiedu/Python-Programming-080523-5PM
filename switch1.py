ch=input("Enter any charcater :")
match ch:
    case '1'|'a':
        print("C programming")
    case '2':
        print("C++")
    case '3':
        print("Python")
    case '4':
        print("Java")
    case '5':
        print("php")
    case _:
        print("Invalid choice")
