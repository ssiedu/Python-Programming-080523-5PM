list1=[]
file=open("Myfile5.txt","w")
for i in range(5):
    n=int(input("Enter Number :"))
    list1.append(n)

print(list1)
file.writelines(list1)
file.close()
