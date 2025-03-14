# Scope

## Scope

```javascript
function myFunction() {
  var pizzaName = "Margarita";
  // Code here can use pizzaName
}

// Code here can't use pizzaName
```

## Block Scoped Variables

```javascript
const isLoggedIn = true;

if (isLoggedIn == true) {
  const statusMessage = "Logged in.";
}

// Uncaught ReferenceError...
console.log(statusMessage);
```

## Global Variables

```javascript
// Variable declared globally
const color = "blue";

function printColor() {
  console.log(color);
}

printColor(); // => blue
```

## let vs var

```javascript
for (let i = 0; i < 3; i++) {
  // This is the Max Scope for 'let'
  // i accessible ✔️
}
// i not accessible ❌
```

---

```javascript
for (var i = 0; i < 3; i++) {
  // i accessible ✔️
}
// i accessible ✔️
```

`var` is scoped to the nearest function block, and `let` is scoped to the nearest enclosing block.

## Loops with closures

```javascript
// Prints 3 thrice, not what we meant.
for (var i = 0; i < 3; i++) {
  setTimeout(_ => console.log(i), 10);
}
```

---

```javascript
// Prints 0, 1 and 2, as expected.
for (let j = 0; j < 3; j++) {
  setTimeout(_ => console.log(j), 10);
}
```

The variable has its own copy using `let`, and the variable has shared copy using `var`.
