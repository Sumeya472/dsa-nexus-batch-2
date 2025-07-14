class Solution:
    def similarPairs(self, words: List[str]) -> int:
        char_sets = [frozenset(word) for word in words]
    
        set_counter = {}
        for char_set in char_sets:
            set_counter[char_set] = set_counter.get(char_set, 0) + 1
        

        pair_count = 0
        for count in set_counter.values():
            if count > 1:
                pair_count += count * (count - 1) // 2
                
        return pair_count
