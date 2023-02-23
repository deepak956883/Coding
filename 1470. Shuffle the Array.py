'''
1470. Shuffle the Array

'''



....

class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        i = 0
        j = n
        ans = []
        while (i<n and j<2*n):
            for k in range(2*n):
                if k%2==0:
                    ans.append(nums[i])
                    i = i+1
                else:
                    ans.append(nums[j])
                    j = j+1
        return ans 
