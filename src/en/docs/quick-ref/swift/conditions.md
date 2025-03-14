# Conditions

## `if` statement

```swift
var halloween = true
if halloween {
  print("Trick or treat!")
}
// print: Trick or treat!
if 5 > 3 {
  print("5 is greater than 3")
} else {
  print("5 is not more than 3")
}
// output: "5 is greater than 3"
```

## `else` statement

```swift
var turbulence = false

if turbulence {
  print("Please sit down.")
} else {
  print("You are free to move around.")
}
// print: You are free to move around.
```

## `else if` statement

```swift
var weather = "rainy"
if weather == "sunny" {
  print("Get some sunscreen")
} else if weather == "rainy" {
  print("Take an umbrella")
} else if weather == "snowing" {
  print("Put on your snow boots")
} else {
  print("Invalid weather")
}
// print: take an umbrella
```

## Comparison Operators

```swift
5 > 1      // true
6 < 10     // true
2 >= 3     // false
3 <= 5     // true
"A" == "a" // false
"B" != "b" // true
```

-`<` less than <br> -`>` greater than <br> -`<=` less than or equal to <br> -`>=` greater than or equal to <br> -`==` is
equal to <br> -`!=` is not equal to

## Range Operators

```swift
a...b      // numbers between a and b (including both a and b)
a..<b      // numbers between a and b (including a but excluding b)
...b      // numbers till b (including b)
```

-`a...b` Closed Range <br> -`a..<b` Half-Open Range <br> -`...b` One-Sided Range

## Ternary Conditional Operator

```swift
var driverLicense = true

driverLicense
    ? print("driver seat") : print("passenger seat")
// print: driver's seat
```

## `switch` statement

```swift
var secondaryColor = "green"

switch secondaryColor {
  case "orange":
    print("A mixture of red and yellow")
  case "purple":
    print("A mix of red and blue")
  default:
    print("This may not be a secondary color")
}
// print: mix of blue and yellow
```

### Interval Matching

```swift
let year = 1905
var artPeriod: String

switch year {
  case 1860...1885:
    artPeriod = "Impressionism"
  case 1886...1910:
    artPeriod = "Post-Impressionism"
  default:
    artPeriod = "Unknown"
}
// print: post-impressionism
```

### Composite Case

```swift
let service = "Seamless"

switch service {
case "Uber", "Lyft":
    print("travel")
  case "DoorDash", "Seamless", "GrubHub":
    print("Restaurant delivery")
  case "Instacart", "FreshDirect":
    print("Grocery Delivery")
  default:
    print("Unknown service")
}
// print: restaurant takeaway
```

### `where` Clause

```swift
let num = 7

switch num {
  case let x where x % 2 == 0:
    print("\(num) is even")
  case let x where x % 2 == 1:
    print("\(num) odd number")
  default:
    print("\(num) is invalid")
}

// print: 7 odd
```

## Logical Operators

```swift
!true  // false
!false //true
```

### Operators &&

```swift
true && true   // true
true && false  // false
false && true  // false
false && false // false
```

### operators ||

```swift
true || true   // true
true || false  // true
false || true  // true
false || false // false
```

### Combined Logical Operators

```swift
!false && true || false // true
```

`!false && true` first evaluates and returns `true` Then, the expression, `true` || `false` evaluates and returns the
final result `true`

```swift
false || true && false // false
```

`true && false` first evaluates to return `false` Then, the expression, `false` || `false` evaluates and returns the
final result `false`

## Control the order of execution

```swift

// without parentheses:
true || true && false || false
//----> true

// with brackets:
(true || true) && (false || false)
//----> false

```

## Simple guards

```swift
func greet(name: String?) {
  guard let unwrapped = name else {
    print("Hello guest!")
    return
  }
  print("Hello \(unwrapped)!")
}
greet(name: "Asma") // output: Hello Asma!
greet(name: nil)    // output: Hello guest!
```
