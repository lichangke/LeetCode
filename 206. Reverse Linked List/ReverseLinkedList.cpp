/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 * @author:leacoder
 * @des: 迭代实现 反转链表
 */
class Solution {
public:
    ListNode* reverseList(ListNode* head) {
        ListNode* cur = head; 	//当前指针节点
        ListNode* prev = NULL;	//前指针节点
        ListNode* temp = NULL;	//临时节点
        while(NULL!=cur){
            temp = cur->next;	//临时节点，暂存当前节点的下一节点(断开处的节点)，用于后移
            cur->next = prev;	//将当前节点指向它前面的节点
            prev = cur;	//前指针后移
            cur = temp;	//当前指针后移
        }
        return prev;
    }
};
