# Miscellaneous

## Type Casting

```rust
let a_int = 90; // int
// int to float
let mut type_cast = (a_int as f64);
```

---

```rust
let original: char = 'I';
// char to int => 73
let type_casted: i64 = original as i64;
```

To perform type-casting in Rust one must use the `as` keyword.

## Borrowing

```rust
let mut foo = 4;
let mut borrowed_foo = &foo;
println!("{borrowed_foo}");
```

---

```rust
let mut bar = 3;
let mut mutable_borrowed_bar = &mut bar;
println!("{mutable_borrowed_bar}");
```

Here borrowed value borrows the value from value one using `&` operator.

## De-referencing

```rust
let mut borrow = 10;
let deref = &mut borrow;

println!("{}", *deref);
```

De-referencing in rust can be done using the `*` operator

## Variable Scope

```rust
{
    // The scope limited to this braces
    let a_number = 1;
}
println!("{a_number}");
```

This will produce error as the scope of the variable `a_number` ends at the braces
