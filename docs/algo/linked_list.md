---
title: 链表
order: 2
nav:
  title: Algo
  order: 1
group:
  title: 概念
  order: 1
---

## 单链表

![](./linked_list.png)

```python
class Node(object):
    def __init__(self, value, next_node=None):
        self.value = value
        self.next_node = next_node


def print_linked_list(root):
    while root:
        print(root.value)
        root = root.next_node


root = Node(0)
n1 = Node(1)
n2 = Node(2)
n3 = Node(3)

root.next_node = n1
n1.next_node = n2
n2.next_node = n3

print_linked_list(root)
```

## 双链表

![](./double-linked-list.png)

`Python`

```python
# Definition for double-linked list.
class Node:
    def __init__(self, val, next_node=None, prev=None):
        self.value = val
        self.prev = prev
        self.next_node = None


def print_linked_list(root):
    while root:
        print(root.value)
        root = root.next_node


def reverse_print_linked_list(node):
    while node:
        print(node.value)
        node = node.prev


root = Node(0)
n1 = Node(1, prev=root)
n2 = Node(2, prev=n1)
n3 = Node(3, prev=n2)

n1.next_node = n2
n2.next_node = n3

root.next_node = n1

print_linked_list(root)
print("reverse print")
reverse_print_linked_list(n3)
```

## 循环链表

- 如何判断链表有环
    - 快慢指针（类似操场跑步，跑的快的人最终会套圈（两个指针指向相同节点）
- 如何找出循环链表的入环点
    - 先使用快慢指针，当两个节点指向相同节点后，fast节点从根节点开始
    - fast与slow节点同时一步一步向下一个节点走，下次两个节点相遇时，就是入环点


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
