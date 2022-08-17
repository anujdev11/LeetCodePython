class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
            codes = {"a": ".-", "b": "-...", "c": "-.-.", "d": "-..", "e": ".", "f": "..-.", "g": "--.", "h": "....", "i": "..", "j": ".---", "k": "-.-", "l": ".-..", "m": "--", "n": "-.", "o": "---", "p": ".--.", "q": "--.-", "r": ".-.", "s": "...", "t": "-", "u": "..-", "v": "...-", "w": ".--", "x": "-..-", "y": "-.--", "z": "--.."}
            
            morseCode = ""
            res = []
            
            for word in words:
                morseCode = ""
                for ch in word:
                    morseCode += codes[ch]
                res.append(morseCode)
                
            return len(set(res))
                
                
                
        