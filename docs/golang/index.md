---
title: 安装
order: 2
nav:
  title: Go ⚡️
  order: 1
group:
  title: 基础
  order: 1
---



## 下载

https://go.dev/dl/


## Mac 交叉编译

```bash
# mac上编译linux和windows二进制
CGO_ENABLED=0 GOOS=linux GOARCH=amd64 go build 
CGO_ENABLED=0 GOOS=windows GOARCH=amd64 go build 
```

## Linux 交叉编译

```bash
# linux上编译mac和windows二进制
CGO_ENABLED=0 GOOS=darwin GOARCH=amd64 go build 
CGO_ENABLED=0 GOOS=windows GOARCH=amd64 go build
```


## Windows 交叉编译

```bash
# windows上编译mac和linux二进制
SET CGO_ENABLED=0 SET GOOS=darwin SET GOARCH=amd64 go build main.go
SET CGO_ENABLED=0 SET GOOS=linux SET GOARCH=amd64 go build main.go
```
