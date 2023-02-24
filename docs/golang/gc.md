---
title: GC
order: 2
nav:
  title: Go
  order: 1
group:
  title: Go
  order: 1
---

## GC 垃圾回收 （三色标记法）

- 白色： 代表最终需要被清理的对象内存块
- 灰色：待处理的内存块
- 黑色：活跃的内存块


## 执行流程

- 所有对象初始为`白色`
- 扫描所以可以搜索到的对象，不需要清理的对象标记会`灰色`, 放入待处理队列
- 从队列中取出灰色对象，将其引用的对象标记会`灰色`放入队列，自身标记为`黑色`
- 有锁监视对象内存的改变
- 在完成全部扫描标记后，只有白色和黑色对象，清除白色对象

## 学习资料推荐

- [Go 语言设计与实现 - 内存分配](https://draveness.me/golang/docs/part3-runtime/ch07-memory/golang-memory-allocator/)
- [Go专家编程 - 内存分配原理](https://books.studygolang.com/GoExpertProgramming/chapter04/4.1-memory_alloc.html)