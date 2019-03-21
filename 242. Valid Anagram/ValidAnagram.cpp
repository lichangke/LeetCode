/*
 *@author:leacoder
 *@des:  map 计算 有效的字母异位词
 * 时间复杂度O(N)
 */

class Solution {
public:
    bool isAnagram(string s, string t) {
       if (s.size() != t.size()) return false;

		unordered_map<char, int> mp1;
		unordered_map<char, int> mp2;

		for (char c : s) mp1[c]++;
		for (char c : t) mp2[c]++;

		unordered_map<char, int>::iterator it;
		for (it = mp1.begin(); it != mp1.end(); it++) //for循环遍历map
			if (it->second != mp2[it->first]) //it->second 为value it->first为key
				return false;
		return true;
    }
};
