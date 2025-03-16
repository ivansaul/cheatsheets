# Functions

## Multiple arguments

```go
func plus(a int, b int) int {
    return a + b
}
func plusPlus(a, b, c int) int {
    return a + b + c
}
fmt.Println(plus(1, 2))
fmt.Println(plusPlus(1, 2, 3))
```

## Multiple return

```go
func vals() (int, int) {
    return 3, 7
}

a, b := vals()
fmt.Println(a)    // => 3
fmt.Println(b)    // => 7
```

## Function literals

```go
r1, r2 := func() (string, string) {
    x := []string{"hello", "cheatsheets.zip"}
    return x[0], x[1]
}()

// => hello cheatsheets.zip
fmt.Println(r1, r2)
```

## Naked returns

```go
func split(sum int) (x, y int) {
  x = sum * 4 / 9
  y = sum - x
  return
}

x, y := split(17)
fmt.Println(x)   // => 7
fmt.Println(y)   // => 10
```

Note that using naked returns hurts readability.

## Variadic functions

```go
func sum(nums ...int) {
    fmt.Print(nums, " ")
    total := 0
    for _, num := range nums {
        total += num
    }
    fmt.Println(total)
}
sum(1, 2)     //=> [1 2] 3
sum(1, 2, 3)  // => [1 2 3] 6

nums := []int{1, 2, 3, 4}
sum(nums...)  // => [1 2 3 4] 10
```

## init function

```go
import --> const --> var --> init()
```

---

```go
var num = setNumber()

func setNumber() int {
    return 42
}
func init() {
    num = 0
}
func main() {
    fmt.Println(num) // => 0
}
```

## Functions as values

```go
func main() {
    // assign a function to a name
    add := func(a, b int) int {
        return a + b
    }
    // use the name to call the function
    fmt.Println(add(3, 4)) // => 7
}
```

## Closures 1

```go
func scope() func() int{
    outer_var := 2
    foo := func() int {return outer_var}
    return foo
}

// Outpus: 2
fmt.Println(scope()())
```

## Closures 2

```go
func outer() (func() int, int) {
    outer_var := 2
    inner := func() int {
        outer_var += 99
        return outer_var
    }
    inner()
    return inner, outer_var
}
inner, val := outer()
fmt.Println(inner()) // => 200
fmt.Println(val)     // => 101
```
