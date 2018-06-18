#Q1. function for calculating area of circle
def area():
    radius=float(input("enter the radius of circle"))
    area=3.14*radius*radius
    print(area)
area()

#Q2. print perfect number series between 1 to 100
def perfect(n) :
    sum=0
    for i in range(1,n) :
     if n%i==0 :
         sum=sum+i
    if sum==n :
         return True
    else :
         return False
for i in range(1,1000) :
 if perfect(i) :
    print(i)


#Q3 table of 12 by recursion
n=12
def table(n,x) :
    print(n*x)
    x=x+1
    if x<=10 :
        table(n,x)
table(n,1)

#Q4 calculate power of number
def power (a,b) :
     if b==1 :
         return a
     else :
         return a*power(a,b-1)
print(power(8,3))

#Q5. find factorial of number and store in dictionary
def factorial (n) :
    if n<=1 :
        return 1
    else :
        return (n*factorial(n-1))
n=int(input("enter the number n:"))
print("factorial :")
print(factorial(n))
a=factorial(n)
l="output"
d={}
d[l]=a
print(d)
        
