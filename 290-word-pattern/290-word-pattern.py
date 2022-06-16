class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        
        patternMap = dict()
        stringMap = dict()

        stringList = s.split(" ")
        if len(stringList) != len(pattern):
            return False


        for char, word in zip(pattern, stringList):
            if char in patternMap and patternMap[char] != word:
                return False
            if word in stringMap and stringMap[word] != char:
                return False

            patternMap[char] = word
            stringMap[word] = char

        return True