# Getting Started

## Introduction

JavaScript is a lightweight, interpreted programming language.

- [JSON cheatsheet](/json) _(cheatsheets.zip)_
- [Regex in JavaScript](/regex#regex-in-javascript) _(cheatsheets.zip)_

## Console

```javascript
// => Hello world!
console.log("Hello world!");

// => Hello CheatSheets.zip
console.warn("hello %s", "CheatSheets.zip");

// Prints error message to stderr
console.error(new Error("Oops!"));
```

## Numbers

```javascript
let amount = 6;
let price = 4.99;
```

## Variables

```javascript
let x = null;
let name = "Tammy";
const found = false;

// => Tammy, false, null
console.log(name, found, x);

var a;
console.log(a); // => undefined
```

## Strings

```javascript
let single = "Wheres my bandit hat?";
let double = "Wheres my bandit hat?";

// => 21
console.log(single.length);
```

## Arithmetic Operators

```javascript
5 + 5 = 10     // Addition
10 - 5 = 5     // Subtraction
5 * 10 = 50    // Multiplication
10 / 5 = 2     // Division
10 % 5 = 0     // Modulo
```

## Comments

```javascript
// This line will denote a comment

/*
The below configuration must be
changed before deployment.
*/
```

## Assignment Operators

```javascript
let number = 100;

// Both statements will add 10
number = number + 10;
number += 10;

console.log(number);
// => 120
```

## String Interpolation

```javascript
let age = 7;

// String concatenation
"Tommy is " + age + " years old.";

// String interpolation
`Tommy is ${age} years old.`;
```

## let Keyword

```javascript
let count;
console.log(count); // => undefined
count = 10;
console.log(count); // => 10
```

## const Keyword

```javascript
const numberOfColumns = 4;

// TypeError: Assignment to constant...
numberOfColumns = 8;
```
