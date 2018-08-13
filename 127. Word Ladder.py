import string


class Solution:
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        wordList = set(wordList)
        if endWord not in wordList:
            return 0
        beginSet = set([beginWord])
        endSet = set([endWord])
        distance = 2
        wordLen = len(beginWord)
        visited = set([beginWord, endWord])

        while beginSet and endSet:
            if len(beginSet) > len(endSet):
                beginSet, endSet = endSet, beginSet
            tempSet = set()
            for word in beginSet:
                for i in range(wordLen):
                    for alpha in string.ascii_lowercase:
                        target = word[:i] + alpha + word[i + 1:]
                        if target in endSet:
                            return distance
                        elif target not in visited and target in wordList:
                            visited.add(target)
                            tempSet.add(target)
            beginSet = tempSet
            distance += 1
        return 0
