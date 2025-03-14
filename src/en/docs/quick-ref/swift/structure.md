# Structure

## Structure Creation

```swift
struct Building {
  var address: String
  var floors: Int
  init(address: String, floors: Int) {
    self.address = address
    self.floors = floors
  }
}
```

Structs or structs are used to programmatically represent real-life objects in code. A structure is created using the
`struct` keyword, followed by its name, followed by a body containing its properties and methods

## Default property values

```swift
struct Car {
  var numOfWheels = 4
  var topSpeed = 80
}

var reliantRobin = Car(numOfWheels: 3)

print(reliantRobin.numOfWheels) // prints: 3
print(reliantRobin.topSpeed)    // print: 80
```

## Structural instance creation

```swift
struct Person {
  var name: String
  var age: Int

  init(name: String, age: Int) {
    self.name = name
    self.age = age
  }
}

// Person instance:
var morty = Person(name: "Peter", age: 14)
```

## init() method

```swift
struct TV {
  var size: Int
  var type: String

  init(size: Int, type: String) {
    self.size = size
    self.type = type
  }
}
```

Using the `TV` class

```swift
var newTV = TV(size: 65, type: "LED")
```

## Check type

```swift
print(type(of: "abc")) // print: String
print(type(of: 123))   // print: 123
```

## Mutation method (mutating)

```swift
struct Menu {
  var menuItems = ["Fries", "Burgers"]
  mutating func addToMenu(dish: String) {
    self.menuItems.append(dish)
  }
}
```

Using the `Menu` class

```swift
var dinerMenu = Menu()
dinerMenu.addToMenu(dish: "Toast")
print(dinerMenu.menuItems)
// prints: ["Fries", "Burgers", "Toast"]
```

## Structural methods

```swift
struct Dog {
  func bark() {
    print("Woof")
  }
}
let fido = Dog()
fido.bark() // prints: Woof
```
