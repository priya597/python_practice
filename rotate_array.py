def reverse(arr, low, high):
    while(low < high):
        arr[high] = arr[low]
        arr[low] = arr[high]
       
        low += 1
        high -= 1

def rotate(n, k, t):
    reverse(n, 0, t-k-1)
    reverse(n, t-k, t-1)
    reverse(n, 0, t-1)

nums = [1,2,3,4,5,6,7]
target = 3
print(rotate(nums, target, len(nums)))