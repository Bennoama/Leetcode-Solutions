// https://leetcode.com/problems/intersection-of-two-linked-lists

/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */

size_t Length(ListNode *headA){
    size_t count = 0;
    while (headA){
        headA = headA->next;
        ++count;
    }
    return count;
}

class Solution {
public:
    ListNode *getIntersectionNode(ListNode *headA, ListNode *headB) {
        size_t lenA = Length(headA);
        size_t lenB = Length(headB);
        ListNode *longList = headA;
        ListNode *shortList = headB;
        size_t diff = lenA - lenB;
        if (lenA < lenB){
            longList = headB;
            shortList = headA;
            diff = lenB - lenA;
        }
        while (diff--){
            longList = longList->next;
        }
        while (longList != shortList)
        {
            longList = longList->next;
            shortList = shortList->next;
        }
        return longList;

    }
};