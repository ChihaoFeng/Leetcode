class Solution:
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        ret, curr, num_of_letters = [], [], 0
        for word in words:
            if num_of_letters + len(curr) + len(word) > maxWidth:
                for i in range(maxWidth - num_of_letters):
                    curr[i % (len(curr) - 1 or 1)] += ' '
                ret.append(''.join(curr))
                curr, num_of_letters = [], 0
            curr.append(word)
            num_of_letters += len(word)
        return ret + [' '.join(curr).ljust(maxWidth, ' ')]


"""
if we are out of space after we add the word, we are going to add space after each current word except the last one.
Once we determine that there are only k words that can fit on a given line, we know what the total length of those words
is num_of_letters. Then the rest are spaces, and there are (maxWidth - num_of_letters) of spaces. 
The "or 1" part is for dealing with the edge case len(cur) == 1.

Time: O(n)
Space: O(maxWidth)
"""
