# Task-7

# Functions
## Functions in python:
A function is a block of code which only runs when it is called.

You can pass data, known as parameters, into a function.

A function can return data as a result.
## Class method VS static method in python:
### Class method:
We use @classmethod decorator in python to create a class method.

A class method can access or modify the class state.

A class method takes cls as the first parameter.
### Static method:
we use @staticmethod decorator to create a static method in python.

A static method can’t access or modify it.

A static method needs no specific parameters.

## Write an empty function in python-pass statement:
In Python, to write empty functions, we use pass statement. pass is a special statement in Python that does nothing. It only works as a dummy statement. 
## Yield instead of Return:
### Return:
"return" is used to return a final result and terminate the function.
### Yield:
"yield" is used to create a generator that can produce multiple values.
## Return multiple values:
In Python, you can return multiple values by simply separating them with commas in the return statement. In Python, comma-separated values are treated as tuples, even without parentheses.
## Partial function in python:
In Python, a partial function is a function that is derived from an existing function by fixing some of its arguments.Python provides a built-in module called functools  that can be used to create partial functions. 
## First class function in python:
When you assign the whole funtion to any variable.then those variable perform like the assigning function.
## Precision handling:
Python allows to handle precision of floating point numbers in several ways using different functions under the "math" module. 
## *args and **kwargs:
### *args:
*args allows you to do is take in more arguments than the number of formal arguments that you previously defined.
### **kwargs:
**kwargs is a variable number of keyworded arguments that can be passed to a function that can perform dictionary operations.
## Python closures:
A Closure in Python is a function object that remembers values in enclosing scopes even if they are not present in memory. 
## Function decorators:
A decorator is a function that takes another function and extends the behavior of the latter function without explicitly modifying it. 
## Decorators in python:
In Decorators you can add extra features in the existing function.

By decorators we change the behaviour of existing function.
## Memorization using decorators in python:
Memorization is technique which hold the previous result so,that it can be used to avoid the repeated calculations and speed up the programs. It can be used to optimize the programs that use recursion. In Python, memoization can be done with the help of function decorators.
