# C Preprocessor

## Preprocessor Directives

| Directive  | Description                                                          |
| ---------- | :------------------------------------------------------------------- |
| `#define`  | define a macro                                                       |
| `#include` | include a source code file                                           |
| `#undef`   | undefined macro                                                      |
| `#ifdef`   | Returns true if the macro is defined                                 |
| `#ifndef`  | Returns true if the macro is not defined                             |
| `#if`      | Compile the following code if the given condition is true            |
| `#else`    | Alternative to `#if`                                                 |
| `#elif`    | If the `#if` condition is false, the current condition is `true`     |
| `#endif`   | End a `#if...#else` conditional compilation block                    |
| `#error`   | Print an error message when standard error is encountered            |
| `#pragma`  | Issue special commands to the compiler using the standardized method |

```c
// replace all MAX_ARRAY_LENGTH with 20
#define MAX_ARRAY_LENGTH 20
// Get stdio.h from the system library
#include <stdio.h>
// Get myheader.h in the local directory
#include "myheader.h"
#undef FILE_SIZE
#define FILE_SIZE 42 // undefine and define to 42
```

## Predefined macros

| Macro      | Description                                                           |
| ---------- | :-------------------------------------------------------------------- |
| `__DATE__` | The current date, a character constant in the format "MMM DD YYYY"    |
| `__TIME__` | The current time, a character constant in the format "HH:MM:SS"       |
| `__FILE__` | This will contain the current filename, a string constant             |
| `__LINE__` | This will contain the current line number, a decimal constant         |
| `__STDC__` | Defined as `1` when the compiler compiles against the `ANSI` standard |

`ANSI C` defines a number of macros that you can use, but you cannot directly modify these predefined macros

### Predefined macro example

```c
#include <stdio.h>

int main(void) {
  printf("File: %s\n", __FILE__);
  printf("Date: %s\n", __DATE__);
  printf("Time: %s\n", __TIME__);
  printf("Line: %d\n", __LINE__);
  printf("ANSI: %d\n", __STDC__);
}
```

## Macro continuation operator (\\)

A macro is usually written on a single line.

```c
#define message_for(a, b) \
    printf(#a " and " #b ": We love you!\n")
```

If the macro is too long to fit on a single line, use the macro continuation operator `\`

## String Constantization Operator (#)

```c
#include <stdio.h>

#define message_for(a, b) \
  printf(#a " and " #b ": We love you!\n")

int main(void) {
  message_for(Carole, Debra);

  return 0;
}
```

When the above code is compiled and executed, it produces the following result:

```
Carole and Debra: We love you!
```

When you need to convert a macro parameter to a string constant, use the string constant operator `#`

## tag paste operator (##)

```c
#include <stdio.h>

#define tokenpaster(n) printf ("Token " #n " = %d\n", token##n)

int main(void) {
  int token34 = 40;
  tokenpaster(34);

  return 0;
}
```

## defined() operator

```c
#include <stdio.h>

#if !defined (MESSAGE)
   #define MESSAGE "You wish!"
#endif

int main(void) {
  printf("Here is the message: %s\n", MESSAGE);

  return 0;
}
```

## Parameterized macros

```c
int square(int x) {
  return x * x;
}
```

The macro rewrites the above code as follows:

```c
#define square(x) ( (x) * (x) )
```

No spaces are allowed between the macro name and the opening parenthesis

```c
#include <stdio.h>
#define MAX(x,y) ( (x) > (y) ? (x) : (y) )

int main(void) {
  printf("Max between 20 and 10 is %d\n", MAX(10, 20));

  return 0;
}
```
