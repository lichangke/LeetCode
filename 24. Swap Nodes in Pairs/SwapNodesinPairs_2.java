/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 * @author:leacoder
 * @des: 循环实现 两两交换链表中的节点
 */
class Solution {
    public ListNode swapPairs(ListNode head) {
        ListNode virtualnode = new ListNode(0);
        virtualnode.next = head;
        
        ListNode node = virtualnode;
        
        while((null!=node.next)&&(null!=node.next.next)){
            ListNode tmp = head.next;//不变的 
            head.next = tmp.next;
            tmp.next = head;//交换
            node.next = tmp;
            
            node = head;//下移  node指向下一组[head,head.next]中head的前节点
            head = node.next;//下移  新的head 指向下一组[head,head.next]的head
        }
        
        return virtualnode.next;
        
    }
}