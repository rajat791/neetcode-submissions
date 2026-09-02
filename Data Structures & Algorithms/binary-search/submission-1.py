class Solution:
    def search(self, nums: List[int], target: int) -> int:

        def recursive(left, right):
            if left > right:
                return -1

            mid = (left + right) // 2

            if nums[mid] == target:
                return mid

            elif target > nums[mid]:
                return recursive(mid + 1, right)

            else:
                return recursive(left, mid - 1)

        return recursive(0, len(nums) - 1)