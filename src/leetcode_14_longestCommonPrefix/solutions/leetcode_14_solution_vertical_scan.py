class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        longest_common_prefix = ""
        
        for i, char in enumerate(strs[0]):
            for s in strs[1:]:
                if i >= len(s) or s[i] != char:
                    return longest_common_prefix
            longest_common_prefix += char

        return longest_common_prefix