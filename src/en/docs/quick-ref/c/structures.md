# Structures

## Create structure

```c
struct MyStructure { // structure declaration
  int myNum; // member (int variable)
  char myLetter; // member (char variable)
}; // end the structure with a semicolon
```

Create a struct variable called `s1`

```c
struct myStructure {
  int myNum;
  char myLetter;
};

int main() {
  struct myStructure s1;

  return 0;
}
```

## Strings in the structure

```c
struct myStructure {
  int myNum;
  char myLetter;
  char myString[30]; // String
};

int main() {
  struct myStructure s1;
  strcpy(s1. myString, "Some text");
  // print value
  printf("My string: %s\n", s1.myString);

  return 0;
}
```

Assigning values to strings using the `strcpy` function

## Accessing structure members

```c
// create a structure called myStructure
struct myStructure {
  int myNum;
  char myLetter;
};

int main() {
  // Create a structure variable called myStructure called s1
  struct myStructure s1;
  // Assign values ​​to the members of s1
  s1.myNum = 13;
  s1.myLetter = 'B';

  // Create a structure variable of myStructure called s2
  // and assign it a value
  struct myStructure s2 = {13, 'B'};
  // print value
  printf("My number: %d\n", s1.myNum);
  printf("My letter: %c\n", s1.myLetter);

  return 0;
}
```

Create different structure variables

```c
struct myStructure s1;
struct myStructure s2;
// Assign values ​​to different structure variables
s1.myNum = 13;
s1.myLetter = 'B';

s2.myNum = 20;
s2.myLetter = 'C';
```

## Copy structure

```c
struct myStructure s1 = {
  13, 'B', "Some text"
};

struct myStructure s2;
s2 = s1;
```

In the example, the value of `s1` is copied to `s2`

## Modify value

```c
// Create a struct variable and assign it a value
struct myStructure s1 = {
  13, 'B'
};
// modify the value
s1.myNum = 30;
s1.myLetter = 'C';
// print value
printf("%d %c",
    s1.myNum,
    s1.myLetter);
```
