
def wave(self, A):
    A.sort();
    for i in range(0, len(A)-1, 2):  
        temp = A[i]
        A[i] = A[i+1]
        A[i+1] = temp
       
    return A  

arr = [1, 2, 3, 4];
out = wave('self', arr)
print(out)