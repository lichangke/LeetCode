/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 * @author:leacoder
 * @des: 递归实现 反转链表
 */
class Solution {
public:
    ListNode* reverseList(ListNode* head) {
        //第一个条件是判断递归开始，传入的参数的合法性。第二个是递归的终止条件
        if (NULL==head || NULL==head->next) 
            return head; 
        ListNode* result = reverseList(head->next); // 循环递归找到最后一个节点 (head->next为最后一节点） 那么 result指向最后节点 以【A B C D】为例 指向 D
        head->next->next = head;//以【A B C D】为例 最底部到达此处时 head 为 C ,head->next 为 D ，反转为  head->next->next 为 C (head)
        head->next = NULL; //以【A B C D】为例 断开 C D 之间连接 C 的 next 指向 NULL，即为  head->next = NULL 如果不断掉 C D成环 递归无法终止
        
        return result; 
    }
};
