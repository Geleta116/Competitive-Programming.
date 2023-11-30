class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        anag_dict = defaultdict(list)
        
        for word in strs:
            anag_dict["".join(sorted(word))].append(word)
        
        output = []
        for key in anag_dict:
            output.append(anag_dict[key])
            
        return output
        