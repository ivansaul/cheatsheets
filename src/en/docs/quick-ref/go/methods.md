# Methods

## Receivers

```go
type Vertex struct {
  X, Y float64
}
```

```go
func (v Vertex) Abs() float64 {
  return math.Sqrt(v.X * v.X + v.Y * v.Y)
}
```

```go
v := Vertex{1, 2}
v.Abs()
```

See: [Methods](https://tour.go.dev/methods/1)

## Mutation

```go
func (v *Vertex) Scale(f float64) {
  v.X = v.X * f
  v.Y = v.Y * f
}
```

```go
v := Vertex{6, 12}
v.Scale(0.5)
// `v` is updated
```

See: [Pointer receivers](https://tour.go.dev/methods/4)
