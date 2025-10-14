class Solution:
    def isPalindrome(self, s: str) -> bool:
        i = 0
        j = len(s) - 1
        while i <= j: #we're not doing i!=j because for odd length strings, the middle element would be skipped
            if not s[i].isalnum(): #if the character isn't alphanumeric, it's skipped
                i = i+1
            elif not s[j].isalnum():
                j = j-1

            elif s[i].lower() == s[j].lower():
                i = i+1
                j = j-1

            else:
                return False
        return True

