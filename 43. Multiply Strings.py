def multiply(self, num1, num2):
    """
    :type num1: str
    :type num2: str
    :rtype: str
    """
    ret = [0] * (len(num1) + len(num2))
    for i, x in enumerate(num1[::-1]):
        for j, y in enumerate(num2[::-1]):
            val = int(x) * int(y) + ret[i + j]
            ret[i + j] = val % 10
            ret[i + j + 1] += val // 10
    while len(ret) > 1 and not ret[-1]:
        ret.pop()
    return ''.join(map(str, ret))[::-1]


"""
The idea is just mimic the vertical multiplication

Time: O(m*n)
Space: O(m+n)
"""