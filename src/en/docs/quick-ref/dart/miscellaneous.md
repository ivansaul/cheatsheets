# Miscellaneous

## Null and Null aware

```dart
int x; // The initial value of any object is null

// ?? null aware operator

x ??=6; // ??= assignment operator, which assigns a value of a variable only if that variable is currently null
print(x); //Print: 6

x ??=3;
print(x); // Print: 6 - result is still 6

print(null ?? 10); // Prints: 10. Display the value on the left if it's not null else return the value on the right
```

## Ternary Operator

```dart
// condition ? exprIfTrue : exprIfFalse
bool isAvailable;

isAvailable ? orderproduct() : addToFavourite();
```

## Spread Operator (...)

```dart
// to insert multiple values into a collection.
var list = [1, 2, 3];
var list2 = [0, ...list];

print(list2.length); //Print: 4
```

## Cascade notation (..)

```dart
// allows you to make a sequence of operations on the same object

// rather than doing this
var user = User();
user.name = "Nicola";
user.email = "nicola@g.c";
user.age = 24;

// you can do this
var user = User()
  ..name = "Nicola"
  ..email = "nicola@g.c"
  ..age = 24;
```

## Conditional Property Access

```dart
userObject?.userName

//The code snippet above is equivalent to following:
(userObject != null) ? userObject.userName : null

//You can chain multiple uses of ?. together in a single expression
userObject?.userName?.toString()

// The preceeding code returns null and never calls toString() if either userObject or userObject.userName is null
```

## enum in dart

```dart
defination: An enum (short for "enumeration") is a special data type that enables a variable to be a set of predefined constants. Enums are used to define variables that can only take one out of a small set of possible values. They help make code more readable and less error-prone by providing meaningful names to these sets of values.

// Define the enum
enum TrafficLight {
  red,
  yellow,
  green
}

// A function that prints a message based on the traffic light state
void printTrafficLightMessage(TrafficLight light) {
  switch (light) {
    case TrafficLight.red:
      print('Stop!');
      break;
    case TrafficLight.yellow:
      print('Get ready...');
      break;
    case TrafficLight.green:
      print('Go!');
      break;
  }
}

void main() {
  // Example usage of the enum
  TrafficLight currentLight = TrafficLight.green;

  // Print the message for the current traffic light state
  printTrafficLightMessage(currentLight);
}


```
