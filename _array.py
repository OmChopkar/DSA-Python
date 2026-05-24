'''
Array: Multiple values in single variable; Homogeneous
Collection of finite number of homo elements. 
Homo elements means if defined as int -> accepts only int.
stored in continuous memory location
'''
# #Find Biggest Number in Array
# def findBiggestNumber(sampleArray):
#     biggestNumber = sampleArray[0] #O(1)
#     for index in range(1,len(sampleArray)): #O(n)
#         if sampleArray[index]>biggestNumber: #O(1)
#             biggestNumber=sampleArray[index] #O(1)
#     print(biggestNumber) #O(1)
# sampleArray=[5,7,3,9,2] #O(1)
# findBiggestNumber(sampleArray) #O(1)
# #totalComplexity: O(n)

#----------------------------------------------------------------
# #Sum and Product of Array Elements
# def fun(array):
#     sum=0 #O(1)
#     product=1 #O(1)
#     for i in array: #O(n)
#         sum+=i  #O(1)
#     for i in array: #O(n)
#         product*=i #O(1)
#     print("Sum: "+str(sum)+", Product:"+str(product)) #O(1)

# array=[1,2,3,4,5] #O(1)
# fun(array) #O(1)
# #totalComplexity: O(n)

#----------------------------------------------------------------
# #ip = [1,2,3,4]
# #op = [24,12,8,6]
# ip = [1,2,3,4]
# op = []
# for i in range(len(ip)):
#     product=1
#     for j in range(len(ip)):
#         if i!=j:
#             product=product*ip[j]
#     op.append(product)
# print(op) #* removes [] and ,