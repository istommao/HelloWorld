---
title: 循环链表
order: 2
nav:
  title: Algo
  order: 1
group:
  title: 链表实战
  order: 1
---

![](./circular-linked-list.png)


- 如何判断链表有环
    - 快慢指针（类似操场跑步，跑的快的人最终会套圈（两个指针指向相同节点）
- 如何找出循环链表的入环点
    - 先使用快慢指针，当两个节点指向相同节点后，fast节点从根节点开始
    - fast与slow节点同时一步一步向下一个节点走，下次两个节点相遇时，就是入环点

## 判断链表是否有环

### Python实现

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return None

        slow = head
        fast = head

        while True:
            if not fast or not fast.next:
                return None

            slow = slow.next
            fast = fast.next.next

            if fast == slow:
                break

        fast = head
        while slow != fast:
            slow = slow.next
            fast = fast.next

        return fast
```

### Go语言实现

`判断链表是否有环`

```go
/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func hasCycle(head *ListNode) bool {
    slow := head
    fast := head
    for {
        if fast == nil || fast.Next == nil {
            break
        }

        fast = fast.Next.Next
        slow = slow.Next
        if (fast == slow) {
            return true
        }
    }

    return false
}
```


## 找出循环链表入环点

### Python实现

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return None

        slow = head
        fast = head

        while True:
            if not fast or not fast.next:
                return None

            slow = slow.next
            fast = fast.next.next

            if fast == slow:
                break

        fast = head
        while slow != fast:
            slow = slow.next
            fast = fast.next

        return fast
```

### Go语言实现

```go
/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */

func detectCycle(head *ListNode) *ListNode {
    slow := head
    fast := head

    var is_cycle bool
    for {
        if fast == nil || fast.Next == nil {
            break
        }

        fast = fast.Next.Next
        slow = slow.Next
        if (fast == slow) {
            is_cycle = true
            break
        }
    }

    if is_cycle {
        fast = head

        for {
            if slow == fast {
                return fast
            }
            slow = slow.Next
            fast = fast.Next
        }
    }

    return nil
}
```