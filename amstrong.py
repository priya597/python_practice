
def solve(self, A):
    # Changed num variable to string, 
    # and calculated the length (number of digits)
    order = len(str(A))

    # initialize sum
    sum = 0

    # find the sum of the cube of each digit
    temp = A
    while temp > 0:
        digit = temp % 10
        sum += digit ** order
        temp //= 10

    # display the result
    if A == sum:
        print(A,"is an Armstrong number")
    else:
        print(A,"is not an Armstrong number")


out = solve('self', 3712)
print(out)