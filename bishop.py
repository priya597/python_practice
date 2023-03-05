
def solve(self, A, B):

    topLeft = min(A, B) - 1

    # Count bottom right squares
    bottomRight = 8 - max(A, B)

    # Count top right squares
    topRight = min(A, 9-B) -1

    # Count bottom left squares
    bottomLeft = 8 - max(A, 9-B)


    # Return total count
    return (topLeft + topRight + bottomRight + bottomLeft)


out = solve('self', 4, 4)
print(out)