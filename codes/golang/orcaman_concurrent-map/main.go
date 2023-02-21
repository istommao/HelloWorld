package main

import (
	"fmt"
	"sync"

	cmap "github.com/orcaman/concurrent-map/v2"
)

type WsClient struct {
	index int
}

type WebsocketMap struct {
	cm cmap.ConcurrentMap[string, *WsClient]
}

func NewWebsocketMap() *WebsocketMap {
	n := cmap.New[*WsClient]()

	return &WebsocketMap{cm: n}
}

func (w *WebsocketMap) GetCount() int {
	return w.cm.Count()
}

func (w *WebsocketMap) Set(key string, client *WsClient) {
	w.cm.Set(key, client)
}
func (w *WebsocketMap) Get(key string) (*WsClient, bool) {
	return w.cm.Get(key)
}

func Test() {
	// Create a new map.
	m := cmap.New[string]()

	// Sets item within map, sets "bar" under key "foo"
	m.Set("foo", "bar")

	// Retrieve item from map.
	bar, ok := m.Get("foo")
	fmt.Println(bar, ok)

	// Removes item under key "foo"
	m.Remove("foo")

	// Retrieve item from map.
	bar, ok = m.Get("foo")
	fmt.Println(bar == "", ok)
}

// func main() {
// 	n := cmap.New[interface{}]()
// 	// Sets item within map, sets "bar" under key "foo"
// 	n.Set("age", "20")

// 	m := cmap.New[cmap.ConcurrentMap[string, interface{}]]()

// 	m.Set("foo", n)

// 	// Retrieve item from map.
// 	bar, ok := m.Get("foo")
// 	fmt.Println(bar, ok)

// 	x, ok := bar.Get("age")
// 	fmt.Println(x, ok)
// }

func main() {
	wmap := NewWebsocketMap()

	lst := []int{}
	for i := 1; i <= 10000; i++ {
		lst = append(lst, i)
	}
	wg := sync.WaitGroup{}

	wg.Add(len(lst))

	for _, index := range lst {
		go func(index int) {
			client1 := &WsClient{index: index}
			key1 := fmt.Sprint(client1)
			wmap.Set(key1, client1)
			wg.Done()
		}(index)

	}
	wg.Wait()
	fmt.Println(wmap.GetCount())
}
