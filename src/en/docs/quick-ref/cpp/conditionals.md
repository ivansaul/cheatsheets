# Conditionals

## If Clause

```cpp
if (a == 10) {
    // do something
}
```

---

```cpp
int number = 16;

if (number % 2 == 0)
{
    std::cout << "even";
}
else
{
    std::cout << "odd";
}

// Outputs: even
```

## Else if Statement

```cpp
int score = 99;
if (score == 100) {
    std::cout << "Superb";
}
else if (score >= 90) {
    std::cout << "Excellent";
}
else if (score >= 80) {
    std::cout << "Very Good";
}
else if (score >= 70) {
    std::cout << "Good";
}
else if (score >= 60)
    std::cout << "OK";
else
    std::cout << "What?";
```

## Operators

### Relational Operators

|          |                              |
| -------- | ---------------------------- |
| `a == b` | a is equal to b              |
| `a != b` | a is NOT equal to b          |
| `a < b`  | a is less than b             |
| `a > b`  | a is greater b               |
| `a <= b` | a is less than or equal to b |
| `a >= b` | a is greater or equal to b   |

### Assignment Operators

| Example  | Equivalent to    |
| -------- | ---------------- |
| `a += b` | _Aka_ a = a + b  |
| `a -= b` | _Aka_ a = a - b  |
| `a *= b` | _Aka_ a = a \* b |
| `a /= b` | _Aka_ a = a / b  |
| `a %= b` | _Aka_ a = a % b  |

### Logical Operators

| Example                     | Meaning                |
| --------------------------- | ---------------------- |
| `exp1 && exp2`              | Both are true _(AND)_  |
| <code>exp1 \|\| exp2</code> | Either is true _(OR)_  |
| `!exp`                      | `exp` is false _(NOT)_ |

### Bitwise Operators

| Operator            | Description             |
| ------------------- | ----------------------- |
| `a & b`             | Binary AND              |
| <code>a \| b</code> | Binary OR               |
| `a ^ b`             | Binary XOR              |
| `~ a`               | Binary One's Complement |
| `a << b`            | Binary Shift Left       |
| `a >> b`            | Binary Shift Right      |

## Ternary Operator

```
           ┌── True ──┐
Result = Condition ? Exp1 : Exp2;
           └───── False ─────┘
```

---

```cpp
int x = 3, y = 5, max;
max = (x > y) ? x : y;

// Outputs: 5
std::cout << max << std::endl;
```

---

```cpp
int x = 3, y = 5, max;
if (x > y) {
    max = x;
} else {
    max = y;
}
// Outputs: 5
std::cout << max << std::endl;
```

## Switch Statement

```cpp
int num = 2;
switch (num) {
    case 0:
        std::cout << "Zero";
        break;
    case 1:
        std::cout << "One";
        break;
    case 2:
        std::cout << "Two";
        break;
    case 3:
        std::cout << "Three";
        break;
    default:
        std::cout << "What?";
        break;
}
```
