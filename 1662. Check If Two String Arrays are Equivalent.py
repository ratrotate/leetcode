class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        string1 = ''
        string2 = ''

        for word in word1:
            for w in word:
                string1 += w

        for word in word2:
            for w in word:
                string2 += w
        print(string1, string2)
        
        if string1 == string2:
            return True
    
        return False
