'''
NeetCode 150
5. Top K Frequent Elements
Given an integer array nums and an integer k, return the k most frequent elements within the array.

The test cases are generated such that the answer is always unique.

You may return the output in any order.

https://neetcode.io/problems/top-k-elements-in-list
'''
from collections import defaultdict
from typing import List

def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = defaultdict(int)
        for num in nums:
            hashmap[num] += 1;  # (number : frequency)
        freq = sorted(hashmap.items(), key=lambda kv: kv[1], reverse = True)[:k]
        List = []
        for k,v in freq:
            List.append(k)
        return List