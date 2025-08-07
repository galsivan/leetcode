class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if str1 + str2 != str2 + str1:
            return ""
        
        if len(str2) < len(str1):
            shorter = str2
            longer = str1
        else:
            shorter = str1
            longer = str2

        s = len(shorter)
        l = len(longer)
        for i in range(l,0,-1):
            if l % i == 0 and s % i == 0:
                if shorter[:i] *  (s // i) == shorter and \
                    shorter[:i] * (l // i) == longer:
                        return shorter[:i]
        return ""
        