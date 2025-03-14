# Extensions

## What are extensions?

Extensions is a way to add new add new functionality to existing classes, structures, enumerations, or protocol types. This includes adding new methods, properties, initializers, and more.

## Why use extensions?

Extensions are particularly useful for organizing and modularizing our code without needing to modify the original type, especially when we don't have access to the original source code.

## Extension syntax

```swift
extension SomeType {
    // New functionalities to be added
}
```

## Computed properties

```swift
extension Int {
    var isEven: Bool {
        self % 2 == 0
    }
}

print(4.isEven) // Outputs: true
print(7.isEven) // Outputs: false
```

## Methods

```swift
extension String {
    func reverse() -> String {
        String(self.reversed())
    }
}

print("abc".reverse()) // Output: cba
```

## Mutating methods

```swift
extension Int {
    mutating func square() {
        self = self * self
    }
}

var number = 5
number.square()
print(number) // Output: 25
```

## Initializers

```swift
extension Date {
    init?(timestamp: Double) {
        self.init(timeIntervalSince1970: timestamp)
    }
}

let timestamp = 1693982400.0 // Unix timestamp for 2023-09-06 06:40:00
if let date = Date(timestamp: timestamp) {
    print(date) // Output: 2023-09-06 06:40:00 +0000
}
```

## Subscripts

```swift
extension String {
    subscript(index: Int) -> Character {
        self[self.index(startIndex, offsetBy: index)]
    }
}

print("Swift"[0]) // Output: S
print("Swift"[1]) // Output: w
print("Swift"[2]) // Output: i
print("Swift"[3]) // Output: f
print("Swift"[4]) // Output: t
```

## Protocol extensions

It works pretty much like abstract classes when regarding a functionality we want to be available in all the classes that implements some protocol (without having to inherit from a base common class).

```swift
// Define a protocol
protocol Describable {
    func describe() -> String
}

// Provide a default implementation using a protocol extension
extension Describable {
    func describe() -> String {
        "This is a generic description"
    }
}

// Define a struct that conforms Describable protocol
struct Person: Describable {
    var name: String
    var age: Int

    // Overriding the default implementation
    func describe() -> String {
        "My name is \(name) and I am \(age) years old."
    }
}

struct Employee: Describable {
    var name: String
    var age: Int

    // Using the default implementation
}

// By just implementing the protocol the describe() method is available

let person = Person(name: "Ivan", age: 21)
let employee = Employee(name: "Saul", age: 25)

print(person.describe()) // Output: My name is Ivan and I am 21 years old.
print(employee.describe()) // Output: This is a generic description
```

## Constraints for extensions

This is especially useful when we want to add functionality to a type that conforms to a specific protocol or has certain conditions.

```swift
extension Array where Element: Numeric {
    func sum() -> Element {
        reduce(0, +)
    }
}

let numbers = [1, 2, 3, 4, 5]
print(numbers.sum()) // Output: 15

let doubles = [1.5, 2.5, 3.5]
print(doubles.sum()) // Output: 7.5

// This will not work because String is not Numeric
// let strings = ["a", "b", "c"]
// print(strings.sum()) // Error: Cannot invoke 'sum' with an array of strings
```

## Organizing code with extensions

Extensions are not limited to adding functionality; they are also handy for code organization. We can group related methods, properties or views in separate extensions.

```swift
import SwiftUI

struct HomeView: View {
    var body: some View {
        ScrollView {
            header
            // Add other views
        }
    }
}

extension HomeView {
    private var header: some View {
        Text("Header ...")
    }
}

#Preview {
    HomeView()
}
```
