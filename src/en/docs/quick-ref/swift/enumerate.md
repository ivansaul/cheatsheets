# Enumerate

## Define the enumeration

```swift
enum Day {
  case monday
  case tuesday
  case wednesday
  case thursday
  case friday
  case saturday
  case sunday
}

let casualWorkday: Day = .friday
```

## Switch statement

```swift
enum Dessert {
  case cake(flavor: String)
  case vanillaIceCream(scoops: Int)
  case brownie
}

let customerOrder: Dessert = .cake(flavor: "Red Velvet")
switch customerOrder {
  case let .cake(flavor):
    print("You ordered a \(flavor) cake")
  case .brownie:
    print("You ordered a chocolate cake")
}
// prints: "You ordered a red velvet cake"
```

## CaseIterable

```swift
enum Season: CaseIterable {
  case winter
  case spring
  case summer
  case falls
}

for season in Season.allCases {
  print(season)
}
```

Add conformance to the `CaseIterable` protocol to access the `allCases` property, which returns an array of all cases of
the enumeration

## Original value

```swift
enum Beatle: String {
  case john paul george ringo
}

print("The Beatles are \(Beatle.john.rawValue).")
// print: The Beatles are john.
```

## Related values

```swift
enum Dessert {
  case cake(flavor: String)
  case vanillaIceCream(scoops: Int)
  case brownie
}

let order: Dessert = .cake(flavor: "Red Velvet")
```

## instance method

```swift
enum Traffic {
  case light
  case heavy

  mutating func reportAccident() {
    self = .heavy
  }
}

var currentTraffic: Traffic = .light

currentTraffic.reportAccident()
// currentTraffic is now .heavy
```

Just like classes and structs, enumerations can have instance methods. If an instance method mutates the value of the
enum, it needs to be marked `mutating`

## Initialize from primitive value

```swift
enum Hello: String {
  case english = "Hello"
  case japanese = "Hello!"
  case emoji = "👋"
}
let hello1 = Hello(rawValue: "Hello!")
let hello2 = Hello(rawValue: "Привет")
print(hello1) // Optional(Hello.japanese)
print(hello2) // nil
```

## Computed properties

```swift
enum ShirtSize: String {
  case small = "S"
  case medium = "M"
  case large = "L"
  case extraLarge = "XL"
  var description: String {
    return "The size of this shirt is \(self.rawValue)"
  }
}
```
