def twoSum(nums, target):
    // prevMap stores previously seen differences
    prevMap = {}

    for i, n in enumerate(nums):
        diff = target - n
        
        // if a difference is found in prevMap, then immediately return result
        if diff in prevMap:
            return [prevMap[diff], i]
        // if we reach here, that means that difference was not in prevMap. So we can put it in prevMap. 
        prevMap[n] = i
