// @author:leacoder
// @des:  双指针  移动零

class Solution {
    public void moveZeroes(int[] nums) {
        int lenght = nums.length;
        int notZeroPoint = 0;
        for (int i = 0; i < lenght; i++) {
            if ( 0 != nums[i] ) {
                nums[notZeroPoint++] = nums[i];
            }
        }

        for (int i = notZeroPoint; i < lenght; i++) {
            nums[i] = 0;
        }
    }
}