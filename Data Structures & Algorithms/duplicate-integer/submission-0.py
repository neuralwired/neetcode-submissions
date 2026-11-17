class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hash = {}
        for num in nums:
            if num not in hash:
                hash[num] = 1
            else:
                hash[num] += 1
        for num in nums:
            if hash[num] > 1:
                return True
        return False