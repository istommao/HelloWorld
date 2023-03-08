---
title: locust + boomer测试
order: 10
nav:
  title: Practices
  order: 10
group:
  title: 实战
  order: 1
---


https://github.com/myzhan/boomer


## Master

```bash
nohup locust --master -f dummy.py--master-bind-host=0.0.0.0 --master-bind-port=5557 --host=http://127.0.0.1/ &
```


## Worker

```bash
# Install the master branch
$ go get github.com/myzhan/boomer@master
# Install a tagged version that works with locust 1.6.0
$ go get github.com/myzhan/boomer@v1.6.0
```

`Code`

```go
// your boomer worker test code
package main

import "time"
import "github.com/myzhan/boomer"





func demotest() {
    elapsed := time.Since(time.Now())
    boomer.RecordSuccess("http", "demotest", elapsed.Nanoseconds()/int64(time.Millisecond), int64(10))
}

func main(){
    task1 := &boomer.Task{
        Name: "foo",
        // The weight is used to distribute goroutines over multiple tasks.
        // Weight: 10,
        Fn: demotest,
    }


    boomer.Run(task1)
}


```

```bash
go run . --master-port=5557 --master-host=<ip.address> 
```
