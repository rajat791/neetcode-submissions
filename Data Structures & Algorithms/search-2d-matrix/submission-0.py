class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        if not matrix:
            return False

        correct_row = 0

        for index, row in enumerate(matrix):
            if row[0] == target:
                return True
            elif row[0] < target:
                correct_row = index
            else:
                break

        nums = matrix[correct_row]

        def recursive(left, right):
            if left > right:
                return False

            mid = (left + right) // 2

            if nums[mid] == target:
                return True

            elif target > nums[mid]:
                return recursive(mid + 1, right)

            else:
                return recursive(left, mid - 1)

        return recursive(0, len(nums) - 1)
        





    