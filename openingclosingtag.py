# Questions :
# Write a program that takes a string as input
# This string only has opening tags (<) and closing tags (>)
# Program should validate all opening tags are properly closed
# Program should validate all closing tags have an opening tag associated to them

def validateTags(arr):
    newlist = []

    for tag in arr:
        if tag == '<':
            newlist.append(tag)
           
        elif tag == '>':
        
            if not newlist:
                return False
            newlist.pop()

    return len(newlist) == 0

test_cases = [ "<<>>",  "<<><>>",  "<>><>>",  "<<<<<<<", "<<<>>>",  "<<>><",  "><" ] #input

for test_case in test_cases:
    result = validateTags(test_case)
    print(f'"{test_case}" => {result}')


# Output :

# "<<>>" => True
# "<<><>>" => True
# "<>><>>" => False
# "<<<<<<<" => False
# "<<<>>>" => True
# "<<>><" => False
# "><" => False