# Functions

## Basic function

```rust
fn print_message() {
    println!("Hello, CheatSheets.zip!");
}

fn main() {
    //Invoking a function in Rust.
    print_message();
}
```

## Pass by Value

```rust
fn main() {
    let x: u32 = 10;
    let y: u32 = 20;

    // => 200
    println!("Calc: {}", cal_rect(x, y));
}

fn cal_rect(x: u32, y: u32) -> u32 {
    x * y
}
```

## Pass by Reference

```rust
fn main() {
    let mut by_ref = 3; // => 3
    power_of_three(&mut by_ref);
    println!("{by_ref}"); // => 9
}

fn power_of_three(by_ref: &mut i32) {
    // de-referencing is important
    *by_ref = *by_ref * *by_ref;
    println!("{by_ref}"); // => 9
}
```

## Returns

```rust
fn main() {
    let (mut radius, mut pi) = (3.0, 3.14);
    let (area, _perimeter) = calculate(
        &mut radius,
        &mut pi
    );
    println!("The area and the perimeter of the circle are: {area} & {_perimeter}");
}

fn calculate(radius: &mut f64, pi: &mut f64) -> (f64, f64) {
    let perimeter = 2.0 * *pi * *radius;
    let area = *pi * *radius * *radius;
    return (area, perimeter);
}
```

## Arrays as Arguments

```rust
fn main() {
    let mut array: [i32; 5] = [1, 2, 3, 4, 6];
    print_arrays(array);
    println!("The elements: {array:?}");
}

fn print_arrays(mut array: [i32; 5]) {
    array[0] = 89;
    array[1] = 90;
    array[2] = 91;
    array[3] = 92;
    array[4] = 93;
    println!("The elements: {array:?}");
}
```

## Returning Arrays

```rust
fn main() {
    let mut arr: [i32; 5] = [2, 4, 6, 8, 10];
    multiply(arr);
    println!("The array is : {:?}", multiply(arr));
}

fn multiply(mut arr: [i32; 5]) -> [i32; 5] {
    arr[2] = 90;
    for mut i in 0..5 {
        arr[i] = arr[i] * arr[2];
    }
    return arr;
}
```
