# Packages

## Importing

```go
import "fmt"
import "math/rand"
```

### Same as

```go
import (
  "fmt"        // gives fmt.Println
  "math/rand"  // gives rand.Intn
)
```

See: [Importing](https://tour.go.dev/basics/1)

## Aliases

```go
import r "math/rand"
```

---

```go
import (
    "fmt"
    r "math/rand"
)
```

---

```go
r.Intn()
```

## Packages

```go
package main

// An internal package may be imported only by another package
// that is inside the tree rooted at the parent of the internal directory
package internal
```

See: [Internal packages](https://go.dev/doc/go1.4#internalpackages)

## Exporting names

```go
// Begin with a capital letter
func Hello () {
  ···
}
```

See: [Exported names](https://tour.go.dev/basics/3)
