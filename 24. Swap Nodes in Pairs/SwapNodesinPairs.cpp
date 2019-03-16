/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 * @author:leacoder
 * @des: 递归实现 两两交换链表中的节点
 */
class Solution {
public:
    //每两个节点为一组 反转前的前节点（反转后的 后节点）、反转前的后节点（反转后的 前节点）
    //下一组 为 反转前的后节点（反转后的 前节点）的 next
    ListNode* swapPairs(ListNode* head) { //入参 反转前的前节点（反转后的 后节点）
        if (NULL==head || NULL==head->next) 
            return head; 
        ListNode *res = head->next; //记录 反转前的后节点（反转后的 前节点）
        head->next = swapPairs(res->next); //更新 反转后的 后节点 的next  为下一组 反转后的 前节点  （入参为反转前的后节点的next 即为下一组的 反转前的前节点（反转后的 后节点）
        res->next = head;
        
        return res;
    }
};