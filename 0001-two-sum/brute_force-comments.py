  
def twoSum(nums, target):
    # loop through the list and then another list
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[j] == target - nums[i]:
                return [i, j]
