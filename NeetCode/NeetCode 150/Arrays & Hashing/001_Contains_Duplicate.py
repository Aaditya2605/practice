'''
NeetCode 150
1. Contains Duplicates
Given an integer array nums, return true if any value appears more than once in the array, otherwise return false.

https://neetcode.io/problems/duplicate-integer
'''

from typing import List

def hasDuplicate(self, nums: List[int]) -> bool:
    dict = {}
    for i in nums:
        if i in dict:
            return True
        dict[i] = 1
    return False   