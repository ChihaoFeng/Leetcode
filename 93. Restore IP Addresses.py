class Solution:
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """

        def dfs(i, count, path):
            if count == 4:
                if i == len(s):
                    ret.append('.'.join(path))
                return
            for j in range(i + 1, min(i + 4, len(s) + 1)):
                if j != i + 1 and s[i] == '0' or int(s[i:j]) > 255:
                    break
                path.append(s[i:j])
                dfs(j, count + 1, path)
                path.pop()

        ret = []
        dfs(0, 0, [])
        return ret


"""
"""
