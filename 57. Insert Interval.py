# Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e


class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]
        """
        left, right = [], []
        s, e = newInterval.start, newInterval.end
        for interval in intervals:
            if interval.end < s:
                left.append(interval)
            elif interval.start > e:
                right.append(interval)
            else:
                s = min(s, interval.start)
                e = max(e, interval.end)
        newInterval.start, newInterval.end = s, e
        left.append(newInterval)
        left.extend(right)
        return left


"""

"""