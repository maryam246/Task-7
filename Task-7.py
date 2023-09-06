# Example of Python Functions:
# In Python a function is defined using the def keyword
def meet():
    print("hello",end=" ")
    print("Aliana")
  
meet()

def add(x,y):
    c =x+y
    return c
Result=add(5,8)
print(Result)

def mul_sub(a,b):
    m =a*b
    s =a-b
    return m,s
r1,r2 =mul_sub(9,4)
print(r1,r2)

def name(n):
    print("My name is: "+ n + " Khan")
    
name("Maryam")
name("Anam")
name("Kiran")

# Example of Class method VS static method in python:

class student:
    grade = 5
    #constructor creating
    def __init__(self,name,age):
        self.name =name
        self.age =age 
    
    def get_info(self):
        print({"name": self.name, "age": self.age, "grade":self.grade})
        
    @classmethod    # Use Class method
    def update_grade(cls,grade):
        cls.grade=grade
        
  
    @staticmethod          # Use static method
    def check_age(age):
        if age>18:
            print("Above 18")
        else:
            print("Below 18")
    
    #object creating
s1 =student("Amir",17)
s2 =student("Areeb",22)

student.update_grade(4)
student.check_age(22) #in static method object is not needed for output

s1.get_info()
s2.get_info()

# Example of Write an empty function in python-pass statement:

def num(x,y):
    if x>y:
        pass
    else:
        print("False")
        
num(7,9)

def fruit(x):
    if x=="orange":
       pass
    else:
       print("not present")
       
       
fruit("grapes")


# Example of Yield instead of Return:
# function use with return keyword:
l =[1,2,3,4,5]
def get_sq(l):
    new_l=[]
    for i in l:
        new_l.append(i**2)
    return new_l
r = get_sq(l)
print(r)

# function use with yield keyword:
l =[3,5,6,7]
def get(l):
    for i in l:
        yield i
r =get(l)
print(list(r))

# Another yield example:

l =[1,2,3,4,5]
def get_sq(l):
    for i in l:
        yield i**2
r = get_sq(l)
for i in r:
    print(list(r))
    
    
# Example of Return multiple values:
def num():
    return 1,2,3,4,5 # it returns multiple value
 
r =num()
print(r) # BYdefault it give tuple answer

#Example of Partial function in python:
from functools import partial
def num(a,b,c):
    print(a+b+c)

n = partial(num,2)
n(3,4)


#Example of First class function in python:
def add(x,y):
    return x+y

var =add
print(var(3,6))

#Example of Precision handling:
f =22.34563
print(f)
from math import *

print(trunc(f)) # eliminate the decimal points

print(ceil(f)) # print least integer > given number

print(floor(f)) #print gretest integer < given number

print(round(9.3332,3))

print("%.3f"%f) # work same as round


#Example of *args and **kwargs:

# example of *args:




# example of**kwargs:
def name(**kwargs):
    for key,value in kwargs.items():
    print(key,value)
    
dic ={1:"maryam",2:"ali",3:"faiza"}
name(**dic)
#Example of Memorization using decorators in python:
# Simple recursive program to find factorial
def factorial(num):
	if num == 1:
		return 1
	else:
		return num * factorial(num-1)
		

print(factorial(1))
print(factorial(5)) # again performing same calculation
print(factorial(5))
