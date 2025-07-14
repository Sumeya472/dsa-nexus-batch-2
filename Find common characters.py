class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        common = [0] * 26
        for char in words[0]:
            index = ord(char) - ord('a')
            common[index] += 1
        
        for word in words[1:]:
            freq = [0] * 26
            for char in word:
                index = ord(char) - ord('a')
                freq[index] += 1
            
            for i in range(26):
                common[i] = min(common[i], freq[i])
        
        result = []
        for i in range(26):
            char = chr(ord('a') + i)
            result.extend([char] * common[i])
        
        return result
