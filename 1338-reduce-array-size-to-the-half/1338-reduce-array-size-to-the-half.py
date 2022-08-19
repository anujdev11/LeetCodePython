class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        frequency = {}
        
        half_length = len(arr)//2
        
        frequency = Counter(arr)
                
        number_frequency = sorted(frequency.values(), reverse=True)
        
        ans=0
        
        while half_length>0:
            half_length-=number_frequency[ans]
            ans+=1
        return ans 
        
            
        