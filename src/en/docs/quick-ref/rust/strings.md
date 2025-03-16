# Strings

## String Literal

```rust
let cs: &str = "cheat sheet";

// => Share cheat sheet for developers
println!("Share {cs} for developers");
```

## String Object

```rust
// Creating an empty string object
let my_string = String::new();

// Converting to a string object
let S_string = a_string.to_string()

// Creating an initialized string object
let lang = String::from("Rust");
println!("First language is {lang}");
```

## .capacity()

```rust
let rand = String::from("Random String");
rand.capacity() // => 13
```

Calculates the capacity of the string in bytes.

## .contains()

```rust
let name = String::from("ElementalX");
name.contains("Element") // => true
```

Checks if the substring is contained inside the original string or not.

## Pushing a single character

```rust
let mut half_text = String::from("Hal");
half_text.push('f'); // => Half
```

## Pushing an entire String

```rust
let mut hi = String::from("Hey there...");
hi.push_str("How are you doing??");

// => Hey there...How are you doing??
println!("{hi}");
```
