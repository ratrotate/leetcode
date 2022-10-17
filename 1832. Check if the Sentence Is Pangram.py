class Solution:
    # import string for having an alphabet
    import string
    
    def checkIfPangram(self, sentence: str) -> bool:
        alp = string.ascii_lowercase
        hashmap = {}
        
        for key in alp:
            hashmap[key] = 0
    
        for elem in sentence:
            if elem in hashmap.keys():
                hashmap[elem] += 1
    
        return 0 not in hashmap.values()
