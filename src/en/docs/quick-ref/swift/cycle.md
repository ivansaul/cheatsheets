# Cycle

## Scope

```swift
let zeroToThree = 0...3
//zeroToThree: 0, 1, 2, 3
```

## Stride() Function

```swift
for oddNum in stride(from: 1, to: 5, by: 2) {
  print(oddNum)
}
// print: 1
// print: 3
```

## For-in Loop

```swift
for char in "hehe" {
  print(char)
}
// print: h
// print: e
// print: h
// print: e
```

## Continue keyword

```swift
for num in 0...5 {
  if num % 2 == 0 {
    continue
  }
  print(num)
}
// print: 1
// print: 3
// print: 5
```

The `continue` keyword will force the loop to continue for the next iteration

## Break Keyword

```swift
for char in "supercalifragilistic" {
if char == "c" {
    break
  }
  print(char)
}
// print: s
// print: u
// print: p
// print: e
// print: r
```

## Use Underscores

```swift
for _ in 1...3 {
  print("Ole")
}
// print: Ole
// print: Ole
// print: Ole
```

## While Loop

```swift
var counter = 1
var stopNum = Int.random(in: 1...10)

while counter < stopNum {
  print(counter)
  counter += 1
}
// loop to print until the stop condition is met
```

A `while` loop accepts a condition and keeps executing its body code while the provided condition is `true`. If the
condition is never false, the loop will keep running and the program will get stuck in an `infinite loop`
