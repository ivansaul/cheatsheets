# Arrays and collections

## Array

```swift
var scores = [Int]()
// array is empty: []
```

## `.count` Property

```swift
var grocery = ["🥓", "🥞", "🍪", "🥛", "🍊"]
print(grocery.count)
// print: 5
```

## Index

The index refers to the item's position in the ordered list, and a single element is retrieved from the array using the
subscript syntax `array[index]`.

```swift
var vowels = ["a", "e", "i", "o", "u"]

print(vowels[0]) // prints: a
print(vowels[1]) // prints: e
print(vowels[2]) // print: i
print(vowels[3]) // prints: o
print(vowels[4]) // prints: u
```

Note: Swift arrays are zero-indexed, meaning the first element has index 0.

## Initialize With Array Literal

```swift
// use type inference:
var snowfall = [2.4, 3.6, 3.4, 1.8, 0.0]
// explicit type:
var temp: [Int] = [33, 31, 30, 38, 44]
```

## Initialize With Default Value

```swift
var teams = [Int](repeating: 0, count: 3)
print(teams) // prints: [0, 0, 0]
// or with Array type
var sizes = Array<Int>(repeating: 0, count: 3)
print(sizes) // prints: [0, 0, 0]
```

## `.append()` Method and `+=` Operator

```swift
var gymBadges = ["Boulder", "Cascade"]
gymBadges.append("Thunder")
gymBadges += ["Rainbow", "Soul"]
// ["Boulder", "Cascade", "Thunder",
// "Rainbow", "Soul"]
```

## `.insert()` and `.remove()` Methods

```swift
var moon = ["🌖", "🌗", "🌘", "🌑"]
moon.insert("🌕", at: 0)
// ["🌕", "🌖", "🌗", "🌘", "🌑"]

moon.remove(at: 4)
// ["🌕", "🌖", "🌗", "🌘"]
```

## Iterate Over an Array

```swift
var employees = ["Peter", "Denial", "Jame"]
for person in employees {
  print(person)
}
// print: Peter
// print: Denial
// print: Jam
```

## Collection (Set)

```swift
var paintingsInMOMA: Set = [
  "The Dream",
  "The Starry Night",
  "The False Mirror"
]
```

We can use a collection (`Set`) to store `unique` elements of the same data type

## Empty Collection (Set)

```swift
var team = Set<String>()

print(team)
// print: []
```

## Populate the Collection

```swift
var vowels: Set = ["a", "e", "i", "o","u"]
```

To create a set filled with values, use the `Set` keyword before the assignment operator.

## `.insert()`

```swift
var cookieJar: Set = [
  "Chocolate Chip",
  "Oatmeal Raisin"
]
// add a new element
cookieJar.insert("Peanut Butter Chip")
```

## `.remove()` and `.removeAll()` Methods

```swift
var oddNumbers: Set = [1, 2, 3, 5]

// remove existing element
oddNumbers.remove(2)
// remove all elements
oddNumbers.removeAll()
```

## `contains()`

```swift
var names: Set = ["Rosa", "Doug", "Waldo"]
print(names.contains("Lola")) // print: false

if names.contains("Waldo"){
  print("There's Waldo!")
} else {
  print("Where's Waldo?")
}
// print: There's Waldo!
```

## `.isEmpty` Property

```swift
var emptyList = [String]()
print(emptyList.isEmpty)     // print: true

var populatedList: [Int] = [1, 2, 3]
print(populatedList.isEmpty) // print: false
```

## Iterate Over a Collection

```swift
var recipe: Set = ["Egg", "Flour", "Sugar"]

for ingredient in recipe {
  print ("Include \(ingredient) in the recipe")
}
```

## `.isEmpty` Property

```swift
var emptySet = Set<String>()
print(emptySet.isEmpty)     // print: true

var populatedSet: Set = [1, 2, 3]
print(populatedSet.isEmpty) // print: false
```

## `.count` Property

```swift
var band: Set = ["Peter", "Denial", "Jame"]

print("The band has \(band.count) players.")
// print: Band has 4 players.
```

## `.intersection()` Intersection

```swift
var setA: Set = ["A", "B", "C", "D"]
var setB: Set = ["C", "D", "E", "F"]

var setC = setA.intersection(setB)
print(setC) // print: ["D", "C"]
```

## `.union()`

```swift
var setA: Set = ["A", "B", "C", "D"]
var setB: Set = ["C", "D", "E", "F"]

var setC = setA.union(setB)
print(setC)
// print: ["B", "A", "D", "F", "C", "E"]
```

## `.symmetricDifference()` Symmetric Difference

```swift
var setA: Set = ["A", "B", "C", "D"]
var setB: Set = ["C", "D", "E", "F"]

var setC = setA.symmetricDifference(setB)
print(setC)
// print: ["B", "E", "F", "A"]
```

## `.subtracting()` Subtraction

```swift
var setA: Set = ["A", "B", "C", "D"]
var setB: Set = ["C", "D"]

var setC = setA.subtracting(setB)
print(setC)
// print: ["B", "A"]
```
