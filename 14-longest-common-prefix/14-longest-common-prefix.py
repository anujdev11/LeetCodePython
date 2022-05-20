class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        if len(strs)==0:
            return ""
        if len(strs)==1:
            return strs[0]
        if strs[0]=="":
            return strs[0]
        
        minLengthString=len(strs[0])
        
        for i in range(len(strs)):
            minLengthString = min(len(strs[i]),minLengthString)
        
        lsp=""
        
        for i in range(minLengthString):
            character = strs[0][i]
            for j in range(1,len(strs)):
                if strs[j][i] != character:
                    return lsp
            lsp+=character
        return lsp
                
                    
                            
                
            
            
        