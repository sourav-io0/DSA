class Solution:
    def leaders(self, nums):
        result = []

        for i in range(len(nums)):
            leader = True

            for j in range(i + 1, len(nums)):
                if nums[j] >= nums[i]:
                    leader = False
                    break

            if leader:
                result.append(nums[i])

        return result
nums = [16, 17, 4, 3, 5, 2]

solution = Solution()
print(solution.leaders(nums))