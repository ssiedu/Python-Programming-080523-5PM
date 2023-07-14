import pickle
f=open("Myfile8","wb")
d1={1:"ssi",2:"Hello"}
pickle.dump(d1,f)
f.close()

f=open("Myfile8","rb")
data=pickle.load(f)
f.close()
print(data)
