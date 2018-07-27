class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""
        strs.sort(key=len)
        ret = strs[0]
        for i in range(1, len(strs)):
            while strs[i].find(ret) != 0:
                ret = ret[:-1]
        return ret


"""
The idea is to use horizontal scanning to find LCP
LCP(S1…Sn)=LCP(LCP(LCP(S1,S2),S3),…Sn)
In python, we use find determine whether the current prefix is also the prefix of the encountered string
If not, we get rid of the last character of current prefix and try again
Time: O(S) S is the sum of all character in all strings
Space: O(1)
"""
