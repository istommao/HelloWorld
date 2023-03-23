---
title: Daily report
order: 10
nav:
  title: Daily report
  order: 10

---

## 2023-03

### 3-22 Telegram bot

`Python`

- [Telegram bot最小demo](/python/telegram_bot)


### 3-16 K8s minikube

`Install minikube`

Website: https://minikube.sigs.k8s.io/docs/start/


- [minikube实战](/practice/k8s_minikube)


### 3-15 PostgreSQL

`Install`

```bash
sudo sh -c 'echo "deb http://apt.postgresql.org/pub/repos/apt $(lsb_release -cs)-pgdg main" > /etc/apt/sources.list.d/pgdg.list'

wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | sudo apt-key add -

sudo apt-get update

sudo apt-get -y install postgresql
```

`Start`

```bash
sudo /etc/init.d/postgresql start  
sudo /etc/init.d/postgresql stop   
sudo /etc/init.d/postgresql restart
```

`Create`

```bash
sudo -i -u postgres

$ psql
postgres=#

现在位于数据库提示符下。

2、创建数据库新用户，如 dbuser：

postgres=# CREATE USER dbuser WITH PASSWORD '*****';
注意：

语句要以分号结尾。
密码要用单引号括起来。
3、创建用户数据库，如exampledb：

postgres=# CREATE DATABASE exampledb OWNER dbuser;
4、将exampledb数据库的所有权限都赋予dbuser：

postgres=# GRANT ALL PRIVILEGES ON DATABASE exampledb TO dbuser;
5、使用命令 \q 退出psql：

postgres=# \q
```


### 3-13 MongoDB

`Install`

```bash
brew tap mongodb/brew

brew install mongodb-community@6.0
```

### 3-12 Linux Command

`Get my ip`

```bash
curl ifconfig.me

# or
curl ifconfig.me/all
```


### 3-11 Linux Command

`netstat`

tcp 统计

```bash
# install
apt install net-tools
```

`TCP stats 1`

```bash
netstat -s -t | sed -e '/Tcp:/!d;:l;n;/^\ /!d;bl'

# output
Tcp:
    103728 active connection openings
    101462 passive connection openings
    141 failed connection attempts
    106936 connection resets received
    3 connections established
    353276068 segments received
    353175097 segments sent out
    77587 segments retransmitted
    14 bad segments received
    75744 resets sent
```

`TCP stats 2`

```bash
netstat -na | awk '/^tcp/ {++S[$NF]} END {for(a in S) print a, S[a]}'

# output
LISTEN 29
LAST_ACK 1
CLOSE_WAIT 7
TIME_WAIT 16
ESTABLISHED 72
```

### 3-10 systemd

`systemd` 简单实践


- [systemd实战](/practice/systemd)


### 3-9 locust + boomer

> 基于 locust + boomer 实现高并发压力测试

https://github.com/myzhan/boomer

- [locust + boomer 压测实战](/practice/locust_boomer)

### 3-8 Astro 2.0 正式发布


> Astro 是一个现代化的轻量级静态站点生成器，用于构建以内容为中心的高性能网站

[Astro 2.0正式发布](https://mp.weixin.qq.com/s/Z3YA9dp5p3PkLm3sePfFJA)

#### Bun


> Bun is a modern JavaScript runtime, built from scratch to serve the modern JavaScript focus on three main things:

`Install bun`

```bash
curl -fsSL https://bun.sh/install | bash
```

`Demo`

```js
// http.js
export default {
  port: 3000,
  fetch(request) {
    return new Response("Welcome to Bun!");
  },
};
```

`Run`

```bash
bun run http.js
```


### 3-2 Python

`asyncio queue`

- [asyncio queue](/python/async_queue)


### 3-2 Go

`sync & atomic`

- [sync & atomic](/golang/sync_mutex)

### 3-1

`TestFramework`

- [locust](/practice/locust)

## 2023-02

### 2-28 Python

`Python`

- [Async Websocket Client Demo](/python/async_websocket)

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
