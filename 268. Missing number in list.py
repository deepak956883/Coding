
# missing number

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        Totalsum = (n*(n+1))//2
        sum = 0
        for i in nums:
            sum = sum + i
        missing = Totalsum - sum
        return missing