x = int(input("uang muka: "))

a=0*x
b=0*x
c=0.1*x
d=0.1*x
e=0.5*x
f=0.5*x
g=0.5*x
h=0.2*x
y=[a,b,c,d,e,f,g,h]

for i in range (len(y)):
    print("laba bulan ke",i+1,"sebesar: ",y[i])

z= (a+b+c+d+e+f+g+h)
print("Total laba adalah: ",z)