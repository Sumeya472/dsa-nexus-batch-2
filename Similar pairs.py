from typing import List

def similar_pairs(words: List[str]) -> int:
    sets = [frozenset(word) for word in words]
    count = 0
    for i in range(len(sets)):
        for j in range(i + 1, len(sets)):
            if sets[i] == sets[j]:
                count += 1
    return count

if __name__ == "__main__":
    sample_words = ["abc", "bca", "cab", "xyz", "zyx", "ab"]
    print(similar_pairs(sample_words))
