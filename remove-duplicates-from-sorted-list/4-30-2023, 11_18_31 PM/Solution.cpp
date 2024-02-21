// https://leetcode.com/problems/remove-duplicates-from-sorted-list

/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* deleteDuplicates(ListNode* head) {
        if (!head)
        {
            return head;
        }
        ListNode* runner = head;
        while (runner->next)
        {
            if (runner->next->val == runner->val)
            {
                runner->next = runner->next->next;
            }
            else
            {
                runner = runner->next;
            }
        }
        return head;
    }
};