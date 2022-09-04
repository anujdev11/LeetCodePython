class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        
        res=[]
        
        
        def DFS(n,num):
            if n == 0:
                return res.append(num)
            
            last_digit = num%10
            
            next_digits = set([last_digit+k,last_digit-k])
            
            for next_digit in next_digits:
                if 0 <= next_digit < 10:
                    new_num = num * 10 + next_digit
                    DFS(n-1, new_num)   
            
        
        for num in range(1,10):
            DFS(n-1,num)
        
        return res
        
        
        
        
#         for j in range(0,n):        
        # for l in range(1,10):
        #     for i in range(0,10):
        #         if abs(l-i)==k:
        #             num=str(l)+str(i)
        #             if len(num)!=n:
        #                 print(num[-1])
        
#         i=1
#         j=0
        
#         while True:
#             if abs(j-i) == k:
                
#                 if len(res)>=2:
#                     res= res + str(j)
#                 else:
#                     res = str(i)+str(j)
#                 i=j
#                 j=0 
#             else:
#                 j+=1
            
#             if j==10:
#                 i+=1
                
#             if len(res)==n:
#                 print(res)
#                 resArr.append(res)
#                 res=""
#                 i+=1
#                 j=0
#                 if i==10:
#                     break
        
        
        
        
            
            