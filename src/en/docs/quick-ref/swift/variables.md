# Variables

## Variable declaration

Variables are declared with `var`:

```swift
var greeting = "Hello"
var numberOfToys = 8
var isMorning = true
```

For clarity, variable declarations can contain type annotations:

```swift
var greeting: String = "Hello"
var numberOfToys: Int = 8
var isMorning: Bool = true
```

Variables are mutable. Their values be changed:

```swift
var numberOfToys: Int = 8
numberOfToys += 1

print(numberOfToys)
// print "9"
```

## Constants

Constants are declared with `let`:

```swift
let greeting = "Hello"
let numberOfToys = 8
let isMorning = true
```

For clarity, constant declarations can contain type annotations:

```swift
let greeting: String = "Hello"
let numberOfToys: Int = 8
let isMorning: Bool = true
```

Constants are immutable. Their values be changed:

```swift
let numberOfToys: Int = 8
numberOfToys += 1
// Error: numberOfToys is immutable
```

## Computed Variables (get and set)

```swift
import Foundation

let df = DateFormatter()
df.dateFormat = "d MMMM yyyy"

guard var birth = df.date(from: "5 June 1999") else {
    print("Date is not valid")
    return
}

var age: Int {
    Calendar.current
        .dateComponents([.year],
                        from: birth,
                        to: Date()).year!
}

print(age) // 23
guard let birth2 = df.date(from: "5 June 2002") else {
    print("Date is not valid")
    return
}
birth = birth2
print(age) // 20
```

In the example below, distanceInFeet has a `getter` and a `setter`. Because of the `setter`, the `getter` requires the
keyword `get`:

```swift
var distanceInMeters: Float = 100

var distanceInFeet: Float {
  get {
    distanceInMeters *3.28
  }
  set(newDistance) {
    distanceInMeters = newDistance /3.28
  }
}

print(distanceInMeters) // 100.0
print(distanceInFeet)   // 328.0

distanceInFeet = 250
print(distanceInMeters) // 76.21951
print(distanceInFeet)   // 250.0

distanceInMeters = 800
print(distanceInMeters) // 800.0
print(distanceInFeet)   // 2624.0
```

## willSet

```swift
var distance = 5 {
  willSet {
    print("The distance will be set")
  }
}

distance = 10 // print: distance will be set
```

The new value can be accessed in `willSet`:

```swift
var distance = 5 {
  willSet(newDistance) {
    print("The distance will be set \(newDistance)")
  }
}

distance = 10 // print: distance will be set to 10
```

`willSet` can be used to execute some code before setting the variable value

## didSet

```swift
var distance = 5 {
  didSet {
    print("The distance is set to \(distance)")
    print("Its old value is: \(oldValue)")
  }
}
distance = 10 // print: distance will be set to 10
              // print: its old value is: 5
```

## willSet and didSet

```swift
var distance = 5 {
  willSet(newDistance) {
    print("The distance will be set to \(newDistance)")
  }
  didSet {
    print("The distance is set to \(distance)")
    print("Its old value is: \(oldValue)")
  }
}
distance = 10
```
