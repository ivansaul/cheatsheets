# Conditionals

## Operators

- <a data-tooltip="Additive operator (also used for String concatenation)">+</a>
- <a data-tooltip="Subtraction operator">-</a>
- <a data-tooltip="Multiplication operator">\*</a>
- <a data-tooltip="Division operator">/</a>
- <a data-tooltip="Remainder operator">%</a>
- <a data-tooltip="Simple assignment operator">=</a>
- <a data-tooltip="Increment operator; increments a value by 1">++</a>
- <a data-tooltip="Decrement operator; decrements a value by 1">--</a>
- <a data-tooltip="Logical complement operator; inverts the value of a boolean">!</a>

{.marker-none .cols-4}

---

- <a data-tooltip="Equal to">==</a>
- <a data-tooltip="Not equal to">!=</a>
- <a data-tooltip="Greater than">></a>
- <a data-tooltip="Greater than or equal to">>=</a>
- <a data-tooltip="Less than"><</a>
- <a data-tooltip="Less than or equal to"><=</a>

{.marker-none .cols-4}

---

- <a data-tooltip="Conditional-AND">&&</a>
- <a data-tooltip="Conditional-OR">||</a>
- [?:](#ternary-operator){data-tooltip="Ternary (shorthand for if-then-else statement)"}

{.marker-none .cols-4}

---

- <a data-tooltip="Compares an object to a specified type">instanceof</a>

---

- <a data-tooltip="Unary bitwise complement">~</a>
- <a data-tooltip="Signed left shift"><<</a>
- <a data-tooltip="Signed right shift">>></a>
- <a data-tooltip="Unsigned right shift">>>></a>
- <a data-tooltip="Bitwise AND">&</a>
- <a data-tooltip="Bitwise exclusive OR">^</a>
- <a data-tooltip="Bitwise inclusive OR">|</a>

{.marker-none .cols-4}

## If else

```java
int k = 15;
if (k > 20) {
  System.out.println(1);
} else if (k > 10) {
  System.out.println(2);
} else {
  System.out.println(3);
}
```

## Switch

```java
int month = 3;
String str;
switch (month) {
  case 1:
    str = "January";
    break;
  case 2:
    str = "February";
    break;
  case 3:
    str = "March";
    break;
  default:
    str = "Some other month";
    break;
}

// Outputs: Result March
System.out.println("Result " + str);
```

## Ternary operator

```java
int a = 10;
int b = 20;
int max = (a > b) ? a : b;

// Outputs: 20
System.out.println(max);
```
