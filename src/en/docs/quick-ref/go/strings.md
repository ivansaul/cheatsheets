# Strings

## Strings function

```go
package main

import (
 "fmt"
 s "strings"
)

func main() {
    /* Need to import strings as s */
 fmt.Println(s.Contains("test", "e"))

    /* Build in */
    fmt.Println(len("hello"))  // => 5
    // Outputs: 101
 fmt.Println("hello"[1])
    // Outputs: e
 fmt.Println(string("hello"[1]))

}
```

## fmt.Printf

```go
package main

import (
 "fmt"
 "os"
)

type point struct {
 x, y int
}

func main() {
 p := point{1, 2}
 fmt.Printf("%v\n", p)                        // => {1 2}
 fmt.Printf("%+v\n", p)                       // => {x:1 y:2}
 fmt.Printf("%#v\n", p)                       // => main.point{x:1, y:2}
 fmt.Printf("%T\n", p)                        // => main.point
 fmt.Printf("%t\n", true)                     // => TRUE
 fmt.Printf("%d\n", 123)                      // => 123
 fmt.Printf("%b\n", 14)                       // => 1110
 fmt.Printf("%c\n", 33)                       // => !
 fmt.Printf("%x\n", 456)                      // => 1c8
 fmt.Printf("%f\n", 78.9)                     // => 78.9
 fmt.Printf("%e\n", 123400000.0)              // => 1.23E+08
 fmt.Printf("%E\n", 123400000.0)              // => 1.23E+08
 fmt.Printf("%s\n", "\"string\"")             // => "string"
 fmt.Printf("%q\n", "\"string\"")             // => "\"string\""
 fmt.Printf("%x\n", "hex this")               // => 6.86578E+15
 fmt.Printf("%p\n", &p)                       // => 0xc00002c040
 fmt.Printf("|%6d|%6d|\n", 12, 345)           // => |    12|   345|
 fmt.Printf("|%6.2f|%6.2f|\n", 1.2, 3.45)     // => |  1.20|  3.45|
 fmt.Printf("|%-6.2f|%-6.2f|\n", 1.2, 3.45)   // => |1.20  |3.45  |
 fmt.Printf("|%6s|%6s|\n", "foo", "b")        // => |   foo|     b|
 fmt.Printf("|%-6s|%-6s|\n", "foo", "b")      // => |foo   |b     |

 s := fmt.Sprintf("a %s", "string")
 fmt.Println(s)

 fmt.Fprintf(os.Stderr, "an %s\n", "error")
}

```

See also: [fmt](https://go.dev/pkg/fmt/)

## Function examples

| Example                       | Result      |
| ----------------------------- | ----------- |
| Contains("test", "es")        | true        |
| Count("test", "t")            | 2           |
| HasPrefix("test", "te")       | true        |
| HasSuffix("test", "st")       | true        |
| Index("test", "e")            | 1           |
| Join([]string{"a", "b"}, "-") | a-b         |
| Repeat("a", 5)                | aaaaa       |
| Replace("foo", "o", "0", -1)  | f00         |
| Replace("foo", "o", "0", 1)   | f0o         |
| Split("a-b-c-d-e", "-")       | [a b c d e] |
| ToLower("TEST")               | test        |
| ToUpper("test")               | TEST        |
