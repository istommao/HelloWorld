---
title: sync.mutex
order: 2
nav:
  title: Go
  order: 1
group:
  title: 并发原语
  order: 2
---

`互斥锁`

Mutex 可能处于两种不同的模式：正常模式和饥饿模式。

- 在`正常模式`中，等待者按照 FIFO 的顺序排队获取锁，但是一个被唤醒的等待者有时候并不能获取 mutex， 它还需要和新到来的 goroutine 们竞争 mutex 的使用权。 

- 新到来的 goroutine 存在一个优势，它们已经在 CPU 上运行且它们数量很多， 因此一个被唤醒的等待者有很大的概率获取不到锁，在这种情况下它处在等待队列的前面。 

- 如果一个 goroutine 等待 mutex 释放的时间超过 1ms，它就会将 mutex 切换到饥饿模式

- 在`饥饿模式`中，mutex 的所有权直接从解锁的 goroutine 递交到等待队列中排在最前方的 goroutine。 

- 新到达的 goroutine 们不要尝试去获取 mutex，即使它看起来是在解锁状态，也不要试图自旋， 而是排到等待队列的尾部。


如果一个等待者获得 mutex 的所有权，并且看到以下两种情况中的任一种：

- 它是等待队列中的最后一个，
- 它等待的时间少于 1ms，它便将 mutex 切换回正常操作模式

> 正常模式下的性能会更好，因为一个 goroutine 能在即使有很多阻塞的等待者时多次连续的获得一个 mutex，饥饿模式的重要性则在于避免了病态情况下的尾部延迟。


## 加锁
Lock 对申请锁的情况分为三种：

- 无冲突，通过 CAS 操作把当前状态设置为加锁状态
- 有冲突，开始自旋，并等待锁释放，如果其他 goroutine 在这段时间内释放该锁，直接获得该锁；如果没有释放则为下一种情况
- 有冲突，且已经过了自旋阶段，通过调用 semrelease 让 goroutine 进入等待状态

## 文档来源于以下资料

- https://golang.design/under-the-hood/zh-cn/part1basic/ch05sync/mutex/

