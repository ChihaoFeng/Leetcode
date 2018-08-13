import collections
import string
class Solution:
    def findLadders(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: List[List[str]]
        """

        def dfs(s, path):
            if s == endWord:
                ret.append(path + [s])
                return
            path.append(s)
            for child in graph[s]:
                dfs(child, path)
            path.pop()
            return

        wordList = set(wordList)
        if endWord not in wordList:
            return []
        beginSet = set([beginWord])
        endSet = set([endWord])
        graph = collections.defaultdict(set)
        wordLen = len(beginWord)
        found = False
        backward = False
        while beginSet and endSet and not found:
            for word in beginSet:
                wordList.discard(word)
            for word in endSet:
                wordList.discard(word)
            if len(beginSet) > len(endSet):
                beginSet, endSet = endSet, beginSet
                backward = not backward
            temp = set()
            for word in beginSet:
                for i in range(wordLen):
                    for alpha in string.ascii_lowercase:
                        target = word[:i] + alpha + word[i + 1:]
                        parent = word
                        child = target
                        if backward:
                            parent, child = child, parent
                        if target in endSet:
                            found = True
                            graph[parent].add(child)
                        elif target in wordList and not found:
                            graph[parent].add(child)
                            temp.add(target)
            beginSet = temp

        if not found:
            return []
        ret = []
        dfs(beginWord, [])
        return ret