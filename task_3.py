"""given an array of integers, return indices of the two numbers such that they add up to a specific target """


def twoSum(self, nums, target):
    for i, num in enumerate(nums):
        for j in range(i + 1, len(nums)):
            if num + nums[j] == target:
                return [i, j]
