def searchInsert(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    low=0
    high=len(nums)-1
    mid=0
    while low<=high:
        print(low,high)
        mid=(low+high)//2
        print(mid)
        if target<nums[mid]:
            high=mid-1
        elif target>n
        ums[mid]:
            low=mid+1
        else:
            return mid
    return  low

print(searchInsert([1,3,5],0))