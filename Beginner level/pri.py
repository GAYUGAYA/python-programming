a=int(input("Enter number: "))
x=0
for i in range(2,a//2+1):
    if(a%i==0):
        x=k+1
if(x<=0):
    print("Number is prime")
else:
    print("Number isn't prime")

