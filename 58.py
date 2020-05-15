import math

def add(a,b):
  'This adds 2 numbers'
  print "Sum of a and b is",a+b
    
def diff(a,b):
  'This finds the difference between 2 nos'
  print "Difference of a and b is",a-b
    
def multiply(a,b):
  'This multiplies 2 nos'
  print "Multiplication of a and b is",a*b

def div(a,b):
  'This divides 2 nos'
  print "Division of a and  b is",a/b
    
def sqroot(a):
    print "Square root of the number",a,"is", math.sqrt(a)
    
def floor_div(a,b):
    print "Floor division of a and b is", a//b
    
def fib(nterms):
  "This generates a fibonacci series"
  a=0
  b=1
  if nterms<=0:
    print("please enter positive number")
  elif nterms==1:
    print("Fibonacci series:",a)
  elif nterms==2:
    print a
    print b
  else:
    print a
    print b
    while(nterms>2):
      numnext=a+b
      print numnext
      a=b
      b=numnext
      nterms=nterms-1
n=int(input("Enter the no of terms"))
fib(n)

def isprime(num):
    for i in range(2,):
        if num%i==0:
            print num,"not prime"
            break
        else:
            print num,"is prime"
            break
number=int(raw_input())        
isprime(number)        

#math.py
from calc import*
add(4,5)
diff(34,12)
multiply(5,7)
div(6,2)
sqroot(9)
floor_div(33,5)
fib(8)
isprime(443)