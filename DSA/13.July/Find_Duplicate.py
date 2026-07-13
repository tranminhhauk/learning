def find_duplicate(nums):
    slow = nums[0]
    fast = nums[0]
    while True:
        slow = nums[slow]
        fast = nums[nums[fast]]
        if slow == fast:
            break
    fast = nums[0]
    while slow != fast:
        slow = nums[slow]
        fast = nums[fast]
    return slow
        
nums1 = [3,1,3,4,2]
nums2 = [2,2,2,2,2]
nums3 = [1,4,6,7,1]
print(find_duplicate(nums1))
print(find_duplicate(nums2))  
print(find_duplicate(nums3))  

