---
title: 实践
order: 2
nav:
  title: Go
  order: 1
group:
  title: Go
  order: 1
---


## Golang 实践

### concurrent map

https://github.com/orcaman/concurrent-map


```go
package main

import (
    "github.com/orcaman/concurrent-map/v2"
)

func main() {
    // Create a new map.
    m := cmap.New[string]()

    // Sets item within map, sets "bar" under key "foo"
    m.Set("foo", "bar")

    // Retrieve item from map.
    bar, ok := m.Get("foo")

    // Removes item under key "foo"
    m.Remove("foo")
}
```
