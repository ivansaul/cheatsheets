# Operators

## Arithmetic Operators

```c
int myNum = 100 + 50;
int sum1 = 100 + 50; // 150 (100 + 50)
int sum2 = sum1 + 250; // 400 (150 + 250)
int sum3 = sum2 + sum2; // 800 (400 + 400)
```

---

| Operator | Name      | Example |
| -------- | --------- | ------- |
| `+`      | Add       | `x + y` |
| `-`      | Subtract  | `x - y` |
| `*`      | Multiply  | `x * y` |
| `/`      | Divide    | `x / y` |
| `%`      | Modulo    | `x % y` |
| `++`     | Increment | `++x`   |
| `--`     | Decrement | `--x`   |

## Assignment operator

| Example              | As                        |
| -------------------- | ------------------------- |
| x `=` 5              | x `=` 5                   |
| x `+=` 3             | x `=` x `+` 3             |
| x `-=` 3             | x `=` x `-` 3             |
| x `*=` 3             | x `=` x `*` 3             |
| x `/=` 3             | x `=` x `/` 3             |
| x `%=` 3             | x `=` x `%` 3             |
| x `&=` 3             | x `=` x `&` 3             |
| x <code>\|=</code> 3 | x `=` x <code>\|</code> 3 |
| x `^=` 3             | x `=` x `^` 3             |
| x `>>=` 3            | x `=` x `>>` 3            |
| x `<<=` 3            | x `=` x `<<` 3            |

## Comparison Operators

```c
int x = 5;
int y = 3;

printf("%d", x > y);
// returns 1 (true) because 5 is greater than 3
```

---

| Symbol | Name                     | Example  |
| ------ | ------------------------ | -------- |
| `==`   | equals                   | x `==` y |
| `!=`   | not equal to             | x `!=` y |
| `>`    | greater than             | x `>` y  |
| `<`    | less than                | x `<` y  |
| `>=`   | greater than or equal to | x `>=` y |
| `<=`   | less than or equal to    | x `<=` y |

Comparison operators are used to compare two values

## Logical Operators

| Symbol            | Name          | Description                                   | Example                       |
| ----------------- | ------------- | --------------------------------------------- | ----------------------------- |
| `&&`              | `and` logical | returns true if both statements are true      | `x < 5 && x < 10`             |
| <code>\|\|</code> | `or` logical  | returns true if one of the statements is true | <code>x < 5 \|\| x < 4</code> |
| `!`               | `not` logical | Invert result, return false if true           | `!(x < 5 && x < 10)`          |

## Operator Examples

```c
unsigned int a = 60; /*60 = 0011 1100 */
unsigned int b = 13; /*13 = 0000 1101 */
int c = 0;

c = a & b; /*12 = 0000 1100 */
printf("Line 1 -the value of c is %d\n", c);

c = a | b; /*61 = 0011 1101 */
printf("Line 2 -the value of c is %d\n", c);
c = a ^ b; /*49 = 0011 0001 */
printf("Line 3 -the value of c is %d\n", c);
c = ~a; /*-61 = 1100 0011 */
printf("Line 4 -The value of c is %d\n", c);
c = a << 2; /*240 = 1111 0000 */
printf("Line 5 -the value of c is %d\n", c);
c = a >> 2; /*15 = 0000 1111 */
printf("Line 6 -The value of c is %d\n", c);
```

## Bitwise operators

| Operator        | Description                                                     | Instance                                              |
| :-------------- | :-------------------------------------------------------------- | :---------------------------------------------------- |
| `&`             | Bitwise AND operation, "AND" operation by binary digits         | `(A & B)` will get `12` which is 0000 1100            |
| <code>\|</code> | Bitwise OR operator, "or" operation by binary digit             | <code>(A \| B)</code> will get`61` which is 0011 1101 |
| `^`             | XOR operator, perform "XOR" operation by binary digits          | `(A ^ B)` will get `49` which is 0011 0001            |
| `~`             | Inversion operator, perform "inversion" operation by binary bit | `(~A)` will get `-61` which is 1100 0011              |
| `<<`            | binary left shift operator                                      | `A << 2` will get `240` which is 1111 0000            |
| `>>`            | binary right shift operator                                     | `A >> 2` will get `15` which is 0000 1111             |
