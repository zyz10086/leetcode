# 给出两个 非空 的链表用来表示两个非负的整数。其中，它们各自的位数是按照 逆序 的方式存储的，并且它们的每个节点只能存储 一位 数字。

# 如果，我们将这两个数相加起来，则会返回一个新的链表来表示它们的和。

# 您可以假设除了数字 0 之外，这两个数都不会以 0 开头。

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/add-two-numbers
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        a , b = [l1],[l2]
        tmp_a,tmp_b = l1,l2
        while( tmp_a.next):
            tmp_a = tmp_a.next
            a.append(tmp_a)
        while( tmp_b.next):
            tmp_b = tmp_b.next
            b.append(tmp_b)
        a_len,b_len = len(a),len(b)
        c = []
        add = 0
        for i in range(a_len):
            if(i<b_len):
                sum_tmp = a[i].val+b[i].val+add
                add = int(sum_tmp / 10)
                c.append(ListNode(sum_tmp-add*10))
            else:
                if(add>0):
                    sum_tmp=a[i].val+add
                    add =int(sum_tmp / 10)
                    c.append(ListNode(sum_tmp-add*10))
                else:
                    c.append(ListNode(a[i].val))
        i+=1
        if(i<b_len):
            for i in range(i,b_len):
                if(add>0):
                    sum_tmp=b[i].val+add
                    add = int(sum_tmp / 10 )
                    c.append(ListNode(sum_tmp-add*10))
                else:
                    c.append(ListNode(b[i].val))
        if(add>0):
            c.append(ListNode(1))
        for i in range(len(c)-1):
            c[i].next = c[i+1]
        return c[0]


l1 = ListNode(2)
l1.next=ListNode(4)
l1.next.next=ListNode(3)
l2 = ListNode(5)
l2.next=ListNode(6)
l2.next.next=ListNode(4)

l1 = ListNode(1)
l1.next=ListNode(8)
l2 = ListNode(0)
s = Solution()
print(s.addTwoNumbers(l1,l2))