/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 * @author:leacoder 
 *@des:  BFS 广度优先  二叉树的层次遍历  时间复杂度 O(n)
 */
class Solution {
    public List<List<Integer>> levelOrder(TreeNode root) {
        
        List<List<Integer>> result = new ArrayList();
        if (root == null)
            return result;
        
        Queue<TreeNode> q = new LinkedList<>();
        q.add(root);
        
        while(!q.isEmpty()){
            int levelSize = q.size();
            List<Integer> currentLevel = new ArrayList();
            for(int i = 0; i < levelSize; i++ ){
                TreeNode currentNode = q.poll(); //先进先出 从第一个元素（头部）  移除
                currentLevel.add(currentNode.val);
                if(currentNode.left!=null){
                    q.add(currentNode.left);
                }
                if(currentNode.right!=null){
                    q.add(currentNode.right);
                }
            }
            result.add(currentLevel);
        }
        return result;
    }
}