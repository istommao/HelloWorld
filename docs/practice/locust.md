---
title: locust 测试框架
order: 10
nav:
  title: Practices
  order: 10
group:
  title: 实战
  order: 1
---

Website: https://locust.io/


> An open source load testing tool.
Define user behaviour with Python code, and swarm your system with millions of simultaneous users.


![](https://locust.io/static/img/screenshot_2.13.1.png)


## 单机模式

```bash
locust -f your_test_script.py --host=http://127.0.0.1/
```


## 集群模式

```bash
# 启动 master节点
locust -f  your_test_script.py --host=http://0.0.0.0/ --master

# worker 节点可以多开
locust -f  your_test_script.py --host=http://0.0.0.0/ --worker --master-host=<your master host>
```
