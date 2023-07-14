import pickle
class Student:
    def __init__(self,rno=0,name=" "):
        self.rno=rno
        self.name=name
        self.s1,self.s2,self.s3=0.0,0.0,0.0
    def getMarks(self):
        print("Enter marks of Student :")
        self.s1=eval(input("Enter marks of subject1 :"))
        self.s2=eval(input("Enter marks of subject2 :"))
        self.s3=eval(input("Enter marks of subject3 :"))
    def display(self):
        print("Student Information :")
        print("Roll Number :", self.rno)
        print("Name        :", self.name)
        print("Subject 1   :", self.s1)
        print("Subject 2   :", self.s2)
        print("Subject 3   :", self.s3)

'''S1=Student(101,"Ram")
S2=Student(102,"Shyam")
S1.getMarks()
S2.getMarks()
file=open("Student_Record","wb")
pickle.dump(S1,file)
pickle.dump(S2,file)
file.close()'''

file=open("Student_Record","rb")
try:
    while True:
        S=pickle.load(file)
        S.display()
except:
    file.close()

























