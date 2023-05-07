def twoSum(nums, target):
    # Store differences in a dictionary
    prevMap = {}

    # Loop through array
    for i, n in enumerate(nums):
        # Calculate target - current. This is the difference
        diff = target - n
        
        # If a difference is found in prevMap, then
        # then return result 
        if diff in prevMap:
            return [prevMap[diff], i]
        
        # If we reach here, that means that difference was not in prevMap. 
        # So we can put it in prevMap.
        prevMap[n] = i
