
def rotateLeft(self , arr, k):
    temp = [];
    for i in range(k):
        temp.append(arr[i])

    for j in range(len(arr)-k):
        arr[j] = arr[j+k]

    for l in range(len(arr)-k, len(arr)):
        arr[l] = temp[l-k-1]

    print(arr)
arr = [1,2,3,4,5,6,7];
k = 3
out = rotateLeft(self , arr, k)
print(out)