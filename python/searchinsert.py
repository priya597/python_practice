
def searchInsert(self, nums, target: int) -> int:
    for i in range(len(nums)):
        if nums[i] == target:
            return i
        if nums[i] > target:
            # If nums[i] is greater, this means that target should be in nums[i]
            return i
        if target < nums[0]:
            return 0
        if target > nums[len(nums)-1]:
            return len(nums)


truckSize = [1, 3, 5, 6]
target = 7
unitcount = searchInsert('self', truckSize, target)
print(unitcount)
