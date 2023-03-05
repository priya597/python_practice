
def plusOne(self, digits: [0]):
    if not digits:
        return digits
    leng = len(digits)
    if len(digits) > 1 and len(digits) > 0:
        last_num = digits[-1] + 1
        digits[-1] = last_num
    else:
        digits = [1, 0]
    return digits


truckSize = [0]
unitcount = plusOne('self', truckSize)
print(unitcount)
