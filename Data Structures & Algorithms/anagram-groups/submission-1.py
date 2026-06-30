class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen = defaultdict(list)

        for s in strs:
            ordered = ''.join(sorted(s))
            if ordered in seen:
                seen[ordered].append(s)
            else: 
                seen[ordered] = [s]
        
        return list(seen.values())
        


        