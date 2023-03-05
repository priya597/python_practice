
def solve(self, A):
    
    i = 0
    j = 0
    while i < len(A):
        if A[i] != 0:
            A[i],A[j] = A[j], A[i]
            

n = [0,3,4,5,2,1,0,4,0,0,0]
print(getProduct(n))