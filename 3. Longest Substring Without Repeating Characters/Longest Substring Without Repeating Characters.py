# @author:leacoder
# @des:  巧用切片 无重复字符的最长子串

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        tmp_list = []
        res = []
        for value in s:
            if value not in tmp_list:
                tmp_list.append(value)
            else:
                res.append(len(tmp_list))
                i = tmp_list.index(value)
                tmp_list = tmp_list[i + 1:]
                tmp_list.append(value)
        res.append(len(tmp_list))
        return max(res)

    	
