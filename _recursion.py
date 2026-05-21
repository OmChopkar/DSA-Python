'''
Recursion
When main problems can be divided into similar sub problems -> go for Recursuion
Recursion uses stack memory
Not memory efficient
'''
# def factorial(num):
#     if num<=0: #Base Condition
#         return 1
#     return num*factorial(num-1)
# print(factorial(4))

# def capitalizeFirst(arr):
#     result=[]
#     if len(arr)==0:
#         return result
#     result.append(arr[0][0].upper()+arr[0][1:])
#     return result + capitalizeFirst(arr[1:])
# print(capitalizeFirst(['car','taco','banana']))

# def power(base,exp):
#     if exp==0:
#         return 1
#     return base*power(base,exp-1)
# print(power(2,0))
# print(power(2,1))
# print(power(2,2))
# print(power(2,3))

# def productOfArray(arr):
#     if len(arr)==0:
#         return 1
#     return arr[0]*productOfArray(arr[1:])
# print(productOfArray([1,2,3]))
# print(productOfArray([1,2,3,4]))

# def reverse(string):
#     if len(string)<=1:
#         return string
#     return string[len(string)-1]+reverse(string[0:len(string)-1])
# print(reverse("Python"))

# def recursiveRange(num):
#     if num<=0:
#         return 0
#     return num + recursiveRange(num-1)
# print(recursiveRange(6))

# def isPalindrome(string):
#     if len(string)==0:
#         return True
#     if string[0]!=string[len(string)-1]:
#         return False
#     return isPalindrome(string[1:-1])
# print(isPalindrome("racecar"))
# print(isPalindrome("hello"))

# def someRecursive(arr,cb):
#     if len(arr)==0:
#         return False
#     if not(cb(arr[0])):
#         return someRecursive(arr[1:],cb)
#     return True

# def isOdd(num):
#     if num%2==0:
#         return False
#     else:
#         return True

# print(someRecursive([1,2,3,4],isOdd))
# print(someRecursive([4,6,8,9],isOdd))
# print(someRecursive([4,6,8],isOdd))