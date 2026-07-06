class Solution:


    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams={}

        for s in strs:
            canon= "".join(sorted(s))

            if canon not in anagrams:
                anagrams[canon] = []
            
            anagrams[canon].append(s)

        return list(anagrams.values())
            
            
        