class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        res = []
        hashMap = {}
        
        for i in range(0,len(strs)):
            sortedWord = ''.join(sorted(strs[i]))
            if sortedWord not in hashMap:
                hashMap[sortedWord] = [strs[i]]
            else:
                hashMap[sortedWord].append(strs[i])
                
        for j in hashMap.values():
            res.append(j)
        
        return res
                
                
        