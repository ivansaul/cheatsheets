# Control flows : loops

## while loop

```dart
while (!dreamsAchieved) {
  workHard();
}
```

while loop check condition before iteration of the loop

## do-while loop

```dart
do {
  workHard();
} while (!dreamsAchieved);
```

do-while loop verifies the condition after the execution of the statements inside the loop

## for loop

```dart
for(int i=0; i< 10; i++){
    print(i);
}

var numbers = [1,2,3];
// for-in loop for lists
for(var number in numbers){
    print(number);
}
```

## for in loop

```dart
  // Define a list of numbers
  var numbers = [1, 2, 3, 4, 5];

  // Use a for-in loop to iterate over the list
  for (var number in numbers) {
    print(number);
  }

  // Define a list of strings
  var fruits = ['Apple', 'Banana', 'Cherry'];

  // Use a for-in loop to iterate over the list
  for (var fruit in fruits) {
    print(fruit);
  }
```
