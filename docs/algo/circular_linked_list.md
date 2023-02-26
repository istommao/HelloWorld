---
title: 循环链表
order: 2
nav:
  title: Algo
  order: 1
group:
  title: 概念
  order: 1
---

## 循环链表

![](./circular-linked-list.png)

`Python`

```python
# Definition for circular linked list.
class Node:

    def __init__(self, val, next_node=None, prev=None):
        self.value = val
        self.prev = prev
        self.next_node = None



root = Node(0)
n1 = Node(1, prev=root)
n2 = Node(2, prev=n1)
n3 = Node(3, prev=n2)


n1.next_node = n2
n2.next_node = n3

n3.next_node = n1

root.next_node = n1
```

