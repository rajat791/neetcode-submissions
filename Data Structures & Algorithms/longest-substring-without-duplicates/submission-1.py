class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        if len(s) == 0:
            return 0
                
        # left = 0
        # right = 1
        substring = ""
        max_length = 0
        # substring += s[left:right]

        # while left <= right:

        for char in s:
            if char not in substring:
                substring += char
            else:
                while char in substring:
                    substring = substring[1:]
                substring += char
            max_length = max(max_length, len(substring))
        
        return max_length

#s="abcabcbb"




