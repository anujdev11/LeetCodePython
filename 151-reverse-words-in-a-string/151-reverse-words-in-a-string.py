class Solution:
    def reverseWords(self, s: str) -> str:
        res = []
        s = s.strip()
        words = s.split(" ")
        words = [x for x in words if x]
        for i in reversed(words):
            res.append(i)
        return " ".join(res)
            
        