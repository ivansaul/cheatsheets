# Getting Started

## Variable

```swift
var score = 0  // Variable
let pi = 3.14  // Constant

var greeting = "Hello"
var numberOfToys = 8
var isMorning = true

var numberOfToys: Int = 8
numberOfToys += 1

print(numberOfToys)
// prints "9"
```

## Type Annotations

```swift
var greeting: String = "Hello"
var numberOfToys: Int = 8
var isMorning: Bool = true
var price: Double = 8.99
```

## Arithmetic Operators

- `+` Add
- `-` Subtraction
- `*` Multiplication
- `/` Division
- `%` Remainder

---

```swift
var x = 0
x = 4 + 2 // x is now 6
x = 4 - 2 // x is now 2
x = 4 * 2 // x is now 8
x = 4 / 2 // x is now 2
x = 4 % 2 // x is now 0
```

---

- `+=` Adds and assigns sums
- `-=` subtract and assign the difference
- `*=` Multiplication and assignment
- `/=` Divide and assign quotient
- `%=` Divide and assign remainder

### Compound Assignment Operators

```swift
var numberOfDogs = 100
numberOfDogs += 1
print("There are \(numberOfDogs) Dalmatians!")

// print: There are 101 Dalmatians!
```

## String Interpolation

```swift
var apples = 6
print("I have \(apples) apples!")

// print: I have 6 apples!
```

## Multi-line String

```swift
let myLongString = """
Swift?
This is my favorite language!
Yeah!
"""
```

## Code Comments

```swift
// This line represents a comment in Swift.

/*
This is all commented out.
None will run!
*/
```

## Form a Tuple

```swift
let player = ("Maya", 5, 150)

print(player) // ("Maya", 5, 150)
print("\(player.0): level \(player.1), \(player.2) pts") // Maya: level 5, 150 pts
```

## Decompose Tuple

```swift
let player = (name: "Maya", level: 5)
let (currentName, curLevel) = player
print("\(currentName): level \(curLevel)")
// print: Maya: level 5
```

## Special Comment Syntax

### MARK

```swift
// MARK: -view settings
```

`MARK` can be used to display comments in the column

### TODO

```swift
// TODO: update logic to accommodate data changes
```

`TODO` is used to display reminders of things that need to be done

### FIXME

```swift
// FIXME: Fix buggy behavior when making changes to existing entries
```

`FIXME` is used to display reminders about things that need to be fixed
