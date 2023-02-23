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

### 遍历

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

### 删除倒数第K个数

> `快慢指针` (双指针法)

```python

def delete_k(root, number):
    pass
```

## 双链表链表

## 循环链表
