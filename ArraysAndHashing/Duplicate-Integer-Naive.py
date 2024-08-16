class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set() #a set made to input numbers seen in array

        for num in nums:
            if num in seen:
                return True #If the number is in the seen setm then the value appears more than once.
            else:
                seen.add(num) #Else we add the number to the set and iterate.

        return False #If set is iterated through and we haven't seen a duplicate integer, return False.

#Time Complexity: O(n), as we literate through the array using one for loop, going through every integer until we find a duplicate array in the set. Worst Case is that we don't find a duplicate and we've iterated through the entire array, hence it being O(n).

#Space Complexity: O(n)
