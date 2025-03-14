# Extensions

## Why use extensions?

```dart
// Extensions allow you to add methods to existing
// classes without modifying them.

// Instead of defining a util class.
class StringUtil {
  static bool isValidEmail(String str) {
    final emailRegExp = RegExp(r"^[a-zA-Z0-9.]+@[a-zA-Z0-9]+\.[a-zA-Z]+");
    return emailRegExp.hasMatch(str);
  }
}

print(StringUtil.isValidEmail('someString')); //Print: false

// We can define an extension which will be applied
// on a certain type.

extension StringExtensions on String {
  bool get isValidEmail {
    final emailRegExp = RegExp(r"^[a-zA-Z0-9.]+@[a-zA-Z0-9]+\.[a-zA-Z]+");
    return emailRegExp.hasMatch(this);
  }
}

print('test@example.com'.isValidEmail); //Print: true
print('SomeString'.isValidEmail); //Print: false

```

## Generic Extensions

```dart
// allows you to apply the same logic to a range of types.
extension NumGenericExtensions<T extends num> on T {
  T addTwo() => this + 2 as T;
}

print(7.addTwo()); // Print: 9
```

## Dart Extensions in Flutter

```dart
extension ContextExtension on BuildContext {
  double get screenHeight => MediaQuery.of(this).size.height;
  double get screenWidth => MediaQuery.of(this).size.width;
}

// usage
@override
Widget build(BuildContext context) => MaterialApp(
    home: Scaffold(
      body: Container(
        width: context.screenWidth * 0.5,
        height: context.screenHeight * 0.3,
        color: Colors.blue,
        child: Text('Hello World!'),
      ),
    ),
  );
```
