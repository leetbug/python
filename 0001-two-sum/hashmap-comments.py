 
def twoSum(nums, target):
    prevMap = {} # stores differences (the number we need to find)

    for i, n in enumerate(nums): # Loop through array
        diff = target - n  # calculate difference needed
        
        # If previously calculated, we solved it. 
        if diff in prevMap:
            return [prevMap[diff], i]
        
        # We have not found it yet. So save in our dictionary.
        prevMap[n] = i
