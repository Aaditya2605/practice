'''
NeetCode 150
1. Valid Anagram
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

https://neetcode.io/problems/is-anagram
'''

def isAnagram(self, s: str, t: str) -> bool:
        if (len(s) != len(t)):
            return False
        table1 = {}
        for i in s:
            if i in table1:
                table1[i] += 1
            else:
                table1[i] = 1
        table2 = {}
        for i in t:
            if i in table2:
                table2[i] += 1
            else:
                table2[i] = 1
        for i in s:
            if (i in table1) & (i in table2):
                if table1[i] != table2[i]:
                    return False
            else:
                return False
        return True   