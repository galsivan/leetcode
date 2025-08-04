class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        i = 0
        j = 0

        while j < len(abbr):
            if i == len(word):
                return False
                
            if abbr[j] == "0":
                return False

            if abbr[j] == word[i]:
                i += 1
                j += 1
                continue
            
            if abbr[j].isdigit():
                jump = ""
                while j < len(abbr) and abbr[j].isdigit():
                    jump += abbr[j]
                    j += 1
                if len(jump) > 0:
                    i += int(jump)
            else:
                return False
            
        return i == len(word)