class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0 or (x and not x % 10):
            return False
        y = 0
        while x > y:
            y = y * 10 + x % 10
            x //= 10
        return x == y or x == y // 10

"""
we first need to handle some corner case: negative number and positive number with last digit 0
Then we use the same idea as reverse integer. Here we only need to reverse half of the number, which
can be perfectly controlled by condition x > y
Finally, the number is palindrome if x == y if x has even number of digits or x == y//10 if x has odd number
if digits

Time: O(log(n)/2) = O(log(n)) depends on the number of digits of x
Space: O(1)
"""