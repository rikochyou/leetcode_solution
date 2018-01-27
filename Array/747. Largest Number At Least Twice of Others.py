def dominantIndex(self,nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    Max=max(nums)
    #print('Max=',Max)
    for value in nums:
        if  value != Max and Max< value * 2:
            return -1
    return nums.index(Max)


#nums = [0,0,2,3]
#print(dominantIndex(nums))
