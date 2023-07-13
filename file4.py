file=open("Myfile3.txt","w")
for i in range(3):
    name=input("Enter name of student :")
    rollno=int(input("Enter roll number :"))
    per=eval(input("Ener percentage :"))
    data=name + "\t" + str(rollno) + "\t" +str(per) +"\n"
    file.write(data)

file.close()
