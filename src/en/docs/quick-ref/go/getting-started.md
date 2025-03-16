# Getting Started

## hello.go

```go
package main

import "fmt"

func main() {
    fmt.Println("Hello, world!")
}
```

Run directly

```bash
$ go run hello.go
Hello, world!
```

Or try it out in the [Go repl](https://repl.it/languages/go)

## Variables

```go
var s1 string
s1 = "Learn Go!"

// declare multiple variables at once
var b, c int = 1, 2
var d = true
```

Short declaration

```go
s1 := "Learn Go!"        // string
b, c := 1, 2             // int
d := true                // bool
```

## Functions

```go
package main

import "fmt"

// The entry point of the programs
func main() {
    fmt.Println("Hello world!")
    say("Hello Go!")
}

func say(message string) {
    fmt.Println("You said: ", message)
}
```

## Comments

```go
// Single line comment

/* Multi-
 line comment */
```

## If statement

```go
if true {
    fmt.Println("Yes!")
}
```
