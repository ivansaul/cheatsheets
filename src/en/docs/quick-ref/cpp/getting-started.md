# Getting Started

## hello.cpp

```cpp
#include <iostream>

int main() {
    std::cout << "Hello CheatSheets\n";
    return 0;
}
```

Compiling and running

```shell script
$ g++ hello.cpp -o hello
$ ./hello
Hello CheatSheets
```

## Variables

```cpp
int number = 5;       // Integer
float f = 0.95;       // Floating number
double PI = 3.14159;  // Floating number
char yes = 'Y';       // Character
std::string s = "ME"; // String (text)
bool isRight = true;  // Boolean

// Constants
const float RATE = 0.8;
```

---

```cpp
int age {25};         // Since C++11
std::cout << age;     // Print 25
```

## Primitive Data Types

| Data Type | Size           | Range               |
| --------- | -------------- | ------------------- |
| `int`     | 4 bytes        | -2^31^ ^to^ 2^31^-1 |
| `float`   | 4 bytes        | _N/A_               |
| `double`  | 8 bytes        | _N/A_               |
| `char`    | 1 byte         | -128 ^to^ 127       |
| `bool`    | 1 byte         | true / false        |
| `void`    | _N/A_          | _N/A_               |
| `wchar_t` | 2 ^or^ 4 bytes | 1 wide character    |

## User Input

```cpp
int num;

std::cout << "Type a number: ";
std::cin >> num;

std::cout << "You entered " << num;
```

## Swap

```cpp
int a = 5, b = 10;
std::swap(a, b);

// Outputs: a=10, b=5
std::cout << "a=" << a << ", b=" << b;
```

## Comments

```cpp
// A single one line comment in C++

/* This is a multiple line comment
   in C++ */
```

## If statement

```cpp
if (a == 10) {
    // do something
}
```

## Loops

```cpp
for (int i = 0; i < 10; i++) {
    std::cout << i << "\n";
}
```

## Functions

```cpp
#include <iostream>

void hello(); // Declaring

int main() {  // main function
    hello();    // Calling
}

void hello() { // Defining
    std::cout << "Hello CheatSheets!\n";
}
```

## References

```cpp
int i = 1;
int& ri = i; // ri is a reference to i

ri = 2; // i is now changed to 2
std::cout << "i=" << i;

i = 3;   // i is now changed to 3
std::cout << "ri=" << ri;
```

`ri` and `i` refer to the same memory location.

## Namespaces

```cpp
#include <iostream>
namespace ns1 {int val(){return 5;}}
int main()
{
    std::cout << ns1::val();
}
```

---

```cpp
#include <iostream>
namespace ns1 {int val(){return 5;}}
using namespace ns1;
using namespace std;
int main()
{
    cout << val();
}
```

Namespaces allow global identifiers under a name
