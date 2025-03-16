# Types

## Boolean

```php
$boolean1 = true;
$boolean2 = TRUE;
$boolean3 = false;
$boolean4 = FALSE;

$boolean5 = (boolean) 1;   # => true
$boolean6 = (boolean) 0;   # => false
```

Boolean are case-insensitive

## Integer

```php
$int1 = 28;    # => 28
$int2 = -32;   # => -32
$int3 = 012;   # => 10 (octal)
$int4 = 0x0F;  # => 15 (hex)
$int5 = 0b101; # => 5  (binary)

# => 2000100000 (decimal, PHP 7.4.0)
$int6 = 2_000_100_000;
```

See also: [Integers](https://www.php.net/manual/en/language.types.integer.php)

## Strings

```php
echo 'this is a simple string';
```

## Arrays

```php
$arr = array("hello", "world", "!");
```

## Float (Double)

```php
$float1 = 1.234;
$float2 = 1.2e7;
$float3 = 7E-10;

$float4 = 1_234.567;  // as of PHP 7.4.0
var_dump($float4);    // float(1234.567)

$float5 = 1 + "10.5";   # => 11.5
$float6 = 1 + "-1.3e3"; # => -1299
```

## Null

```php
$a = null;
$b = 'Hello php!';
echo $a ?? 'a is unset'; # => a is unset
echo $b ?? 'b is unset'; # => Hello php

$a = array();
$a == null    # => true
$a === null   # => false
is_null($a)   # => false
```

## Iterables

```php
function bar(): iterable {
    return [1, 2, 3];
}
function gen(): iterable {
    yield 1;
    yield 2;
    yield 3;
}
foreach (bar() as $value) {
    echo $value;   # => 123
}
```
