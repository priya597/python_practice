class Solution:
    # @param A : list of integers
    # @return a list of integers
    def maxset( A):
        maxsum = 0;
        currsum = 0; 
        new = []
        for i in range(len(A)):
            
            currsum +=  A[i]
            if(currsum > maxsum):
                maxsum = currsum
                new.append(A[i])
            
            if(currsum < 0):
               currsum = 0 
               new = []
               
        return  maxsum if len(new) == 0 else new

    arr = [10, -1, 2, 3, -4, 100]
    out = maxset( arr)
    print(out)