# Functions

## Function declaration and definition

```c
int main(void) {
  printf("Hello World!\n");

  return 0;
}
```

The function consists of two parts

```c
void myFunction() { // declaration declaration
  // function body (code to be executed) (definition)
}
```

---

- `Declaration` declares the function name, return type and parameters _(if any)_
- `Definition` function body _(code to execute)_

---

```c
// function declaration
void myFunction();
// main method
int main() {
  myFunction(); // --> call the function

  return 0;
}

void myFunction() {// Function definition
  printf("Good evening!\n");
}
```

## Call function

```c
// create function
void myFunction() {
  printf("Good evening!\n");
}

int main() {
  myFunction(); // call the function
  myFunction(); // can be called multiple times

  return 0;
}
// Output -> "Good evening!"
// Output -> "Good evening!"
```

## Function parameters

```c
void myFunction(char name[]) {
  printf("Hello %s\n", name);
}

int main() {
  myFunction("Liam");
  myFunction("Jenny");

  return 0;
}
// Hello Liam
// Hello Jenny
```

## Multiple parameters

```c
void myFunction(char name[], int age) {
  printf("Hi %s, you are %d years old.\n",name,age);
}
int main() {
  myFunction("Liam", 3);
  myFunction("Jenny", 14);

  return 0;
}
// Hi Liam you are 3 years old.
// Hi Jenny you are 14 years old.
```

## Return value

```c
int myFunction(int x) {
  return 5 + x;
}

int main() {
  printf("Result: %d\n", myFunction(3));
  return 0;
}
// output 8 (5 + 3)
```

Two parameters

```c
int myFunction(int x, int y) {
  return x + y;
}

int main() {
  printf("Result: %d\n", myFunction(5, 3));
  // store the result in a variable
  int result = myFunction(5, 3);
  printf("Result = %d\n", result);

  return 0;
}
// result: 8 (5 + 3)
// result = 8 (5 + 3)
```

## Recursive example

```c
int sum(int k);

int main() {
  int result = sum(10);
  printf("%d\n", result);

  return 0;
}

int sum(int k) {
  if (k > 0) {
    return k + sum(k -1);
  } else {
    return 0;
  }
}
```

## Mathematical functions

```c
#include <math.h>

void main(void) {
  printf("%f\n", sqrt(16)); // square root
  printf("%f\n", ceil(1.4)); // round up (round)
  printf("%f\n", floor(1.4)); // round down (round)
  printf("%f\n", pow(4, 3)); // x(4) to the power of y(3)
}
```

---

- `abs(x)` absolute value
- `acos(x)` arc cosine value
- `asin(x)` arc sine
- `atan(x)` arc tangent
- `cbrt(x)` cube root
- `cos(x)` cosine
- the value of `exp(x)` Ex
- `sin(x)` the sine of x
- tangent of `tan(x)` angle
