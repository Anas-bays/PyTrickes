# we put the BublleSort method in a function
def bubbleSort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]


arr = [64, 20, 16, 90, 40, 10, 2] # try your exemple and see
bubbleSort(arr)

print("Storted Arrey is:")
for i in range (len(arr)):
    print("%d" %arr[i], end=" ")

'''
OutPut:
Sorted Arrey is:
2 10 16 20 40 64 90
'''

