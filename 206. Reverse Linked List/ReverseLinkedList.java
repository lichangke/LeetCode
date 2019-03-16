/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 * @author:leacoder
 * @des: 迭代实现 反转链表
 */
class Solution {
    public ListNode reverseList(ListNode head) {
        ListNode cur = head; //当前指针节点
        ListNode prev = null; //前指针节点
        ListNode tmp = null;//临时节点
        while(cur!=null){
            tmp = cur.next;//临时节点，暂存当前节点的下一节点，用于后移
            cur.next = prev; //将当前节点指向它前面的节点
            prev =  cur;//前指针后移
            cur = tmp;//当前指针后移
        }
        return prev;
    }
}
