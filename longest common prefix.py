class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""

        prefix = []
        for i, char in enumerate(strs[0]):
            for s in strs[1:]:
                if i >= len(s) or s[i] != char:
                    return "".join(prefix)
            prefix.append(char)

        return "".join(prefix)        
