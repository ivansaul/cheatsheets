# Loops

## While

```cpp
int i = 0;
while (i < 6) {
    std::cout << i++;
}

// Outputs: 012345
```

## Do-while

```cpp
int i = 1;
do {
    std::cout << i++;
} while (i <= 5);

// Outputs: 12345
```

## Continue statements

```cpp
for (int i = 0; i < 10; i++) {
    if (i % 2 == 0) {
        continue;
    }
    std::cout << i;
} // Outputs: 13579
```

## Infinite loop

```cpp
while (true) { // true or 1
    std::cout << "infinite loop";
}
```

---

```cpp
for (;;) {
    std::cout << "infinite loop";
}
```

---

```cpp
for(int i = 1; i > 0; i++) {
    std::cout << "infinite loop";
}
```

## for_each (Since C++11)

```cpp
#include <iostream>
#include <array>

int main()
{
    auto print = [](int num) { std::cout << num << std::endl; };

    std::array<int, 4> arr = {1, 2, 3, 4};
    std::for_each(arr.begin(), arr.end(), print);
    return 0;
}
```

## Range-based (Since C++11)

```cpp
for (int n : {1, 2, 3, 4, 5}) {
    std::cout << n << " ";
}
// Outputs: 1 2 3 4 5
```

---

```cpp
std::string hello = "CheatSheets.zip";
for (char c: hello)
{
    std::cout << c << " ";
}
// Outputs: Q u i c k R e f . M E
```

## Break statements

```cpp
int password, times = 0;
while (password != 1234) {
    if (times++ >= 3) {
        std::cout << "Locked!\n";
        break;
    }
    std::cout << "Password: ";
    std::cin >> password; // input
}
```

## Several variations

```cpp
for (int i = 0, j = 2; i < 3; i++, j--){
    std::cout << "i=" << i << ",";
    std::cout << "j=" << j << ";";
}
// Outputs: i=0,j=2;i=1,j=1;i=2,j=0;
```
