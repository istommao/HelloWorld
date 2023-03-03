---
title: MPG模型
order: 2
nav:
  title: Go
  order: 1
group:
  title: 实践
  order: 10
---

## MPG概念

`goroutine调度机制`

- M Machine，或 worker thread 代表一个线程，所有 goroutine任务最终都会在M上执行
- P
    - 代表一个处理器(即一种人为抽象的、用于执行 Go 代码被要求局部资源)，每个运行的M都必须绑定一个P
- G 代表 goroutine对象，每次go调用时都会创建一个G对象

## goroutine调度流程

- 创建 gorotuine对象，加入本地队列或全局队列
- 查找空闲的P
    - 如果有，用系统API创建一个M（线程）
- 由这个M循环执行G任务
- G任务的执行顺序
    - 先从本地队列找
    - 从全局队列找
    - 去其他P中找

- 所以G任务的执行顺序按照go的调用顺序执行

## 学习资料

- [《GO专家编程》 协程](https://books.studygolang.com/GoExpertProgramming/chapter03/3.1-go_schedule.html)
- [MPG 模型与并发调度单元](https://golang.design/under-the-hood/zh-cn/part2runtime/ch06sched/mpg/)