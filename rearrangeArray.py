# def rearrangeArrayAlternatively(a, n):
#     # initializing output array of size-n
#     output = []

#     # initializing the pointers
#     i = 0
#     j = n - 1

#     # appending the data into the output list or array until i<= j
#     while i < j:
#         # inserting the current greatest element and the current smallest element
#         output.append(a[j])
#         output.append(a[i])

#         # moving pointers of the input array.
#         j = j - 1
#         i = i + 1

#     for i in range(len(output)):
#         print(output[i], end="  ")


def arrange(self, A):
        k = 0
        i = 0
        j = len(A)-1
        while i < j:
            
            temp = A[i]
            A[k] =  A[j]
            A.insert(A[k+1], temp)
            
            k += 2
            j -= 1
            i += 1
            
        print(A) 
        
if __name__ == "__main__":
    a = [1, 2, 3, 4, 5, 6]

    print("Array formed after alternative rearrangement is: ")
    arrange('self', a)