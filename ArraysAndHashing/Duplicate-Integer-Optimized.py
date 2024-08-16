class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        return len(set(nums)) != len(nums) 

#Explaining the Solution

#The list nums is converted to a set using set(nums). In Python, a set automatically removes any duplicate elements. For example, if nums = [1, 2, 3, 2], then set(nums) would be {1, 2, 3}. So when we check...
#The actual length of the set, if it's not equal to the length of the original list given to us, then we know that in the original array, there was a duplicate integer.

# Time Complexity, O(n), as we still need to convert the list into a set, which takes O(n) Time
# Space Complexity, O(n)
