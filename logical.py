a=int(input("Enter First Number :"))#10
b=int(input("Enter Second Number :"))#20
print("And :", (a>b) and(a==b))#F
print("Or  :", (a<b) or (a==b))#T
print("Not :", not(a<b))#F
print("AND OR :", ((a>b) and (b<b))or(a!=b))#T
print("AND Not :", (not(a>b)) and (b==a))#F
print("OR Not : ", not((a>b)or (a!=b)))#F
print("AND or NOT :", not((a>b)and((b<a) or(a!=b))))#T
