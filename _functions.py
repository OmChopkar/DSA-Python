'''
functions: self contained block used to perform statements
Types: Predefined and User defined
Advantages: Modularity, Reusability

functions are called by name
methods are called using objects
'''
# def hello():
#     print("Hello World!") 
# hello()

# #It is possible to return multiple values in python
# #use print() when calling for output
# def arithmatic():
#     a=int(input("Enter value of a:"))
#     b=int(input("Enter value of b:"))
#     sum=a+b 
#     sub=a-b 
#     mult=a*b 
#     div=a/b
#     return sum, sub, mult, div #Returns in tuple because values fixed, wont change
# print(arithmatic())
# # result=arithmatic()
# # print(result) #tuple

#How many types of arg we pass in functions?
#1. Positional arg
#2. keyword arg
#3. Default arg
#4. Variable length arg / variable number of arg

# def arithmatic(a,b):
#     sum=a+b 
#     sub=a-b 
#     mult=a*b 
#     div=a/b
#     return sum, sub, mult, div #Returns in tuple because values fixed, wont change
# # #Positional arg: position fixed from left to right
# result=arithmatic(5,5)
# print("Arithmatic: ",result)

# # #Keyword arg: position not necessary
# def credentials(username,password):
#     if username==password:
#         print("Login Successfully.")
#     else:
#         print("Invalid Credentials.")
# credentials(password="admin",username="admin") #Keyword and parameter names must be same

# #Default arg
# def cityName(city="Pune"):
#     print(city)
# cityName("Nagpur")
# cityName("Mumbai")
# cityName() #When not passed, takes arg value given in the header

# #Variable length arg / variable number of arg
# def cityName(*name):
#     print(name)
# cityName("Nagpur","Mumbai","Pune","chennai") #Printed as tuple

# #modularity approach in function
# import sys
# def add():
#     a=int(input("Enter value of a: "))
#     b=int(input("Enter value of b: "))
#     print(a+b)

# def sub():
#     a=int(input("Enter value of a: "))
#     b=int(input("Enter value of b: "))
#     print(a-b)

# def div():
#     a=int(input("Enter value of a: "))
#     b=int(input("Enter value of b: "))
#     print(a/b)

# def mult():
#     a=int(input("Enter value of a: "))
#     b=int(input("Enter value of b: "))
#     print(a*b)

# while True:
#     print("\n---Arithmatic Operations---")
#     print("1. Addition")
#     print("2. Subtraction")
#     print("3. Multiplication")
#     print("4. Division")
#     print("5. Exit")
#     print()
#     ch=int(input("Enter your choice: "))
#     if ch==1:
#         add()
#     elif ch==2:
#         sub()
#     elif ch==3:
#         mult()
#     elif ch==4:
#         div()
#     elif ch==5:
#         sys.exit()
#     else: 
#         print("Please Enter Correct Menu Option.")

# #Factorial
# N=int(input())
# f=1
# for i in range(1,N+1):
#     f*=i
# print(f)

# def factorial(N):
#     f=1
#     for i in range(1,N+1):
#         f*=i
#     print(f)

# N=int(input())
# factorial(N)

# def func(value,values):
#     var=1
#     values[0]=44
# t=3
# v=[1,2,3]
# func(t,v)
# print(t,v[0]) #3 44

# def f(i,values=[]):
#     values.append(i)
#     print(values)
# f(1)
# f(2)
# f(3)