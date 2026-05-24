# #Slicing
# name="OmDhanraj"
# print(name[0])
# print(name[-1])
# print(name[0:])
# print(name[:])
# print(name[:5])
# print(name[1:8:2])
# print(name[::-1])

# s="Python are High level programming Language"
# print(s.lower())
# print(s.upper())
# print(s.swapcase())
# print(s.title())
# print(s.capitalize())

# name="Om"
# age=21
# sal=2000
# print("My name is {} and I am {} yers old, earning {}".format(name,age,sal))
# print("My name is {0} and I am {1} yers old, earning {2}".format(name,age,sal))
# print("My name is {x} and I am {y} yers old, earning {z}".format(x=name,y=age,z=sal))
# print(f"My name is {name} age is {age} sal is {sal}")

# name="OmDhanraj"
# for i in name:
#     print(i)

# #WAP to remove duplicate
# name="OmDhanraj"
# newname=""
# #op= OmDhanrj
# for i in name:
#     if i not in newname:
#         newname+=i
# print(newname)

# #Reverse a string
# name='Om'
# rev=""
# N=len(name)
# #for i in range(N-1,-1,-1):
# for i in range(len(name)-1,-1,-1):
#     rev+=name[i]
# print(rev)

# #Palindrome
# s1=input("Enter String:")
# s2=""
# for i in range(len(s1)-1,-1,-1):
#     s2+=s1[i]
# print(s1)
# if s1==s2:
#     print("Palindrome String")
# else:
#     print("Not Palindrom String")

#-----------------------------------------------------------------
# #Anagram
# s1=input("Enter String 1: ")
# s2=input("Enter String 2: ")
# if (len(s1))==len(s2):
#     for i in s1:
#         if s1 in s2:
#             print("Anagram")
#         else:
#             print("Not Anagram")
# else:
#     print("Size of String is not Same.")

#-----------------------------------------------------------------
# #Count vowels and Consonants
# name=input("Enter Name:")
# vowels=['a','e','i','o','u']
# v=0
# c=0
# for i in name:
#     if i in vowels:
#         v+=1
#     else:
#         c+=1
# print("Consonant: ",c)
# print("Vowel: ",v)

#-----------------------------------------------------------------
# #Word Count
# name="My name is Om"
# s=1
# for i in name:
#     if i == " ":
#         s+=1
# print(s)

#-----------------------------------------------------------------
# a=50
# b=30
# c=20
# d=10
# print((a+b)*c/d) 
# print((a-b)*(c/d))
# print(a+(b*c)/d) 

# #Counting spl characters in String
# msg=input("Enter Message: ")
# count=0
# z=ord(i)
# print(i)
# for z in range(len(msg)-1):
#     if z>=65 and z<=90:
#         continue
#     elif z>=97 and z<=122 :
#         continue
#     elif z>=48 and z<=57:
#         continue   
#     else:
#         count+=1
# print(count)

#-----------------------------------------------------------------
# print('OmDhanraj22'.isalnum())
# print('OmDhanraj'.isalpha())
# print('22'.isdigit())
# print('omdhanraj'.isupper())
# print(''.istitle())
# print(' '.isspace())
# print(''.isalnum())
# print('Om Dhanraj'.istitle())
# print("Hello".startswith("He"))
# print("Hello".endswith("o"))
# print(' '.isdigit()) #empty string or space always False in isdigit isupper islower istitle etc

# print("Omdhanraj".find('j')) #if not found -1
# print("Omdhanraj".index('z')) #error if not in string
# print("Omdhanraj".count('a'))


#-----------------------------------------------------------------
#Input= "abababab"
#Output = 4
ip="abababab"
s="ab"
c=ip.count(s)
print(c)

#-----------------------------------------------------------------
# #INPUT= "Om**Dhanraj*Chopkar******"
# #OUTPUT= OmDhanrajChopkar*********
# s1="Om**Dhanraj*Chopkar******"
# s2=""
# s3=""
# for i in s1:
#     if i!='*':
#         s3+=i 
#     else:
#         s2+=i 
# print(s3+s2)


#-----------------------------------------------------------------
#Removing spaces from the string
#1. rstrip()=> removes right side spaces
#2. lstrip()=> removes left side spaces
#3. strip()=> removes  both side spaces

# city=input("Enter city:")
# scity=city.strip()
# if scity=='Hyderabad':
#     print("Adab")
# elif scity=='Chennai':
#     print("Vannakam")
# elif scity=='Banglore':
#     print("Shubodya")
# else:
#     print("Invalid City")

#-----------------------------------------------------------------
#INPUT="aabbbeeeffff"
#OUTPUT=a2b3e3f4
# name="abbbbeeeeeffggg"
# newname={}
# for i in range(len(name)):
#     key=name[i]
#     count=0
#     for j in range(len(name)):
#         if key==name[j]:
#             count+=1
#     newname[key]=count
# for i,j in newname.items():
#     print(i,j,sep='',end='')

'''
WAP to access each character of string in forward and backward direction by using while loop?
Forward Direction: L e a r n i n g   P y t h o n   i s   v e r y   e a s y 
Backward Direction: y s a e   y r e v   s i   n o h t y P   g n i n r a e L 
'''
# s=input("Enter String: ")
# n=len(s)
# i=0
# print("Forward Direction")
# while i<n:
#     print(s[i],end=' ')
#     i+=1
# print("\nBackward Direction")
# i=-1
# while i>=-n:
#     print(s[i],end=' ')
#     i-=1

#-----------------------------------------------------------------
# stringSent, stringRec = map(str, input().split()) 
# # print(stringSent)
# # print(stringRec)
# for i in stringSent:
#     if i not in stringRec:
#         print(i)