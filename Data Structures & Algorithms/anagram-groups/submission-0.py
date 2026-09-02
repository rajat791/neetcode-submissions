class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        output = {}
        for index, string in enumerate(strs):
            string_sorted = "".join(sorted(string))

            if string_sorted not in output:
                output[string_sorted] = [string]
            else:
                group = output.get(string_sorted)
                group.append(string)
                output[string_sorted] = group
        return list(output.values())




        