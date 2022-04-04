class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        min_word = min(strs, key = len)
        len_min_word = len(min_word)
        
        for _ in range(len_min_word):
            prefix = min_word[:len_min_word - _]
            counter = 0
            for word in strs:
                if word[:len_min_word - _] == prefix:
                    counter += 1
                else:
                    break
            if counter == len(strs):
                return prefix
        return ""