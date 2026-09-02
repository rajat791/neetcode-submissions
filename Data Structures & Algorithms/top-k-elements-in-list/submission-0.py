class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums_dict = {}

        for num in nums:
            if num in nums_dict:
                count = nums_dict[num]
                count+=1
                nums_dict[num] = count
            else:
                nums_dict[num] = 1
        
        sorted_nums_dict = sorted(nums_dict, key=lambda num :           nums_dict[num], reverse=True)

        print(sorted_nums_dict)

        return sorted_nums_dict[0:k]
        