/*
 *@author:leacoder
 *@des:   一层枚举 左右两指针形式  三数之和 
 */
class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        vector<vector<int>> res; //返回值
        if(nums.size()<3){ //输入检查
            return res;
        }
        sort(nums.begin(), nums.end()); //排序
        
        for (int i = 0; i < nums.size()-2; i++) //一层循环
        {
            if(i>0 && nums[i] == nums[i-1])
                continue;
            int target = -nums[i]; //其他两数和
            int l = i + 1, r = nums.size() - 1; //左右指针形式  l 左 r右
            while (l < r)
            {
                if (nums[l] + nums[r] < target) //小于目标 l 增加
                    ++l;
                else if (nums[l] + nums[r] > target) //大于目标 r 减少
                    --r;
                else{ //刚好
                    res.push_back(vector<int>{nums[i], nums[l], nums[r]});
                    while (l < r && nums[l] == nums[l+1])
                        l++;
                    while (l < r && nums[r] == nums[r-1])
                        r--;
                    l++; r--;
                }
            }
            
        }
        return res;
    }
};