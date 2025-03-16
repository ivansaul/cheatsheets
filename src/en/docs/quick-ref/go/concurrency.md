# Concurrency

## Goroutines

```go
package main

import (
 "fmt"
 "time"
)

func f(from string) {
 for i := 0; i < 3; i++ {
  fmt.Println(from, ":", i)
 }
}

func main() {
 f("direct")
 go f("goroutine")

 go func(msg string) {
  fmt.Println(msg)
 }("going")

 time.Sleep(time.Second)
 fmt.Println("done")
}
```

See: [Goroutines](https://tour.go.dev/concurrency/1), [Channels](https://tour.go.dev/concurrency/2)

## WaitGroup

```go
package main

import (
 "fmt"
 "sync"
 "time"
)

func w(id int, wg *sync.WaitGroup) {
 defer wg.Done()
 fmt.Printf("%d starting\n", id)

 time.Sleep(time.Second)
 fmt.Printf("%d done\n", id)
}

func main() {
 var wg sync.WaitGroup
 for i := 1; i <= 5; i++ {
  wg.Add(1)
  go w(i, &wg)
 }
 wg.Wait()
}
```

See: [WaitGroup](https://go.dev/pkg/sync/#WaitGroup)

## Closing channels

```go
ch <- 1
ch <- 2
ch <- 3
close(ch) // Closes a channel
```

---

```go
// Iterate the channel until closed
for i := range ch {
  ···
}
```

---

```go
// Closed if `ok == false`
v, ok := <- ch
```

See: [Range and close](https://tour.go.dev/concurrency/4)

## Buffered channels

```go
ch := make(chan int, 2)
ch <- 1
ch <- 2
ch <- 3
// fatal error:
// all goroutines are asleep - deadlock
```

See: [Buffered channels](https://tour.go.dev/concurrency/3)
