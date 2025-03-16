# Flow Control

## If Expression

```rust
let case1: i32 = 81;
let case2: i32 = 82;

if case1 < case2 {
  println!("case1 is greater than case2");
}
```

## If...Else Expression

```rust
let case3 = 8;
let case4 = 9;

if case3 >= case4 {
    println!("case3 is better than case4");
} else {
    println!("case4 is greater than case3");
}
```

## If...Else...if...Else Expression

```rust
let foo = 12;
let bar = 13;

if foo == bar {
    println!("foo is equal to bar");
} else if foo < bar {
    println!("foo less than bar");
} else if foo != bar {
    println!("foo is not equal to bar");
} else {
    println!("Nothing");
}
```

## If...Let Expression

```rust
let mut arr1: [i64; 3] = [1, 2, 3];
if let [1, 2, _] = arr1 {
    println!("Works with array");
}

let mut arr2: [&str; 2] = ["one", "two"];
if let ["Apple", _] = arr2 {
    println!("Works with str array too");
}
```

---

```rust
let tuple_1 = ("India", 7, 90, 90.432);
if let (_, 7, 9, 78.99) = tuple_1 {
    println!("Works with tuples too");
}

let tuple_2 = (9, 7, 89, 12, "Okay");
if let (9, 7, 89, 12, blank) = tuple_2 {
    println!("Everything {blank} mate?");
}

let tuple_3 = (89, 90, "Yes");
if let (9, 89, "Yes") = tuple_3 {
    println!("Pattern did match");
} else {
    println!("Pattern did not match");
}
```

## Match Expression

```rust
let day_of_week = 2;
match day_of_week {
    1 => {
        println!("Its Monday my dudes");
    }
    2 => {
        println!("It's Tuesday my dudes");
    }
    3 => {
        println!("It's Wednesday my dudes");
    }
    4 => {
        println!("It's Thursday my dudes");
    }
    5 => {
        println!("It's Friday my dudes");
    }
    6 => {
        println!("It's Saturday my dudes");
    }
    7 => {
        println!("It's Sunday my dudes");
    }
    _ => {
        println!("Default!")
    }
};
```

## Nested...If Expression

```rust
let nested_conditions = 89;
if nested_conditions == 89 {
    let just_a_value = 98;
    if just_a_value >= 97 {
        println!("Greater than 97");
    }
}
```

## For Loop

```rust
for mut i in 0..15 {
    i -= 1;
    println!("The value of i is : {i}");
}
```

## While Loop

```rust
let mut check = 0;
while check < 11 {
    println!("Check is : {check}");
    check += 1;
    println!("After incrementing: {check}");

    if check == 10 {
        break; // stop while
    }
}
```

## Loop keyword

```rust
loop {
    println!("hello world forever!");
}
```

The infinite loop indicated.

## Break Statement

```rust
let mut i = 1;
loop {
    println!("i is {i}");
    if i > 100 {
        break;
    }
    i *= 2;
}
```

## Continue Statement

```rust
for (v, c) in (0..10 + 1).enumerate() {
    println!("The {c} number loop");
    if v == 9 {
        println!("Here we go continue?");
        continue;
    }
    println! {"The value of v is : {v}"};
}
```
