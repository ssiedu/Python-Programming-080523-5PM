file=open("Myfile4.txt","r")
while str:
    str=file.readlines()
    print(str)

file.close()
