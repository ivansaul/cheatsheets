# Generics

## example 1

```go
// comparable represents types that can be compared.
type comparable interface {
 int | float64 | string
}

// Max returns the maximum of two comparable values.
func Max[T comparable](a, b T) T {
 if a > b {
  return a
 }
 return b
}

func main() {
 // Find the maximum of two integers.
 maxInt := Max(10, 20)
 fmt.Println("Max integer:", maxInt)

 // Find the maximum of two floats.
 maxFloat := Max(3.14, 2.71)
 fmt.Println("Max float:", maxFloat)

 // Find the maximum of two strings.
 maxString := Max("apple", "banana")
 fmt.Println("Max string:", maxString)
}

```

## example 2

```go

// Pair[T, U] represents a generic pair of values.
type Pair[T, U any] struct {
 First  T
 Second U
}

func main() {
 pair := Pair[int, string]{First: 42, Second: "hello"}

 fmt.Println("First:", pair.First)
 fmt.Println("Second:", pair.Second)

 // Print the types of the values in the pair.
 fmt.Println("Type of First:", reflect.TypeOf(pair.First))
 fmt.Println("Type of Second:", reflect.TypeOf(pair.Second))
}

```
