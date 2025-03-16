# Functions

## Returning values

```php
function square($x)
{
    return $x * $x;
}

echo square(4);  # => 16
```

## Return types

```php
// Basic return type declaration
function sum($a, $b): float {/*...*/}
function get_item(): string {/*...*/}

class C {}
// Returning an object
function getC(): C { return new C; }
```

## Nullable return types

```php
// Available in PHP 7.1
function nullOrString(int $v) : ?string
{
    return $v % 2 ? "odd" : null;
}
echo nullOrString(3);       # => odd
var_dump(nullOrString(4));  # => NULL
```

See: [Nullable types](https://www.php.net/manual/en/migration71.new-features.php)

## Void functions

```php
// Available in PHP 7.1
function voidFunction(): void
{
 echo 'Hello';
 return;
}

voidFunction();  # => Hello
```

## Variable functions

```php
function bar($arg = '')
{
    echo "In bar(); arg: '$arg'.\n";
}

$func = 'bar';
$func('test'); # => In bar(); arg: test
```

## Anonymous functions

```php
$greet = function($name)
{
    printf("Hello %s\r\n", $name);
};

$greet('World'); # => Hello World
$greet('PHP');   # => Hello PHP
```

## Recursive functions

```php
function recursion($x)
{
    if ($x < 5) {
        echo "$x";
        recursion($x + 1);
    }
}
recursion(1);  # => 1234
```

## Default parameters

```php
function coffee($type = "cappuccino")
{
    return "Making a cup of $type.\n";
}
# => Making a cup of cappuccino.
echo coffee();
# => Making a cup of .
echo coffee(null);
# => Making a cup of espresso.
echo coffee("espresso");
```

## Arrow Functions

```php
$y = 1;

$fn1 = fn($x) => $x + $y;

// equivalent to using $y by value:
$fn2 = function ($x) use ($y) {
    return $x + $y;
};
echo $fn1(5);   # => 6
echo $fn2(5);   # => 6
```
