# Getting Started

## Hello_World.rs

```rust
fn main() {
    println!("Hello, World!");
}
```

### Compiling and Running

```shell
$ rustc Hello_World.rs
$ ./Hello_World
Hello, World!
```

## Primitive types

|                           |                                 |
| ------------------------- | :------------------------------ |
| `bool`                    | Boolean (`true` _/_ `false`)    |
| `char`                    | character                       |
| `f32`, `f64`              | 32-bits, 64-bits floats         |
| `i64`, `i32`, `i16`, `i8` | signed 16- ... integers         |
| `u64`, `u32`, `u16`, `u8` | unsigned 16-bits, ... integers  |
| `isize`                   | pointer-sized signed integers   |
| `usize`                   | pointer-sized unsigned integers |

## Formatting

```rust
// Single Placeholder
println!("{}", 1);

// Multiple Placeholder
println!("{} {}", 1, 3);

// Positional Arguments
println!(
    "{0} is {1} {2}, also {0} is a {3} programming language",
    "Rust", "cool", "language", "safe"
);

// Named Arguments
println!(
    "{country} is a diverse nation with unity.",
    country = "India"
);

// Placeholder traits :b for binary, :0x is for hex and :o is octal
println!("Let us print 76 is binary which is {:b} , and hex equivalent is {:0x} and octal equivalent is {:o}", 76, 76, 76);

// Debug Trait
println!(
    "Print whatever we want to here using debug trait {:?}",
    (76, 'A', 90)
);

// New Format Strings in 1.58
let x = "world";
println!("Hello {x}!");
```

## Printing Styles

```rust
// Prints the output
print!("Hello World\n");

// Appends a new line after printing
println!("Appending a new line");

// Prints as an error
eprint!("This is an error\n");

// Prints as an error with new line
eprintln!("This is an error with new line");
```

## Variables

```rust
// Initializing and declaring a variable
let some_variable = "This_is_a_variable";

// Making a variable mutable
let mut mutable_variable = "Mutable";

// Assigning multiple variables
let (name, age) = ("ElementalX", 20);

// (Global) constant
const SCREAMING_SNAKE_CASE: i64 = 9;
```

## Comments

```rust
// Line Comments
/*.............Block Comments */
/// Outer doc comments
//! Inner doc comments
```

See: [Comment](https://doc.rust-lang.org/reference/comments.html)

## Functions

```rust
fn test() {
    println!("This is a function!");
}

fn main() {
    test();
}
```
