/**
 * Definition for singly-linked list.
 * class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) {
 *         val = x;
 *         next = null;
 *     }
 * }
 * @author:leacoder
 * @des:  存储记录 环形链表 HashSet 
 */
public class Solution {
    public boolean hasCycle(ListNode head) {
        HashSet<ListNode> hSet = new HashSet<>();
        while(null != head){
            if(hSet.contains(head)){
                return true;
            }else{
                hSet.add(head);
            }
            head = head.next;
        }
        return false;
    }
}