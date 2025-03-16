# Types

## Integer

```rust
let mut a: u32 = 8;
let b: u64 = 877;
let c: i64 = 8999;
let d = -90;
```

## Floating-Point

```rust
let mut sixty_bit_float: f64 = 89.90;
let thirty_two_bit_float: f32 = 7.90;
let just_a_float = 69.69;
```

## Boolean

```rust
let true_val: bool = true;
let false_val: bool = false;
let just_a_bool = true;
let is_true = 8 < 5; // => false
```

## Character

```rust
let first_letter_of_alphabet = 'a';
let explicit_char: char = 'F';
let implicit_char = '8';
let emoji = "\u{1f600}"; // => 😀
```

## String Literal

```rust
let community_name = "AXIAL";
let no_of_members: &str = "ten";

println!("The name of the community is {community_name} and it has {no_of_members} members");
```

## Arrays

```rust
┌─────┬─────┬─────┬─────┬─────┬─────┐
| 92  | 97  | 98  | 99  | 98  | 94  |
└─────┴─────┴─────┴─────┴─────┴─────┘
   0     1     2     3     4     5
```

---

```rust
let array: [i64; 6] = [92, 97, 98, 99, 98, 94];
```

## Multi-Dimensional Array

```rust
     j0   j1   j2   j3   j4   j5
   ┌────┬────┬────┬────┬────┬────┐
i0 | 1  | 2  | 3  | 4  | 5  | 6  |
   ├────┼────┼────┼────┼────┼────┤
i1 | 6  | 5  | 4  | 3  | 2  | 1  |
   └────┴────┴────┴────┴────┴────┘
```

---

```rust
let array: [[i64; 6]; 2] = [
    [1, 2, 3, 4, 5, 6],
    [6, 5, 4, 3, 2, 1]
];
```

## Mutable Array

```rust
let mut array: [i32; 3] = [2, 6, 10];

array[1] = 4;
array[2] = 6;
```

Use the `mut` keyword to make it mutable.

## Slices

```rust
let mut array: [i64; 4] = [1, 2, 3, 4];
let mut slices: &[i64] = &array[0..3]; // Lower range is inclusive and upper range is exclusive

println!("The elements of the slices are : {slices:?}");
```

## Vectors

```rust
let some_vector = vec![1, 2, 3, 4, 5];
```

A vector is declared using the `vec!` macro.

## Tuples

```rust
let tuple = (1, 'A', "Cool", 78, true);
```
