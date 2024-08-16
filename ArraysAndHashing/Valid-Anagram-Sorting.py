class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
      #Turns Strings into a list ex. example -> [e,x,a,m,p,l,e]
      sList = list(s) 
      tList = list(t)
      #Sorts Lists into Alphabetical Order
      sList.sort()
      tList.sort()
      #Returns if the lists are the same (If they are it's an anagram, as anagram and nagaram, which are examples, turn into the lists of [a,a,a,g,m,n,r] and [a,a,a,g,m,n,r], which are the same.
      return sList == tList


# Time Complexity, O(n*log(n)), list(s) and list(t) both take O(n) time, and Sorting a list of length takes usually O(n*log(n)) time, as the word gets larger and larger, this method of sorting the list becomes increasingly unusuable.
# Space Complexity, O(n)
