class Solution:
    def reverseBits(self, n: int) -> int:
        binary = ""

        val = n
        while val != 0:
            mod = val % 2
            binary += str(mod)
            val = val // 2

        diff = 32 - len(binary)

        while diff != 0:
            binary += "0"
            diff -= 1

        return (int(binary, 2))

        