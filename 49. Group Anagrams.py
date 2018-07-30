import collections
class Solution:
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        table = collections.defaultdict(list)
        for s in strs:
            temp = [0] * 26
            for c in s:
                temp[ord(c) - ord('a')] += 1
            table[tuple(temp)].append(s)
        return list(table.values())

    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        table = collections.defaultdict(list)
        for s in strs:
            table[''.join(sorted(s))].append(s)
        return list(table.values())

"""
Sol1: categorize by sorted string
Time: O(n*klogk) n is the length of strs, k is the maximum length of a string in strs
Space: O(nk)

Sol2: Categorize by Count
Time: O(nk)
Space: O(nk)
"""