# Functions

## Function Definition

```javascript
// Defining the function:
function sum(num1, num2) {
  return num1 + num2;
}

// Calling the function:
sum(3, 6); // 9
```

## Anonymous Functions

```javascript
// Named function
function rocketToMars() {
  return "BOOM!";
}

// Anonymous function
const rocketToMars = function () {
  return "BOOM!";
};
```

## Arrow Functions (ES6)

### With two arguments

```javascript
const sum = (param1, param2) => {
  return param1 + param2;
};
console.log(sum(2, 5)); // => 7
```

### With no arguments

```javascript
const printHello = () => {
  console.log("hello");
};
printHello(); // => hello
```

### With a single argument

```javascript
const checkWeight = (weight) => {
  console.log(`Weight : ${weight}`);
};
checkWeight(25); // => Weight : 25
```

### Concise arrow functions

```javascript
const multiply = (a, b) => a * b;
// => 60
console.log(multiply(2, 30));
```

[Arrow function](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/Arrow_functions) available
starting ES2015

## return Keyword

```javascript
// With return
function sum(num1, num2) {
  return num1 + num2;
}

// The function doesn't output the sum
function sum(num1, num2) {
  num1 + num2;
}
```

## Calling Functions

```javascript
// Defining the function
function sum(num1, num2) {
  return num1 + num2;
}

// Calling the function
sum(2, 4); // 6
```

## Function Expressions

```javascript
const dog = function () {
  return "Woof!";
};
```

## Function Parameters

```javascript
// The parameter is name
function sayHello(name) {
  return `Hello, ${name}!`;
}
```

## Function Declaration

```javascript
function add(num1, num2) {
  return num1 + num2;
}
```
