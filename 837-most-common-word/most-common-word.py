class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        for c in "!?',;.":
            paragraph = paragraph.replace(c, " ")
        
        banned = set(banned)

        paragraph = paragraph.lower().split()

        d = {}
        max_frequency = 0
        res = None

        for word in paragraph:
            if word in banned:
                continue
            d[word] = 1 + d.get(word, 0)
            if d[word] > max_frequency:
                max_frequency = d[word]
                res = word
        
        return res



