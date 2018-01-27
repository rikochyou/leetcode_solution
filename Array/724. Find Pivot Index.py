def pivotIndex(nums):
    """
    :type nums: List[int]
    :rtype: int
    """


    left, right = 0, sum(nums)
    for index, num in enumerate(nums):
        right -= num
        if left == right:
            return index
        left += num
    return -1

#nums=[1, 2, 3]
#print(pivotIndex(nums))

"""Input: [1, 7, 3, 6, 5, 6]

index: 0, num: 1, left: 0, right: 27
index: 1, num: 7, left: 1, right: 20
index: 2, num: 3, left: 8, right: 17
index: 3, num: 6, left: 11, right: 11 <-- Found!!!"""
