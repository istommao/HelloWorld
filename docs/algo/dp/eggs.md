---
title: 丢鸡蛋
order: 2
nav:
  title: Algo
  order: 1
group:
  title: DP实战
  order: 10
---

# 丢鸡蛋问题

https://leetcode.cn/problems/super-egg-drop/submissions/


```go

func superEggDrop(k int, n int) int {
    dp := make([][]int, k + 1)
    for i := range dp {
        dp[i] = make([]int, n + 1)
    }


    m := 0
    for dp[k][m] < n {
        m ++
        for i := 1; i <= k; i++ {
            dp[i][m] = dp[i][m - 1] + dp[i - 1][m - 1] + 1
        }
    }


    return m
}
```