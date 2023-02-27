---
title: 最小栈
order: 2
nav:
  title: Algo
  order: 1
group:
  title: 栈实战
  order: 1
---

https://leetcode.cn/problems/min-stack/

> 利用两个栈实现

## Python实现

```python
class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.minstack = []

    def push(self, val: int) -> None:
        self.stack.append(val)

        if not self.minstack or val <= self.getMin():
            self.minstack.append(val)

    def pop(self) -> None:
        val = self.stack.pop()
        if val == self.getMin():
            self.minstack.pop()

    def top(self) -> int:
        return self.stack[-1]


    def getMin(self) -> int:
        if self.minstack:
            return self.minstack[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
```