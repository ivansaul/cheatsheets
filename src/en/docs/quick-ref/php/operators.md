# Operators

## Arithmetic

| -    | -              |
| ---- | -------------- |
| `+`  | Addition       |
| `-`  | Subtraction    |
| `*`  | Multiplication |
| `/`  | Division       |
| `%`  | Modulo         |
| `**` | Exponentiation |

## Assignment

| -        | -                   |
| -------- | ------------------- |
| `a += b` | Same as `a = a + b` |
| `a -= b` | Same as `a = a – b` |
| `a *= b` | Same as `a = a * b` |
| `a /= b` | Same as `a = a / b` |
| `a %= b` | Same as `a = a % b` |

## Comparison

| -     | -                            |
| ----- | ---------------------------- |
| `==`  | Equal                        |
| `===` | Identical                    |
| `!=`  | Not equal                    |
| `<>`  | Not equal                    |
| `!==` | Not identical                |
| `<`   | Less than                    |
| `>`   | Greater than                 |
| `<=`  | Less than or equal           |
| `>=`  | Greater than or equal        |
| `<=>` | Less than/equal/greater than |

## Logical

| -     | -            |
| ----- | ------------ |
| `and` | And          |
| `or`  | Or           |
| `xor` | Exclusive or |
| `!`   | Not          |
| `&&`  | And          |
| `||`  | Or           |

## Arithmetic

```php
// Arithmetic
$sum        = 1 + 1; // 2
$difference = 2 - 1; // 1
$product    = 2 * 2; // 4
$quotient   = 2 / 1; // 2

// Shorthand arithmetic
$num = 0;
$num += 1;       // Increment $num by 1
echo $num++;     // Prints 1 (increments after evaluation)
echo ++$num;     // Prints 3 (increments before evaluation)
$num /= $float;  // Divide and assign the quotient to $num
```

## Bitwise

| -    | -                  |
| ---- | ------------------ |
| `&`  | And                |
| `|`  | Or (inclusive or)  |
| `^`  | Xor (exclusive or) |
| `~`  | Not                |
| `<<` | Shift left         |
| `>>` | Shift right        |
