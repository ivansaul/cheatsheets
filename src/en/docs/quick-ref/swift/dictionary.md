# Dictionary

## Base Dictionary

```swift
var dictionaryName = [
  "Key1": "Value1",
  "Key2": "Value2",
  "Key3": "Value3"
]
```

An `unordered` collection of pairs of data or key-value pairs

## Keys

```swift
var fruitStand = [
  "Coconuts": 12,
  "Pineapples": 12,
  "Papaya": 12
]
```

Each `key` is `unique` even if they all contain the same `value`

## Type Consistency

```swift
var numberOfSides = [
  "triangle": 3,
  "square": 4,
  "rectangle": 4
]
```

Contains only `String` keys and `Int` values

## Initialize and populate the dictionary

```swift
var employeeID = [
  "Hamlet": 1367,
  "Horatio": 8261,
  "Ophelia": 9318
]
```

## Initialize an empty dictionary

```swift
// initializer syntax:
var yearlyFishPopulation = [Int: Int]()

// Empty dictionary literal syntax:
var yearlyBirdPopulation: [Int: Int] = [:]
```

## add to dictionary

```swift
var pronunciation = [
  "library": "lai·breh·ree",
  "apple": "a·pl"
]
// new key: "programming", new value: "prow gra"
pronunciation["programming"] = "prow·gra"
```

## Delete key-value pair

```swift
var bookShelf = [
  "Goodnight": "Margaret Wise Brown",
  "The BFG": "Roald Dahl",
  "Falling Up": "Shel Silverstein",
  "No, David!": "David Shannon"
]
// remove value by setting key to nil
bookShelf["The BFG"] = nil

// remove value using .removeValue()
bookShelf.removeValue(forKey: "Goodnight")

// remove all values
bookShelf.removeAll()
```

## Modify the key-value pair

```swift
var change = [
  "Quarter": 0.29,
  "Dime": 0.15,
  "Nickel": 0.05
]

// Change the value using subscript syntax
change["Quarter"] = .25

// Change the value using .updateValue()
change.updateValue(.10, forKey: "Dime")
```

To change the value of a key-value pair, use the `.updateValue()` method or the subscript syntax by appending brackets
`[ ]` with the existing keys within to the name of the dictionary, then adding the assignment operator _(`=`)_ followed
by the modified value

## .isEmpty property

```swift
var bakery = [String:Int]()

// check if the dictionary is empty
print(bakery.isEmpty) // prints true
bakery["Cupcakes"] = 12
// check if the dictionary is empty
print(bakery.isEmpty) // print false
```

## .count property

```swift
var fruitStand = [
  "Apples": 12,
  "Oranges", 17
]
print(fruitStand.count) // print: 2
```

## Assigning values to variables

```swift
var hex = [
  "red": "#ff0000",
  "yellow": "#ffff00",
  "blue": "#0000ff",
]

print("Blue hexadecimal code \(hex["blue"])")
// print: blue hex code Optional("#0000ff")

if let redHex = hex["red"] {
  print("red hexadecimal code \(redHex)")
}
// print: red hex code #ff0000
```

Assigning the value of a key-value pair to a variable will return an optional value. To extract values, use the optional
expansion

## Traversing the dictionary

```swift
var emojiMeaning = [
  "🤔": "Thinking Face",
  "😪": "Sleepy Face",
  "😵": "Dizzy Face"
]
// loop through keys and values
for (emoji, meaning) in emojiMeaning {
  print("\(emoji) is called '\(meaning)Emoji'")
}
// iterate through keys only
for emoji in emojiMeaning.keys {
  print(emoji)
}
// iterate through values only
for meaning in emojiMeaning.values {
  print(meaning)
}
```
