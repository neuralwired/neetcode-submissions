class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        hash1 = {}
        for ch in s:
            if ch in hash1:
                hash1[ch] += 1
            else:
                hash1[ch] = 1
        hash2 = {}
        for ch in t:
            if ch in hash2:
                hash2[ch] += 1
            else:
                hash2[ch] = 1
        return hash1 == hash2