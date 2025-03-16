# Data Types

## Basic data types

| Data Type            | Size             | Range                              | Description                         |
| -------------------- | ---------------- | ---------------------------------- | :---------------------------------- |
| `char`               | 1 byte           | `−128` ~ `127`                     | single character/alphanumeric/ASCII |
| `signed char`        | 1 byte           | `−128` ~ `127`                     |                                     |
| `unsigned char`      | 1 byte           | `0` ~ `255`                        |                                     |
| `int`                | `2` to `4` bytes | `−32,768` ~ `32,767`               | store integers                      |
| `signed int`         | 2 bytes          | `−32,768` ~ `32,767`               |                                     |
| `unsigned int`       | 2 bytes          | `0` ~ `65,535`                     |                                     |
| `short int`          | 2 bytes          | `−32,768` ~ `32,767`               |                                     |
| `signed short int`   | 2 bytes          | `−32,768` ~ `32,767`               |                                     |
| `unsigned short int` | 2 bytes          | `0` ~ `65,535`                     |                                     |
| `long int`           | 4 bytes          | `-2,147,483,648` ~ `2,147,483,647` |                                     |
| `signed long int`    | 4 bytes          | `-2,147,483,648` ~ `2,147,483,647` |                                     |
| `unsigned long int`  | 4 bytes          | `0` ~ `4,294,967,295`              |                                     |
| `float`              | 4 bytes          | `3.4E-38` ~ `3.4E+38`              |                                     |
| `double`             | 8 bytes          | `1.7E-308` ~ `1.7E+308`            |                                     |
| `long double`        | 10 bytes         | `3.4E-4932` ~ `1.1E+4932`          |                                     |

## Data types

```c
// create variables
int myNum = 5; // integer
float myFloatNum = 5.99; // floating point number
char myLetter = 'D'; // string
// High precision floating point data or numbers
double myDouble = 3.2325467;
// print output variables
printf("%d\n", myNum);
printf("%f\n", myFloatNum);
printf("%c\n", myLetter);
printf("%lf\n", myDouble);
```

---

| Data Type | Description                          |
| :-------- | :----------------------------------- |
| `char`    | character type                       |
| `short`   | short integer                        |
| `int`     | integer type                         |
| `long`    | long integer                         |
| `float`   | single-precision floating-point type |
| `double`  | double-precision floating-point type |
| `void`    | no type                              |

## Basic format specifiers

| Format Specifier | Data Type                                             |
| ---------------- | :---------------------------------------------------- |
| `%d` or `%i`     | `int` integer                                         |
| `%f`             | `float` single-precision decimal type                 |
| `%lf`            | `double` high precision floating point data or number |
| `%c`             | `char` character                                      |
| `%s`             | for `strings` strings                                 |

## Separate base format specifiers

| Format      | Short         | Int         | Long          |
| ----------- | ------------- | ----------- | :------------ |
| Octal       | `%ho`         | `%o`        | `%lo`         |
| Decimal     | `%hd`         | `%d`        | `%ld`         |
| Hexadecimal | `%hx` / `%hX` | `%x` / `%X` | `%lx` / `%lX` |

## Data format example

```c
int myNum = 5;
float myFloatNum = 5.99; // floating point number
char myLetter = 'D';     // string
// print output variables
printf("%d\n", myNum);
printf("%f\n", myFloatNum);
printf("%c\n", myLetter);
```
