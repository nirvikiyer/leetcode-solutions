class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        result = ""
        zipstrs = zip(*strs)
        for char in zipstrs:
            if len(set(char)) == 1:
                result += char[0]
            else:
                break
        return result
