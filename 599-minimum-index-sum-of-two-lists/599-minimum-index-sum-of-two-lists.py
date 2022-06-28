class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        hashMap = {}
        res=[]
        for i in range(0,len(list1)):
            for j in range(0, len(list2)):
                if list1[i] == list2[j]:
                    hashMap[list1[i]] = i+j    
        min_value = min(hashMap.values())
        ans = {key:value for key, value in hashMap.items() if value == min_value}
        res = ans.keys()
        return res