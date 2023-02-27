---
title: 反转链表
order: 2
nav:
  title: Algo
  order: 1
group:
  title: 链表实战
  order: 1
---

## 反转链表

![](https://www.itzoo.top/assets/img/linkedlist.drawio.34dfa28c.png)

`迭代法`

```python
class Node(object):
    def __init__(self, value, next_node=None):
        self.value = value
        self.next_node = next_node


def reverse_linked_list(root: Node) -> Node:
    prev = None
    curr = root

    while curr:
        nextnode = curr.next_node
        curr.next_node = prev

        prev = curr
        curr = nextnode

    return prev
```


`递归`

```python
def reverse_list(root: Node) -> Node:
    if not root or not root.next_node:
        return root

    newroot = reverse_list(root.next_node)
    root.next_node.next_node = root
    root.next_node = None

    return newroot
```
