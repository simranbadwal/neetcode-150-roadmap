class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list) #Creating a Default Dict allows values that are filled in to default to lists, allow you to extract the values that are actually in there.

        for string in strs: #For each string in the list of strings
            countOfLetters = [0] * 26 #We create an array for each letter in the alphabet

            for letter in string: #and for each letter in the string
                countOfLetters[ord(letter)-ord('a')] += 1 #we add one for every instance of said letter, ord(letter)-ord('a') == 1,2,3,4... for a,b,c,d...

            result[tuple(countOfLetters)].append(string) #after each letter is counted we append the string to the key, which is the actual count of the letters so for example in the countOfLetters an example string like "abc" would be under the key like this 11100000000000000000000000 : ["abc"] (note: we turn the countOfLetters to a tuple because it is non-mutable(an object whose state cannot be modified after it is created), non mutable objects can be used as keys in dicts)
        
        return result.values() #after all the strings in the list is appended to the result, we extract the values that are not the defaultdict values inside of the dict

# Time Complexity: O(n*k) n = length of list k = length of longest string
