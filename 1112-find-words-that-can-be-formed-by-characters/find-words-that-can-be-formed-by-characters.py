class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        d = {}
        res = 0

        # create dict of chars bc we need frequencies
        for c in chars:
            d[c] = 1 + d.get(c, 0)
        
        for word in words:
            tmp = dict(d)
            good = True

            for c in word:
                if c not in tmp:
                    good = False
                    break
                if tmp[c] == 1:
                    del tmp[c]
                else:
                    tmp[c] -= 1
            if good:
                res += len(word)
        return res
                
            

        