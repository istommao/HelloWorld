---
title: Poetry
order: 10
nav:
  title: Python
  order: 1
group:
  title: 实战
  order: 1
---

> Poetry是一个Python虚拟环境和依赖管理工具，另外它还提供了包管理功能，比如打包和发布。可以用来管理python库和python程序。

https://python-poetry.org/docs/

## Install poetry

```bash
curl -sSL https://install.python-poetry.org | python3 -
```


## Project setup

```bash
poetry new poetry-demo
```

```bash
poetry-demo
├── pyproject.toml
├── README.md
├── poetry_demo
│   └── __init__.py
└── tests
    └── __init__.py
```

## Initialising a pre-existing project


```bash
cd pre-existing-project
poetry init
```