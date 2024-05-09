arr = [5,10,2,3,11,13,19,12]

def selection(arr,size):
    temp = 0
    for i in range(size):
        small = i
        for j in range(i + 1,size):
            if arr[j] <= arr[small]:
                small = j
        temp = arr[i]
        arr[i] = arr[small]
        arr[small] = temp
        print(arr)
    return arr

print("Sorted Array")
print(selection(arr,len(arr)))



#....time complexity of O(n^2)
#....space complexity of O(1)
