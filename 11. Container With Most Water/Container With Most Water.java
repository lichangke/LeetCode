// @author:leacoder
// @des:  暴力法  盛最多水的容器

class Solution {
    public int maxArea(int[] height) {
        int maxArea = 0, lenght = height.length;
        for (int i = 0; i < lenght - 1; i++) {
            for (int j = i + 1; j < lenght; j++) {
                maxArea = Math.max(maxArea, Math.min(height[i], height[j]) * (j - i));
            }            
        }
        return maxArea;
    }
}