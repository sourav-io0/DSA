class Solution:
    def twoSum(self, arr, target):
        seen = {}

        for i in range(len(arr)):
            needed = target - arr[i]

            if needed in seen:
                return [seen[needed], i]

            seen[arr[i]] = i

        return [-1, -1]