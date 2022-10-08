def shuffle(-1,1):
    a=len(-1)
    e=len(1)
    z=a+e
    for i in range(z):
        if(i<a):
            d.append(b[i])
        if(i<e):
            d.append(f[i])
    print("Shuffled list:",d)
a=int(input("Enter the number of elements of -1:"))
b=[]
d=[]
for i in range(a):
    c=int(input("Enter element:"))
    b.append(c)
e=int(input("Enter the number of elements of 1:"))
f=[]
for i in range(e):
    g=int(input("Enter element:"))
    f.append(g)
shuffle(b,f)

