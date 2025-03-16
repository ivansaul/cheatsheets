# Getting Started

## Hello.java

```java
public class Hello {
  // main method
  public static void main(String[] args)
  {
    // Output: Hello, world!
    System.out.println("Hello, world!");
  }
}
```

Compiling and running

```bash
$ javac Hello.java
$ java Hello
Hello, world!
```

## Variables

```java
int num = 5;
float floatNum = 5.99f;
char letter = 'D';
boolean bool = true;
String site = "cheatsheets.zip";
```

## Primitive Data Types

| Data Type | Size   | Default | Range               |
| --------- | ------ | ------- | :------------------ |
| `byte`    | 1 byte | 0       | -128 ^to^ 127       |
| `short`   | 2 byte | 0       | -2^15^ ^to^ 2^15^-1 |
| `int`     | 4 byte | 0       | -2^31^ ^to^ 2^31^-1 |
| `long`    | 8 byte | 0       | -2^63^ ^to^ 2^63^-1 |
| `float`   | 4 byte | 0.0f    | _N/A_               |
| `double`  | 8 byte | 0.0d    | _N/A_               |
| `char`    | 2 byte | \\u0000 | 0 ^to^ 65535        |
| `boolean` | _N/A_  | false   | true / false        |

## Strings

```java
String first = "John";
String last = "Doe";
String name = first + " " + last;
System.out.println(name);
```

## Loops

```java
String word = "CheatSheets";
for (char c: word.toCharArray()) {
  System.out.print(c + "-");
}
// Outputs: C-h-e-a-t-S-h-e-e-t-s-
```

## Arrays

```java
char[] chars = new char[10];
chars[0] = 'a'
chars[1] = 'b'

String[] letters = {"A", "B", "C"};
int[] mylist = {100, 200};
boolean[] answers = {true, false};
```

## Swap

```java
int a = 1;
int b = 2;
System.out.println(a + " " + b); // 1 2

int temp = a;
a = b;
b = temp;
System.out.println(a + " " + b); // 2 1
```

## Type Casting

```java
// Widening
// byte<short<int<long<float<double
int i = 10;
long l = i;               // 10

// Narrowing
double d = 10.02;
long l = (long)d;         // 10

String.valueOf(10);       // "10"
Integer.parseInt("10");   // 10
Double.parseDouble("10"); // 10.0
```

## Conditionals

```java
int j = 10;

if (j == 10) {
  System.out.println("I get printed");
} else if (j > 10) {
  System.out.println("I don't");
} else {
  System.out.println("I also don't");
}
```

## User Input

```java
Scanner in = new Scanner(System.in);
String str = in.nextLine();
System.out.println(str);

int num = in.nextInt();
System.out.println(num);
```
