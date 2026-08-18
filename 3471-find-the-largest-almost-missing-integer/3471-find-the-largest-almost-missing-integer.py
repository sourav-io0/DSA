class Solution:
    def largestInteger(self, nums, k):
        n = len(nums)

        # Case 1
        if k == n:
            return max(nums)

        # Count frequencies
        freq = {}

        for x in nums:
            freq[x] = freq.get(x, 0) + 1

        # Case 2
        if k == 1:
            ans = -1

            for x in nums:
                if freq[x] == 1:
                    ans = max(ans, x)

            return ans

        # Case 3
        ans = -1

        if freq[nums[0]] == 1:
            ans = max(ans, nums[0])

        if freq[nums[-1]] == 1:
            ans = max(ans, nums[-1])

        return ans
        
        