# Function

## Basic functions

```swift
func washCar() -> Void {
  print("Soap")
  print("Scrub")
  print("Rinse")
  print("Dry")
}
```

## Call functions

```swift
func greetLearner() {
 print("Welcome to CheatSheets.zip!")
}
// function call:
greetLearner()
// print: Welcome to CheatSheets.zip!
```

## return value

```swift
let birthYear = 1994
var currentYear = 2020

func findAge() -> Int {
  return currentYear-birthYear
}

print(findAge()) // prints: 26
```

## Multiple parameters

```swift
func convertFracToDec(numerator: Double, denominator: Double) -> Double {
  return numerator / denominator
}

let decimal = convertFracToDec(numerator: 1.0, denominator: 2.0)
print(decimal) // prints: 0.5
```

## Omit parameter labels

```swift
func findDiff(_ a: Int, b: Int) -> Int {
  return a -b
}

print(findDiff(6, b: 4)) // prints: 2
```

## return multiple values

```swift
func smartphoneModel() -> (name: String, version: String, yearReleased: Int) {
  return ("iPhone", "8 Plus", 2017)
}
let phone = smartphoneModel()

print(phone.name)         // print: iPhone
print(phone.version)      // print: 8 Plus
print(phone.yearReleased) // print: 2017
```

## Parameters & Arguments

```swift
func findSquarePerimet(side: Int) -> Int {
  return side *4
}

let perimeter = findSquarePerimet(side: 5)
print(perimeter) // print: 20

// Parameter: side
// Argument: 5
```

## Implicit return

```swift
func nextTotalSolarEclipse() -> String {
  "April 8th, 2024 🌎"
}

print(nextTotalSolarEclipse())
// print: April 8th, 2024 🌎
```

## Default parameters

```swift
func greet(person: String = "guest") {
  print("Hello \(person)")
}
greet() // Hello guest
greet(person: "Aliya") // Hello Aliya
```

## Input and output parameters

```swift
var currentSeason = "Winter"

func season(month: Int, name: inout String) {
  switch month {
    case 1...2:
      name = "Winter ⛄️"
    case 3...6:
      name = "Spring 🌱"
    case 7...9:
      name = "Summer ⛱"
    case 10...11:
      name = "Autumn 🍂"
    default:
      name = "Unknown"
  }
}
season(month: 4, name: &currentSeason)

print(currentSeason) // Spring 🌱
```

## variable parameter

```swift
func totalStudent(data: String...) -> Int {
  let numStudents = data.count
  return numStudents
}

print(totalStudent(data: "Denial", "Peter"))
// print: 2
```

## Optional parameters

```swift
func getFirstInitial(from name: String?) -> String? {
  return name?.first
}
```

Functions can accept optional types and return optional types. When a function cannot return a reasonable instance of
the requested type, it should return `nil`
