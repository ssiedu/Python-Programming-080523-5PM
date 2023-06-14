ch=input("Enter any charcater :")
match ch.upper():
    case 'A'|'E'|'I'|'O'|'U':
        print("Vowel")
    case _:
        print("Consonant")
