# Error Control

## Deferring functions

```go
func main() {
  defer func() {
    fmt.Println("Done")
  }()
  fmt.Println("Working...")
}
```

## Lambda defer

```go
func main() {
  var d = int64(0)
  defer func(d *int64) {
    fmt.Printf("& %v Unix Sec\n", *d)
  }(&d)
  fmt.Print("Done ")
  d = time.Now().Unix()
}
```

The defer func uses current value of d, unless we use a pointer to get final value at end of main.

## Defer

```go
func main() {
  defer fmt.Println("Done")
  fmt.Println("Working...")
}
```

See: [Defer, panic and recover](https://blog.go.dev/defer-panic-and-recover)
