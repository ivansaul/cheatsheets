# Arrays

## Defining

```php
$a1 = ["hello", "world", "!"]
$a2 = array("hello", "world", "!");
$a3 = explode(",", "apple,pear,peach");
```

### Mixed int and string keys

```php
$array = array(
    "foo" => "bar",
    "bar" => "foo",
    100   => -100,
    -100  => 100,
);
var_dump($array);
```

### Short array syntax

```php
$array = [
    "foo" => "bar",
    "bar" => "foo",
];
```

## Multi array

```php
$multiArray = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
];

print_r($multiArray[0][0]) # => 1
print_r($multiArray[0][1]) # => 2
print_r($multiArray[0][2]) # => 3
```

## Multi type

```php
$array = array(
    "foo" => "bar",
    42    => 24,
    "multi" => array(
         "dim" => array(
             "a" => "foo"
         )
    )
);

# => string(3) "bar"
var_dump($array["foo"]);

# => int(24)
var_dump($array[42]);

# =>  string(3) "foo"
var_dump($array["multi"]["dim"]["a"]);
```

## manipulation

```php
$arr = array(5 => 1, 12 => 2);
$arr[] = 56;      // Append
$arr["x"] = 42;   // Add with key
sort($arr);       // Sort
unset($arr[5]);   // Remove
unset($arr);      // Remove all
```

See: [Array Functions](https://www.php.net/manual/en/ref.array.php)

## Indexing iteration

```php
$array = array('a', 'b', 'c');
$count = count($array);

for ($i = 0; $i < $count; $i++) {
    echo "i:{$i}, v:{$array[$i]}\n";
}
```

## Value iteration

```php
$colors = array('red', 'blue', 'green');

foreach ($colors as $color) {
    echo "Do you like $color?\n";
}
```

## Key iteration

```php
$arr = ["foo" => "bar", "bar" => "foo"];

foreach ( $arr as $key => $value )
{
   echo "key: " . $key . "\n";
    echo "val: {$arr[$key]}\n";
}
```

## Concatenate arrays

```php
$a = [1, 2];
$b = [3, 4];

// PHP 7.4 later
# => [1, 2, 3, 4]
$result = [...$a, ...$b];
```

## Into functions

```php
$array = [1, 2];

function foo(int $a, int $b) {
 echo $a; # => 1
   echo $b; # => 2
}
foo(...$array);
```

## Splat Operator

```php
function foo($first, ...$other) {
 var_dump($first); # => a
   var_dump($other); # => ['b', 'c']
}
foo('a', 'b', 'c' /*, ...*/ );
// or
function foo($first, string ...$other){}
```
