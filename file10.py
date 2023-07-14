import pickle
f=open("Myfile7","wb")
l1=[11,22,33,44,55]
pickle.dump(l1,f)
f.close()

f=open("Myfile7","rb")
data=pickle.load(f)
f.close()
print(data)
