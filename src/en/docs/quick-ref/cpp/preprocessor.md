# Preprocessor

## Preprocessor

- [if](https://en.cppreference.com/w/cpp/preprocessor/conditional)
- [elif](https://en.cppreference.com/w/cpp/preprocessor/conditional)
- [else](https://en.cppreference.com/w/cpp/preprocessor/conditional)
- [endif](https://en.cppreference.com/w/cpp/preprocessor/conditional)
- [ifdef](https://en.cppreference.com/w/cpp/preprocessor/conditional)
- [ifndef](https://en.cppreference.com/w/cpp/preprocessor/conditional)
- [define](https://en.cppreference.com/w/cpp/preprocessor/replace)
- [undef](https://en.cppreference.com/w/cpp/preprocessor/replace)
- [include](https://en.cppreference.com/w/cpp/preprocessor/include)
- [line](https://en.cppreference.com/w/cpp/preprocessor/line)
- [error](https://en.cppreference.com/w/cpp/preprocessor/error)
- [pragma](https://en.cppreference.com/w/cpp/preprocessor/impl)
- [defined](https://en.cppreference.com/w/cpp/preprocessor/conditional)
- [\_\_has_include](https://en.cppreference.com/w/cpp/feature_test)
- [\_\_has_cpp_attribute](https://en.cppreference.com/w/cpp/feature_test)
- [export](https://en.cppreference.com/w/cpp/keyword/export)
- [import](https://en.cppreference.com/mwiki/index.php?title=cpp/keyword/import&action=edit&redlink=1)
- [module](https://en.cppreference.com/mwiki/index.php?title=cpp/keyword/module&action=edit&redlink=1)

{.marker-none .cols-2}

## Includes

```cpp
#include "iostream"
#include <iostream>
```

## Defines

```cpp
#define FOO
#define FOO "hello"

#undef FOO
```

## If

```cpp
#ifdef DEBUG
  console.log('hi');
#elif defined VERBOSE
  ...
#else
  ...
#endif
```

## Error

```cpp
#if VERSION == 2.0
  #error Unsupported
  #warning Not really supported
#endif
```

## Macro

```cpp
#define DEG(x) ((x) * 57.29)
```

## Token concat

```cpp
#define DST(name) name##_s name##_t
DST(object);   #=> object_s object_t;
```

## Stringification

```cpp
#define STR(name) #name
char * a = STR(object);   #=> char * a = "object";
```

## file and line

```cpp
#define LOG(msg) console.log(__FILE__, __LINE__, msg)
#=> console.log("file.txt", 3, "hey")
```
