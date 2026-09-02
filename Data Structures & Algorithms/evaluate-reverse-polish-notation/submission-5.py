class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        int_stack = []
        operators = ['+', '-', '*', '/']

        for token in tokens:

            if token not in operators:
                int_stack.append(int(token))

            else:
                operand_one = int_stack.pop()
                operand_two = int_stack.pop()

                if token == '+':
                    result = operand_two + operand_one

                elif token == '-':
                    result = operand_two - operand_one

                elif token == '*':
                    result = operand_two * operand_one

                else:
                    result = int(operand_two / operand_one)

                int_stack.append(result)

        return int_stack[-1]