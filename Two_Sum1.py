""" Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order """

class solution:
    def two_sum(self, nums, target):
        for i, num1 in enumerate(nums):
            for j, num2 in enumerate(nums):
                if i != j and num1 + num2 == target:
                    return [i,j]
                