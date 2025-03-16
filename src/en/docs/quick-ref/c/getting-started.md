# Getting Started

## hello.c

```c
#include <stdio.h>

int main(void) {
  printf("Hello World!\n");

  return 0;
}
```

Compile `hello.c` file with `gcc`

```bash
gcc -Wall -g hello.c -o hello
```

Run the compiled binary `hello`

```bash
./hello
```

Output => Hello World!

## Variables

```c
int myNum = 15;

int myNum2; // do not assign, then assign
myNum2 = 15;

int myNum3 = 15; // myNum3 is 15
myNum3 = 10;     // myNum3 is now 10

float myFloat = 5.99; // floating point number
char myLetter = 'D';  // character

int x = 5;
int y = 6;
int sum = x + y; // add variables to sum

// declare multiple variables
int a = 5, b = 6, c = 50;
```

## Constants

```c
const int minutesPerHour = 60;
const float PI = 3.14;
```

Best Practices

```c
const int BIRTHYEAR = 1980;
```

## Comment

```c
// this is a comment
printf("Hello World!\n"); // Can comment anywhere in file

/*Multi-line comment, print Hello World!
to the screen, it's awesome */
```

## Print text

```c
printf("I am learning C.\n");
int testInteger = 5;
printf("Number = %d\n", testInteger);

float f = 5.99; // floating point number
printf("Value = %f\n", f);

short a = 0b1010110; // binary number
int b = 02713; // octal number
long c = 0X1DAB83; // hexadecimal number

// output in octal form
printf("a=%ho, b=%o, c=%lo\n", a, b, c);
// output => a=126, b=2713, c=7325603

// Output in decimal form
printf("a=%hd, b=%d, c=%ld\n", a, b, c);
// output => a=86, b=1483, c=1944451

// output in hexadecimal form (letter lowercase)
printf("a=%hx, b=%x, c=%lx\n", a, b, c);
// output => a=56, b=5cb, c=1dab83

// Output in hexadecimal (capital letters)
printf("a=%hX, b=%X, c=%lX\n", a, b, c);
// output => a=56, b=5CB, c=1DAB83
```

## Control the number of spaces

```c
int a1 = 20, a2 = 345, a3 = 700;
int b1 = 56720, b2 = 9999, b3 = 20098;
int c1 = 233, c2 = 205, c3 = 1;
int d1 = 34, d2 = 0, d3 = 23;

printf("%-9d %-9d %-9d\n", a1, a2, a3);
printf("%-9d %-9d %-9d\n", b1, b2, b3);
printf("%-9d %-9d %-9d\n", c1, c2, c3);
printf("%-9d %-9d %-9d\n", d1, d2, d3);
```

output result

```bash
20        345       700
56720     9999      20098
233       205       1
34        0         23
```

In `%-9d`, `d` means to output in `10` base, `9` means to occupy at least `9` characters width, and the width is not
enough to fill with spaces, `-` means left alignment

## Strings

```c
char greetings[] = "Hello World!";
printf("%s", greetings);
```

Access string

```c
char greetings[] = "Hello World!";
printf("%c", greetings[0]);
```

Modify string

```c
char greetings[] = "Hello World!";
greetings[0] = 'J';

printf("%s", greetings);
// prints "Jello World!"
```

Another way to create a string

```c
char greetings[] = {'H','e','l','l','\0'};

printf("%s", greetings);
// print "Hell!"
```

Creating String using character pointer (String Literals)

```c
char *greetings = "Hello";
printf("%s", greetings);
// print "Hello!"
```

**NOTE**: String literals might be stored in read-only section of memory. Modifying a string literal invokes undefined
behavior. You can't modify it!

`C` **does not** have a String type, use `char` type and create an `array` of characters

## Condition

```c
int time = 20;
if (time < 18) {
  printf("Goodbye!\n");
} else {
  printf("Good evening!\n");
}
// Output -> "Good evening!"
int time = 22;
if (time < 10) {
  printf("Good morning!\n");
} else if (time < 20) {
  printf("Goodbye!\n");
} else {
  printf("Good evening!\n");
}
// Output -> "Good evening!"
```

## Ternary operator

```c
int age = 20;
(age > 19) ? printf("Adult\n") : printf("Teenager\n");
```

## Switch

```c
int day = 4;

switch (day) {
  case 3: printf("Wednesday\n"); break;
  case 4: printf("Thursday\n"); break;
  default:
    printf("Weekend!\n");
}
// output -> "Thursday" (day 4)
```

## While Loop

```c
int i = 0;

while (i < 5) {
  printf("%d\n", i);
  i++;
}
```

**NOTE**: Don't forget to increment the variable used in the condition, otherwise the loop will never end and become an
"infinite loop"!

## Do/While Loop

```c
int i = 0;

do {
  printf("%d\n", i);
  i++;
} while (i < 5);
```

## For Loop

```c
for (int i = 0; i < 5; i++) {
  printf("%d\n", i);
}
```

## Break out of the loop Break/Continue

```c
for (int i = 0; i < 10; i++) {
  if (i == 4) {
    break;
  }
  printf("%d\n", i);
}
```

Break out of the loop when `i` is equal to `4`

```c
for (int i = 0; i < 10; i++) {
  if (i == 4) {
    continue;
  }
  printf("%d\n", i);
}
```

Example to skip the value of `4`

## While Break Example

```c
int i = 0;

while (i < 10) {
  if (i == 4) {
    break;
  }
  printf("%d\n", i);

  i++;
}
```

## While continue example

```c
int i = 0;

while (i < 10) {
  i++;

  if (i == 4) {
    continue;
  }
  printf("%d\n", i);
}
```

## Arrays

```c
int myNumbers[] = {25, 50, 75, 100};

printf("%d", myNumbers[0]);
// output 25
```

Change array elements

```c
int myNumbers[] = {25, 50, 75, 100};
myNumbers[0] = 33;

printf("%d", myNumbers[0]);
```

Loop through the array

```c
int myNumbers[] = {25, 50, 75, 100};
int i;

for (i = 0; i < 4; i++) {
  printf("%d\n", myNumbers[i]);
}
```

Set array size

```c
// Declare an array of four integers:
int myNumbers[4];

// add element
myNumbers[0] = 25;
myNumbers[1] = 50;
myNumbers[2] = 75;
myNumbers[3] = 100;
```

## Enumeration Enum

```c
enum week { Mon = 1, Tues, Wed, Thurs, Fri, Sat, Sun };
```

Define enum variable

```c
enum week a, b, c;
enum week { Mon = 1, Tues, Wed, Thurs, Fri, Sat, Sun } a, b, c;
```

With an enumeration variable, you can assign the value in the list to it

```c
enum week { Mon = 1, Tues, Wed, Thurs, Fri, Sat, Sun };
enum week a = Mon, b = Wed, c = Sat;
// or
enum week{ Mon = 1, Tues, Wed, Thurs, Fri, Sat, Sun } a = Mon, b = Wed, c = Sat;
```

## Enumerate sample applications

```c
enum week {Mon = 1, Tues, Wed, Thurs} day;

scanf("%d", &day);

switch(day) {
  case Mon: puts("Monday"); break;
  case Tues: puts("Tuesday"); break;
  case Wed: puts("Wednesday"); break;
  case Thurs: puts("Thursday"); break;
  default: puts("Error!");
}
```

## User input

```c
// Create an integer variable to store the number we got from the user
int myNum;

// Ask the user to enter a number
printf("Enter a number: ");

// Get and save the number entered by the user
scanf("%d", &myNum);

// Output the number entered by the user
printf("The number you entered: %d\n", myNum);
```

## User input string

```c
// create a string
char firstName[30];
// Ask the user to enter some text
printf("Enter your name: ");
// get and save the text
scanf("%s", &firstName);
// output text
printf("Hello %s.\n", firstName);
```

## memory address

When a variable is created, it is assigned a memory address

```c
int myAge = 43;

printf("%p", &myAge);
// Output: 0x7ffe5367e044
```

To access it, use the reference operator (`&`)

## create pointer

```c
int myAge = 43; // an int variable
printf("%d\n", myAge); // output the value of myAge(43)

// Output the memory address of myAge (0x7ffe5367e044)
printf("%p\n", &myAge);
```

## pointer variable

```c
int myAge = 43; // an int variable
int*ptr = &myAge; // pointer variable named ptr, used to store the address of myAge

printf("%d\n", myAge); // print the value of myAge (43)

printf("%p\n", &myAge); // output the memory address of myAge (0x7ffe5367e044)
printf("%p\n", ptr); // use the pointer (0x7ffe5367e044) to output the memory address of myAge
```

## Dereference

```c
int myAge = 43; // variable declaration
int*ptr = &myAge; // pointer declaration

// Reference: output myAge with a pointer
// memory address (0x7ffe5367e044)
printf("%p\n", ptr);
// dereference: output the value of myAge with a pointer (43)
printf("%d\n", *ptr);
```
