---
title: Daily report
order: 10
nav:
  title: Daily report
  order: 10

---

## 2023


### 2-27 Algo & Python

`Python`
- [Discord bot最小demo](/python/discord_bot)

`Algo`
- [最小栈 - 使用两个栈实现](/algo/min_stack)


### 2-26 Algo

`pypi`
- https://github.com/istommao/algolibs

`Algo 循环链表`

- [反转链表](/algo/reverse_linked_list)
- [循环链表](/algo/linked_list)
  - 如何判断链表有环
      - 快慢指针（类似操场跑步，跑的快的人最终会套圈（两个指针指向相同节点）
  - 如何找出循环链表的入环点
      - 先使用快慢指针，当两个节点指向相同节点后，fast节点从根节点开始
      - fast与slow节点同时一步一步向下一个节点走，下次两个节点相遇时，就是入环点

`https://leetcode.cn/problems/linked-list-cycle-ii/`

### 2-24 Go

`Go`

- [MPG模型](/golang/mpg)
- [GC](/golang/gc)

`Algo`

- [双链表](/algo/linked_list)
- [循环链表](/algo/linked_list)

### 2-23 Algo


`算法`

- [单链表](/algo/linked_list)
  - 删除倒数第K个节点 (快慢指针)

### 2-22 kuma


>  A fancy self-hosted monitoring tool

- Github: https://github.com/louislam/uptime-kuma
- Website: uptime.kuma.pet

```bash
# Run
docker run -d --restart=always -p 3001:3001 -v uptime-kuma:/app/data --name uptime-kuma louislam/uptime-kuma:1
```

![daily-report-2023-2-22](./daily-report-2023-2-22.jpeg)
