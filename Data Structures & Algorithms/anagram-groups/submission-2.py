from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        anagram_map = defaultdict(list)
        
        for s in strs:
            # Array of 26 zeros for lowercase English letters
            count = [0] * 26
            for char in s:
                count[ord(char) - ord('a')] += 1
            
            # Convert to an immutable tuple to use as a dictionary key
            anagram_map[tuple(count)].append(s)
            
        return list(anagram_map.values())
        