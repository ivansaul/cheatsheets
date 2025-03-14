# Class

## reference type (class)

```swift
class Player {
  var name: String

  init(name: String) {
    self.name = name
  }
}

var player1 = Player(name: "Tomoko")
var player2 = player1
player2.name = "Isabella"

print(player1.name) // Isabella
print(player2.name) // Isabella
```

## instance of the class

```swift
class Person {
  var name = ""
  var age = 0
}

var sonny = Person()
// sonny is now an instance of Person
```

## init() method

```swift
class Fruit {
  var hasSeeds = true
  var color: String

  init(color: String) {
    self.color = color
  }
}
```

Using the Fruit class

```swift
let apple = Fruit(color: "red")
```

A class can be initialized using the `init()` method and the corresponding initialization properties. In the `init()`
method, the `self` keyword is used to refer to the actual instance of the class assigning property values

## Class Attributes

```swift
var ferris = Student()

ferris.name = "Ferris Bueller"
ferris.year = 12
ferris.gpa = 3.81
ferris.honors = false
```

## Inherit

Suppose we have a BankAccount class:

```swift
class BankAccount {
  var balance = 0.0
  func deposit(amount: Double) {
    balance += amount
  }
  func withdraw(amount: Double) {
    balance -= amount
  }
}
```

`SavingsAccount` extends `BankAccount` class

```swift
class SavingsAccount: BankAccount {
  var interest = 0.0

  func addInterest() {
    let interest = balance *0.005
    self.deposit(amount: interest)
  }
}
```

The new `SavingsAccount` class (subclass) automatically gets all the characteristics of the `BankAccount` class
(superclass). Additionally, the `SavingsAccount` class defines an `.interest` property and an `.addInterest()` method.

## Example

use data type

```swift
class Student {
  var name: String
  var year: Int
  var gpa: Double
  var honors: Bool
}
```

Use default property values

```swift
class Student {
  var name = ""
  var gpa = 0.0
  var honors = false
}
```

## This is an example of a struct definition and a class definition

```swift
struct Resolution {
  var width = 0
  var height = 0
}
class VideoMode {
  var resolution = Resolution()
  var interlaced = false
  var frameRate = 0.0
  var name: String?
}
```

The `Resolution` structure definition and the `VideoMode` class definition only describe the appearance of `Resolution`
or `VideoMode`, create an instance of the structure or class:

```swift
let resolution = Resolution(width: 1920)
let someVideoMode = VideoMode()
```
