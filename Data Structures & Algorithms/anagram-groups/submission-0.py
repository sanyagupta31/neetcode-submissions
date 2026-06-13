class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups:defaultdict=defaultdict(list)
        ans=[]
        for word in strs:
            sortedword=''.join(sorted(word))
            groups[sortedword].append(word)
        for group in groups.values():
            ans.append(group)
        return ans
