# Flow Control

## Conditional

```go

a := 10

if a > 20 {
    fmt.Println(">")
} else if a < 20 {
    fmt.Println("<")
} else {
    fmt.Println("=")
}
```

## Statements in if

```go
x := "hello go!"

if count := len(x); count > 0 {
    fmt.Println("Yes")
}

```

---

```go

if _, err := doThing(); err != nil {
    fmt.Println("Uh oh")
}
```

## Switch

```go
x := 42.0
switch x {
case 0:
case 1, 2:
    fmt.Println("Multiple matches")
case 42:   // Don't "fall through".
    fmt.Println("reached")
case 43:
    fmt.Println("Unreached")
default:
    fmt.Println("Optional")
}
```

See: [Switch](https://github.com/golang/go/wiki/Switch)

## For loop

```go
for i := 0; i <= 10; i++ {
  fmt.Println("i: ", i)
}
```

## For-Range loop

```go
nums := []int{2, 3, 4}
sum := 0
for _, num := range nums {
    sum += num
}
fmt.Println("sum:", sum)
```

## While loop

```go
i := 1
for i <= 3 {
    fmt.Println(i)
    i++
}
```

## Continue keyword

```go
for i := 0; i <= 5; i++ {
    if i % 2 == 0 {
        continue
    }
    fmt.Println(i)
}
```

## Break keyword

```go
for {
    fmt.Println("loop")
    break
}
```
