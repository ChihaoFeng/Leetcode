from collections import Counter
from collections import defaultdict


class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        if not s or not words:
            return []
        table = Counter(words)
        m = len(words)
        n = len(words[0])
        ret = []
        for i in range(n):
            subd = defaultdict(int)
            left = i
            count = 0
            for j in range(i, len(s) - n + 1, n):
                word = s[j:j + n]
                if word in table:
                    subd[word] += 1
                    count += 1
                    while subd[word] > table[word]:
                        subd[s[left:left + n]] -= 1
                        count -= 1
                        left += n
                    if count == m:
                        ret.append(left)
                else:
                    left = j + n
                    subd.clear()
                    count = 0
        return ret


"""
For example, S="ABCDEFGHI", and L=["EFG"].
When i=0, we match "EFG" with S. In this process, we match "EFG" with "ABC", "DEF", "GHI", but they are all incorrect.
So, next time, let i=i+1 and j=i, which means S's first substr is "BCD", so we match "EFG" with "BCD", "EFG", it's correct.
But when i = wl(which equals 3), we match "EFG" with "DEF","GHI", and it's the same as i=0, so it's unnecessary.

Time: O(m*n)
Space: O(m)
"""
