def twoSum(nums, target):
    prevMap = {} # Store differences in a dictionary

    for i, n in enumerate(nums): # Loop through array
        diff = target - n # The difference is what we need to find. 
        
        # If a difference is found in prevMap, then
        # then return result 
        if diff in prevMap:
            return [prevMap[diff], i]
        
        # If we reach here, that means that difference was not in prevMap. 
        # So we can put it in prevMap.
        prevMap[n] = i
