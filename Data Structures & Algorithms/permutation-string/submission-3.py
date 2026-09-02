class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        flag = False
        for l in range(0,len(s2) - len(s1) + 1):
            r = l + len(s1) - 1
            substring = s2[l:r + 1]
            result = ''.join(sorted(substring))
            s1_sorted = ''.join(sorted(s1))
            print(result)
            if result == s1_sorted:
                return True
        
        return flag

        