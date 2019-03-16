/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 * @author:leacoder
 * @des: 递归实现 两两交换链表中的节点
 */
class Solution {
    public ListNode swapPairs(ListNode head) {
        if((head == null)||(head.next == null))
            return head;
        ListNode second = head.next;
        head.next = swapPairs(second.next);
        second.next = head;
        return second;
    }
}