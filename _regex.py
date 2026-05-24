''''
To search a string / search pattern -> use regex

input -> bytecode 
Applications of Regular Expression:
- Develop digital circuit
- Develop compiler and interpreter
- Develop communication protocol like tcp
- Develop validation logic
- Develop pattern matching and searching application (like ctrl-f)

import re - re performs all regex based operations


[abc] either a b or c
[^abc] except a b c
[a-z]
[A-Z]
'''
# # Compile fn()
# import re 
# count=0
# pattern=re.compile("function") #strinng converts into bytecode
# # print(pattern)
# matcher=pattern.finditer("A function in python is defined by a def statement. The general syntax looks like this: def function-name(parameter list): statements, i.e., the function body. The parameter pytho list consists of none or more parameters")
# # print(matcher)
# for i in matcher:
#     count+=1
#     print(i.start(),"...",i.end(),"...",i.group())
# print("The number of occurences:",count)

# #without using compile fn()
# import re
# count=0
# matcher=re.finditer("hi","hihihihi") #re.finditer("pattern","sentences")
# for i in matcher:
#     count+=1
#     print(i.start(),"...",i.end(),"...",i.group())
# print("The number of occurences:",count)

# #user input
# import re
# obj=input("Enter any character:")
# objmatch=re.finditer(obj,"a7b @k9z")
# for match in objmatch:
#     print(match.start(),"...",match.end(),"...",match.group())

# #match() is used to match only the starting word only; if not found then None.
# import re
# a=input("Enter any string to perform match operations:")
# mtch=re.match(a,"python is a very important language")
# print(mtch)
# if mtch!=None:
#     print("Match found at begining level")
#     print(mtch.start(),"...",mtch.end())
# else:
#     print("There is no matching at begining level")

# #fullmatch() match full string to a given pattern
# import re
# a=input("Enter any string to perform match operations:")
# mtch=re.fullmatch(a,"hhaacckkeerrrraannkk")
# print(mtch)
# if mtch!=None:
#     print("Match found")
#     print(mtch.start(),"...",mtch.end())
# else:
#     print("Full match not found")

# import re
# s=input("Enter Mail ID:")
# m=re.fullmatch("\w[a-zA-Z0-9_.]*@gmail[.]com",s)
# if m!=None:
#     print("VALID!")
# else:
#     print("INVALID!")

# # #WAP to check valid mobine number
# import re
# mo=input("Enter Mobile Number:")
# obj=re.fullmatch("[0-9]\d{9}",mo)
# if obj!=None:
#     print("VALID!")
# else:
#     print("INVALID!")

# #search()
# import re
# a=input("Enter any string to perform match operations:")
# mtch=re.search(a,"python is a dynamic language")
# print(mtch)
# if mtch!=None:
#     print("Match found")
#     print(mtch.start(),"...",mtch.end())
# else:
#     print("Full match not found")

# #findall() - returns in list
# import re
# mtch=re.findall('[^A-Za-z]',"t6er5XCV!@3")
# print(mtch)

# #sub() substitue or replcaes
# #sub(expression,replacement,string)
# import re
# obj=re.sub('[A-Z]','*','2345 fcLP cHkG HOLL')
# print(obj)

# #subn () returns count of replacement along with substitute
# import re
# obj=re.subn('[A-Z]','*','2345 fcLP cHkG HOLL')
# print(obj)
# print("The string is:",obj[0])
# print("The number of replacement is:",obj[1])


# #Search in file
import re
f1=open("input.txt","r")
f2=open("output.txt","w")
for line in f1:
    list=re.findall("[A-Za-z ]",line)
    for n in list:
        f2.write(n)