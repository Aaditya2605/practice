'''
NeetCode 150
3. Two Sum
Given an array of integers nums and an integer target, return the indices i and j such that nums[i] + nums[j] == target and i != j.

You may assume that every input has exactly one pair of indices i and j that satisfy the condition.

Return the answer with the smaller index first.

https://neetcode.io/problems/two-integer-sum
'''
from typing import List

def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}
        
        map = {val: idx for idx, val in enumerate(nums)}; # val : idx
                                                                 # for idx, val in emurate arr
        for i, n in enumerate(nums):
            difference = target - n # from the hint
            if (difference in map) and (map[difference] != i):
                    return [i, map[difference]]
        return []