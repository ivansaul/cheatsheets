# Basic Types

## Strings

```go
s1 := "Hello" + "World"

s2 := `A "raw" string literal
can include line breaks.`

// Outputs: 10
fmt.Println(len(s1))

// Outputs: Hello
fmt.Println(string(s1[0:5]))
```

Strings are of type `string`.

## Numbers

```go
num := 3         // int
num := 3.        // float64
num := 3 + 4i    // complex128
num := byte('a') // byte (alias: uint8)

var u uint = 7        // uint (unsigned)
var p float32 = 22.7  // 32-bit float
```

### Operators

```go
x := 5
x++
fmt.Println("x + 4 =", x + 4)
fmt.Println("x * 4 =", x * 4)
```

## Booleans

```go
isTrue   := true
isFalse  := false
```

### Operators

```go
fmt.Println(true && true)   // true
fmt.Println(true && false)  // false
fmt.Println(true || true)   // true
fmt.Println(true || false)  // true
fmt.Println(!true)          // false
```

## Arrays

```go
┌────┬────┬────┬────┬─────┬─────┐
| 2  | 3  | 5  | 7  | 11  | 13  |
└────┴────┴────┴────┴─────┴─────┘
  0    1    2    3     4     5
```

---

```go
primes := [...]int{2, 3, 5, 7, 11, 13}
fmt.Println(len(primes)) // => 6

// Outputs: [2 3 5 7 11 13]
fmt.Println(primes)

// Same as [:3], Outputs: [2 3 5]
fmt.Println(primes[0:3])
```

---

```go
var a [2]string
a[0] = "Hello"
a[1] = "World"

fmt.Println(a[0], a[1]) //=> Hello World
fmt.Println(a)   // => [Hello World]
```

### 2d array

```go
var twoDimension [2][3]int
for i := 0; i < 2; i++ {
    for j := 0; j < 3; j++ {
        twoDimension[i][j] = i + j
    }
}
// => 2d:  [[0 1 2] [1 2 3]]
fmt.Println("2d: ", twoDimension)
```

## Pointers

```go
func main () {
  b := *getPointer()
  fmt.Println("Value is", b)
}
```

```go
func getPointer () (myPointer *int) {
  a := 234
  return &a
}
```

```go
a := new(int)
*a = 234
```

See: [Pointers](https://tour.go.dev/moretypes/1)

## Slices

```go
s := make([]string, 3)
s[0] = "a"
s[1] = "b"
s = append(s, "d")
s = append(s, "e", "f")

fmt.Println(s)
fmt.Println(s[1])
fmt.Println(len(s))
fmt.Println(s[1:3])

slice := []int{2, 3, 4}
```

See also: [Slices example](https://gobyexample.com/slices)

## Constants

```go
const s string = "constant"
const Phi = 1.618
const n = 500000000
const d = 3e20 / n
fmt.Println(d)
```

## Type conversions

```go
i := 90
f := float64(i)
u := uint(i)

// Will be equal to the character Z
s := string(i)
```

### How to get int string?

```go
i := 90

// need import "strconv"
s := strconv.Itoa(i)
fmt.Println(s) // Outputs: 90
```
