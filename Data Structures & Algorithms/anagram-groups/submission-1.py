class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash = {}
        for str in strs:
            chars = [0] * 26
            for i in range(len(str)):
                chars[ord(str[i]) - ord('a')] += 1
            key = tuple(chars)
            if key not in hash:
                hash[key] = [str]
            else:
                hash[key].append(str)
        return list(hash.values())