# Getting Started

## hello.php

```php
<?php // begin with a PHP open tag.

echo "Hello World\n";
print("Hello cheatsheets.zip");

?>
```

PHP run command

```shell script
php hello.php
```

## Variables

```php
$boolean1 = true;
$boolean2 = True;

$int = 12;
$float = 3.1415926;
unset($float);  // Delete variable

$str1 = "How are you?";
$str2 = 'Fine, thanks';
```

## Strings

```php
$url = "cheatsheets.zip";
echo "I'm learning PHP at $url";

// Concatenate strings
echo "I'm learning PHP at " . $url;

$hello = "Hello, ";
$hello .= "World!";
echo $hello;   # => Hello, World!
```

## Arrays

```php
$num = [1, 3, 5, 7, 9];
$num[5] = 11;
unset($num[2]);    // Delete variable
print_r($num);     # => 1 3 7 9 11
echo count($num);  # => 5
```

## Operators

```php
$x = 1;
$y = 2;

$sum = $x + $y;
echo $sum;   # => 3
```

## Include

### vars.php

```php
<?php // begin with a PHP open tag.
$fruit = 'apple';
echo "I was imported";
return 'Anything you like.';
?>
```

### test.php

```php
<?php
include 'vars.php';
echo $fruit . "\n";   # => apple

/* Same as include,
cause an error if cannot be included*/
require 'vars.php';

// Also works
include('vars.php');
require('vars.php');

// Include through HTTP
include 'http://x.com/file.php';

// Include and the return statement
$result = include 'vars.php';
echo $result;  # => Anything you like.
?>
```

## Functions

```php
function add($num1, $num2 = 1) {
    return $num1 + $num2;
}
echo add(10);    # => 11
echo add(10, 5); # => 15
```

## Comments

```php
# This is a one line shell-style comment

// This is a one line c++ style comment

/* This is a multi line comment
   yet another line of comment */
```

## Constants

```php
const MY_CONST = "hello";

echo MY_CONST;   # => hello

# => MY_CONST is: hello
echo 'MY_CONST is: ' . MY_CONST;
```

## Classes

```php
class Student {
    public function __construct($name) {
        $this->name = $name;
    }
}
$alex = new Student("Alex");
```
