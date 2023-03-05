# # Python3 program to reverse a string
# # s = input()
# s = "i like this program very much"
# words = s.split(' ')
# string = []
# for word in words:

#     print(word);
	
#     string.insert(0, word);


# print(" ".join(string))

# # Solution proposed bu Uttam


def reverseWords(s):

    # splitting the string
    s = s.split(" ")

    # initializing 2 pointers
    left = 0
    right = len(s) - 1

    # traversing till the left does not exceed the right pointer
    while left <= right:
    	# swap elements
        s[left], s[right] = s[right], s[left]

        # increment left and decrement right
        left += 1
        right -= 1

    s = " ".join(s)
    return s

s = 'I love Programming bottom of My Heart'
print(reverseWords(s))

