/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 * @author:leacoder
 * @des: 快慢指针 环形链表 
 */
class Solution {
public:
    bool hasCycle(ListNode *head) {
        ListNode *slow=head,*fast=head;
        while(NULL!=slow&&NULL!=fast&&NULL!=fast->next){
            slow = slow->next;
            fast = fast->next->next;
            if(slow == fast) 
                return true;
        }
        return false;
    }
};