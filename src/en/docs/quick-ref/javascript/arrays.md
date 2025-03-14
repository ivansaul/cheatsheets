# Arrays

## Create Array

```javascript
const fruits = ["apple", "orange", "banana"];

// Different data types
const data = [1, "chicken", false];
```

## Property .length

```javascript
const numbers = [1, 2, 3, 4];

numbers.length; // 4
```

## Index

```javascript
// Accessing an array element
const myArray = [100, 200, 300];

console.log(myArray[0]); // 100
console.log(myArray[1]); // 200
```

## Mutable chart

|           | add | remove | start | end |
| :-------- | :-: | :----: | :---: | :-: |
| `push`    | ✔  |        |       | ✔  |
| `pop`     |     |   ✔   |       | ✔  |
| `unshift` | ✔  |        |  ✔   |     |
| `shift`   |     |   ✔   |  ✔   |     |

## Array.push()

```javascript
// Adding a single element:
const cart = ["apple", "orange"];
cart.push("pear");

// Adding multiple elements:
const numbers = [1, 2];
numbers.push(3, 4, 5);
```

Add items to the end and returns the new array length.

## Array.pop()

```javascript
const fruits = ["apple", "orange", "banana"];

const fruit = fruits.pop(); // 'banana'
console.log(fruits); // ["apple", "orange"]
```

Remove an item from the end and returns the removed item.

## Array.shift()

```javascript
let cats = ["Bob", "Willy", "Mini"];

cats.shift(); // ['Willy', 'Mini']
```

Remove an item from the beginning and returns the removed item.

## Array.unshift()

```javascript
let cats = ["Bob"];

// => ['Willy', 'Bob']
cats.unshift("Willy");

// => ['Puff', 'George', 'Willy', 'Bob']
cats.unshift("Puff", "George");
```

Add items to the beginning and returns the new array length.

## Array.concat()

```javascript
const numbers = [3, 2, 1];
const newFirstNumber = 4;

// => [ 4, 3, 2, 1 ]
[newFirstNumber].concat(numbers);

// => [ 3, 2, 1, 4 ]
numbers.concat(newFirstNumber);
```

If you want to avoid mutating your original array, you can use concat.
