# a=[1,3,4,7,2]
# target=int(input("Enter target value to search:"))
# for i in range(len(a)):
#     if a[i]==target:
#         print("Target Found at index",i)

# def linearSearch(array,target):
#     for i in range(0,len(array)):
#         if array[i] == target:
#             return i 
#     return -1

# array=[1,4,2,5,7]
# target=9
# result=linearSearch(array,target)
# if result==-1:
#     print("Target value not found")
# else:
#     print("Element found at index",result)

#---------------------------------------------------------------------
# def binarySearch(array,target):
#     low=0
#     high=len(array)-1
#     while low<=high:
#         mid=(low+high)//2
#         if target==array[mid]:
#             return mid 
#         elif array[mid]<target:
#             low=mid+1
#         else:
#             high=mid-1
#     return -1

# array=[2,4,5,9,11,13,14,15,19,20,22,23,27,30,32,39,42,44,45,49,51,53,54,55,59,60,62,63,67,70,72,79]
# target=72
# result=binarySearch(array,target)
# if result==-1:
#     print("Not Found")
# else:
#     print(f"Target {target} found at index {result}")