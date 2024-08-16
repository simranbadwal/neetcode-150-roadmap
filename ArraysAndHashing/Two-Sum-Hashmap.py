class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {} #create hashmap for seen numbers in the list

        for index in range(len(nums)): #for each index in the nums list
            if target-nums[index] in seen: #if the complement number is in the seen hashmap
                return [seen[target-nums[index]],index] #return the indexes
            else: 
                seen[nums[index]] = index #else add the value and the index into the hashmap
        return []

# Time complexity: O(N) for iterating through the list
# Space Complexity: O(N); worse case of space being taken by nums hashmap.
