// @author:leacoder
// @des:  双指针法  盛最多水的容器


class Solution {
    public int maxArea(int[] height) {
        int maxArea = 0, lenght = height.length;
        int left = 0, right = lenght - 1;
        while (right > left) {
            maxArea = Math.max(maxArea, Math.min(height[left], height[right]) * (right - left));
            if (height[left] < height[right] ) {
                left++;
            } else {
                right--;
            }
        }
        return maxArea;
    }
}