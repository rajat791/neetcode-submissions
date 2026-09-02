class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        sorted_nums = sorted(enumerate(position), key=lambda x: x[1])
        # need to use a monotonic decreasing stack
        for tup in sorted_nums:
            index = tup[0]
            remaining = (target - position[index]) / speed[index]
            if not stack:
                stack.append(remaining)
            else:
                while len(stack) > 0 and remaining >= stack[-1]:
                    stack.pop(-1)
                stack.append(remaining)

        
        return len(stack)

        