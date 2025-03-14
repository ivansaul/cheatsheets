# Generics

## What are generics?

Generics in Swift are a feature that allows us to create functions, classes, structures, and protocols that can work with any data type.

## Why use generics?

Generics enable us to write clear and concise code that works with any data type. By using placeholders (like `T`), this reduces the risk of introducing bugs.

## Type parameters

```swift
func foo<T, U>(a: T, b: U) {
  // ...
}

struct Foo<T, U> {
  var a: T
  // ...
}
```

The placeholders `T` is an example of a type parameter, are written inside angle brackets(such as `<T>`).

## Generic Data Structures

```swift
struct Box<T> {
    var value: T
}
let intBox = Box(value: 10)
let stringBox = Box(value: "Hello")

print(intBox.value) // Output: 10
print(stringBox.value) // Output: "Hello"
```

## Generic Functions

```swift
func swapValues<T>(_ a: inout T, _ b: inout T) {
    let temp = a
    a = b
    b = temp
}

var a = 10
var b = 20
swapValues(&a, &b)
print(a) // Output: 20
print(b) // Output: 10

var c = "Hello"
var d = "World"
swapValues(&c, &d)
print(c) // Output: "World"
print(d) // Output: "Hello"
```

## Constraints on Generics

```swift
func sum<T: Numeric>(_ array: [T]) -> T {
    array.reduce(0, +)
}

print(sum([1, 1.5, 2])) // Output: 4.5

// This will not work because String is not Numeric
// print(sum(["a", "b", "c"]))
// Error: function 'sum' requires that 'String' conform to 'Numeric'
```

## Associated Types

```swift
protocol Foo {
    associatedtype T
    func foo() -> T
}
```

Associated types are used in protocols to define a placeholder for a type that will be specified later. They act as a generic placeholder. The exact type isn't defined in the protocol itself; instead, it's determined when a class, struct, or enum conforms to the protocol.

## Generic Protocols

```swift
protocol Storage {
    associatedtype Item
    func store(item: Item)
    func retrieve() -> Item?
}

class SimpleStorage<T>: Storage {
    private var items: [T] = []

    func store(item: T) {
        items.append(item)
    }

    func retrieve() -> T? {
        return items.isEmpty ? nil : items.removeLast()
    }
}

let intStorage = SimpleStorage<Int>()
intStorage.store(item: 42)
print(intStorage.retrieve() ?? "Empty")  // Output: 42
```

## Generic Typealiases

Generic typealiases allow us to create a new name for an existing type (i.e., they would not introduce a new type).

```swift
typealias StringDictionary<T> = [String: T]
typealias IntFunction<T> = (Int) -> Int
typealias Vector<T> = (T, T, T)
```
