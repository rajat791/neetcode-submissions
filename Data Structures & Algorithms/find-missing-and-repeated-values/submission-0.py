class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        
        dict = {}

        for n in range(1, (len(grid)**2) + 1):
            dict[n] = 0

        a = 0
        b = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                val = grid[i][j]
                count = dict[val]
                if count == 0:
                    dict[val] = count + 1
                else:
                    a = val
        

        for d in dict:
            count = dict[d]
            if count == 0:
                b = d
            else:
                continue
        
        


                
                
                

        return [a,b]
        