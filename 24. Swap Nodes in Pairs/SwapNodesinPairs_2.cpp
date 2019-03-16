/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 * @author:leacoder
 * @des: 循环实现 两两交换链表中的节点
 */
class Solution {
public:
    ListNode* swapPairs(ListNode* head) {
        /*在头结点前新建一节点，其next指向head。好处 将[]\[1]这种特殊情况能够统一处理*/
        ListNode *virtualnode = new ListNode(0);
        virtualnode->next = head;
        
        ListNode *node = virtualnode;//存储新的开始节点
        
        while(head&&head->next){
            ListNode *tmp = head->next;//不变的 
            head->next = tmp->next;
            tmp->next = head;//交换
            node->next = tmp;
            
            node = head;
            head = node->next;//下移
        }
        
        return virtualnode->next;
            
    }
};