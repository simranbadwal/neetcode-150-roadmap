class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t): #Default Param, if lengths of strings are not equal they are not anagrams
            return 0

        hashmap = {i: 0 for i in t} #create hashmap

        for i in s: #add values from s also, for edge case that the amount of the anagram letters are the same but there is another letter which is not accounted for in the hashmap.
            hashmap[i] = 0

        for letter in s: #For S string, for each letter add 1 to letter index.
            hashmap[letter] += 1 


        for letter in t: #For T string, for each letter minus 1 to letter index.
            hashmap[letter] -= 1


        for key, value in hashmap.items(): #compare, if not 0 return False else return True.
            if value != 0:
                return False
        return True

#Time Complexity, O(n), using for loops, it's O(5n), removing 5 as when we get to infinity it doesn't matter.
#Space Complexity, O(n)

