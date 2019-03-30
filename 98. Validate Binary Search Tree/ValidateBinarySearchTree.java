/*
 *@author:leacoder
 *@des:  递归比较min max,  验证二叉搜索树
 */
/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
class Solution {
    public boolean isValidBST(TreeNode root) {
        Integer min = null;
        Integer max = null;
        
        return isValid(root,min,max);
    }
    public boolean isValid(TreeNode root,Integer min,Integer max){ //min 下界   max上界
        if(root == null) return true;
        if(min!=null && root.val <=min) return false; 
        if(max!=null && root.val >=max) return false;  //当前root节点值 必须在 min 和 max之间
        
        //注意下边函数式子     分别递归检测   root的左子树（min下界不关心，其上界必须是root的值） 与 root右子树（max上界不关心，其下界界必须是root的值）
        return isValid(root.left,min,root.val)&&isValid(root.right,root.val,max);
    }
}