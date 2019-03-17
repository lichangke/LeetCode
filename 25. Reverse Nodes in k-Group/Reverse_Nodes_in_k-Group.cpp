/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 * @author:leacoder
 * @des: 存储法 k个一组翻转链表
 */
class Solution {
public:
    ListNode* reverseKGroup(ListNode* head, int k) {
        ListNode *nodearray[k];//存储 需翻转的 k个节点
        ListNode* result = new ListNode(0); //翻转后链表 用于结果返回
        ListNode* ret = result;//由于存储翻转后链表
        int count = 0;
        while( NULL != head){
            ListNode* next = head->next; //记录下移节点
            nodearray[count] = head; //记录到数组
            count++;//数组 下标自加 
            if(k == count){ //已存 k个值  需要翻转了
               for(int i = k;i>0;i--){ //循环读取 数组中数据
                   ret->next = nodearray[i-1]; //从后往前去数组中数据 添加到ret链表中
                   ret = ret->next;//移位
                   nodearray[i-1] = NULL;//置空
                   count--;//数组中数据个数--
               }
            }
            head = next;
        }
        
        for(int i = 0;i<count;i++){//处理不需要翻转的数据
           ret->next = nodearray[i];
           ret = ret->next;
           nodearray[i] = NULL;
        }
        ret->next = NULL;
        return result->next;
    }
};