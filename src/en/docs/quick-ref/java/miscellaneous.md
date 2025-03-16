# Miscellaneous

## Access Modifiers

| Modifier    | Class | Package | Subclass | World |
| ----------- | ----- | ------- | -------- | ----- |
| public      | Y     | Y       | Y        | Y     |
| protected   | Y     | Y       | Y        | _N_   |
| no modifier | Y     | Y       | _N_      | _N_   |
| private     | Y     | _N_     | _N_      | _N_   |

## Regular expressions

```java
String text = "I am learning Java";
// Removing All Whitespace
text.replaceAll("\\s+", "");

// Splitting a String
text.split("\\|");
text.split(Pattern.quote("|"));
```

See: [Regex in java](/regex#regex-in-java)

## Comment

```java
// I am a single line comment!

/*
And I am a
multi-line comment!
*/

/**
 * This
 * is
 * documentation
 * comment
 */
```

## Keywords

- `abstract`
- `continue`
- `for`
- `new`
- `switch`
- `assert`
- `default`
- `goto`
- `package`
- `synchronized`
- `boolean`
- `do`
- `if`
- `private`
- `this`
- `break`
- `double`
- `implements`
- `protected`
- `throw`
- `byte`
- `else`
- `import`
- `public`
- `throws`
- `case`
- `enum`
- `instanceof`
- `return`
- `transient`
- `catch`
- `extends`
- `int`
- `short`
- `try`
- `char`
- `final`
- `interface`
- `static`
- `void`
- `class`
- `finally`
- `long`
- `strictfp`
- `volatile`
- `const`
- `float`
- `native`
- `super`
- `while`

{.marker-none .cols-6}

## Math methods

| Method                | Description            |
| --------------------- | :--------------------- |
| `Math.max(a,b)`       | Maximum of a and b     |
| `Math.min(a,b)`       | Minimum of a and b     |
| `Math.abs(a)`         | Absolute value a       |
| `Math.sqrt(a)`        | Square-root of a       |
| `Math.pow(a,b)`       | Power of b             |
| `Math.round(a)`       | Closest integer        |
| `Math.sin(ang)`       | Sine of ang            |
| `Math.cos(ang)`       | Cosine of ang          |
| `Math.tan(ang)`       | Tangent of ang         |
| `Math.asin(ang)`      | Inverse sine of ang    |
| `Math.log(a)`         | Natural logarithm of a |
| `Math.toDegrees(rad)` | Angle rad in degrees   |
| `Math.toRadians(deg)` | Angle deg in radians   |

## Try/Catch/Finally

```java
try {
  // something
} catch (Exception e) {
  e.printStackTrace();
} finally {
  System.out.println("always printed");
}
```
