# #Bubble Sort
# def bubbleSort(array):
#     for i in range(len(array)-1):
#         for j in range(len(array)-i-1):
#             if(array[j]>array[j+1]):
#                 temp=array[j]
#                 array[j]=array[j+1]
#                 array[j+1]=temp 
#             print(array)
#         print()
# array=[64,34,25,12,22,11,30]
# bubbleSort(array)

# #Insertion Sort
# def insertionSort(array):
    # for i in range(1,len(array)):
    #     key=array[i]
    #     j=i-1
    #     while j>=0 and array[j]>key:
    #         array[j+1]=array[j]
    #         j-=1
    #     array[j+1]=key
    # print(array)
#         # print()
# array=[5,3,6,8,2]
# print("Original Array:",array)
# insertionSort(array)

# #Selection Sort
# def selectionSort(array):
    # for i in range(len(array)):
    #     min=i
    #     j=i+1
    #     while j<len(array):
    #         if array[j]<array[min]:
    #             min=j
    #         j+=1 
    #         #array[i],array[min]=array[min],array[i]
    #         temp=array[i]
    #         array[i]=array[min]
    #         array[min]=temp
    #     print(array)
# array=[20,12,10,15,2]
# print("Original Array:",array)
# selectionSort(array)