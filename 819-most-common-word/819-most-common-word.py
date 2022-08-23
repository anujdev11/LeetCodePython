class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:

        count ={}
        for c in "!?',;.":
            paragraph = paragraph.replace(c, " ")
        listOfWords = paragraph.split()
        
        bannedSet = set(banned)
        
        for word in listOfWords:
            word = word.lower()
            
            if word not in bannedSet:
                if word in count:
                    count[word]+=1
                else:
                    count[word]=1
        
        return max(count.items(), key=operator.itemgetter(1))[0]
            
            
       