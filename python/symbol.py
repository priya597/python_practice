
def isValid(self, s: str) -> bool:

    leftsymbol = []
    for c in s:
        if c in ['(', '[', '{']:
            leftsymbol.append(c)

        elif c == ')' and len(leftsymbol) != 0 and leftsymbol[-1] == '(':
            leftsymbol.pop()
        elif c == ']' and len(leftsymbol) != 0 and leftsymbol[-1] == '[':
            leftsymbol.pop()
        elif c == '}' and len(leftsymbol) != 0 and leftsymbol[-1] == '{':
            leftsymbol.pop()
        else:
            return False
    return leftsymbol == []


truckSize = '{[]}'
unitcount = isValid('self', truckSize)
print(unitcount)
