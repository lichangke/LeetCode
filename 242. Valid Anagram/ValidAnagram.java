/*
 *@author:leacoder
 *@des:  另类map 计算 有效的字母异位词
 */
class Solution {
    public boolean isAnagram(String s, String t) {
        int[] Counts = new int[26];
        for (char ch : s.toCharArray()) {
            Counts[ch - 'a']++;
        }
        for (char ch : t.toCharArray()) {
            Counts[ch - 'a']--;
        }
        for (int i = 0; i < 26; i++) {
            if (Counts[i] != 0) {
                return false;
            }
        }
        return true;
    }
}