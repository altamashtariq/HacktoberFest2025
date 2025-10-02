class Solution:
    def majorityElement(self, nums):
        n = len(nums)
        ans = []
        freq = {}

        # Count frequencies of each number
        for num in nums:
            freq[num] = freq.get(num, 0) + 1

        # Add elements that appear more than n/3 times
        for key, value in freq.items():
            if value > n // 3:
                ans.append(key)

        return ans
