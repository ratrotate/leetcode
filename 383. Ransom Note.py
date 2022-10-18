class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        hashmap = {}
        for word in magazine:
            if word not in hashmap.keys():
                hashmap[word] = 1
            else:
                hashmap[word] += 1

        for word_m in ransomNote:
            if word_m not in hashmap.keys():
                return False
            else:
                hashmap[word_m] -= 1
                if hashmap[word_m] == 0:
                    del hashmap[word_m]
        return True
