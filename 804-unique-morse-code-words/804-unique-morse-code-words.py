class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
            codes = {"a": ".-", "b": "-...", "c": "-.-.", "d": "-..", "e": ".", "f": "..-.", "g": "--.", "h": "....", "i": "..", "j": ".---", "k": "-.-", "l": ".-..", "m": "--", "n": "-.", "o": "---", "p": ".--.", "q": "--.-", "r": ".-.", "s": "...", "t": "-", "u": "..-", "v": "...-", "w": ".--", "x": "-..-", "y": "-.--", "z": "--.."}
            
            morseCode = ""
            count = 0
            res = []
            
            for word in words:
                for ch in word:
                    morseCode += codes[ch]
                print(morseCode)
                if morseCode not in res:
                    res.append(morseCode)
                    count += 1
                morseCode = ""
            return count
                
                
                
        