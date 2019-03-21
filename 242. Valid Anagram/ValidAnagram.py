# @author:leacoder
# @des:  排序法 有效的字母异位词
# 时间复杂度 O(NlogN)
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)