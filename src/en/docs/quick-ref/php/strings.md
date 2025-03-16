# Strings

## String

```php
# => '$String'
$sgl_quotes = '$String';

# => 'This is a $String.'
$dbl_quotes = "This is a $sgl_quotes.";

# => a   tab character.
$escaped   = "a \t tab character.";

# => a slash and a t: \t
$unescaped = 'a slash and a t: \t';
```

## Multi-line

```php
$str = "foo";

// Uninterpolated multi-liners
$nowdoc = <<<'END'
Multi line string
$str
END;

// Will do string interpolation
$heredoc = <<<END
Multi line
$str
END;
```

## Manipulation

```php
$s = "Hello Phper";
echo strlen($s);       # => 11

echo substr($s, 0, 3); # => Hel
echo substr($s, 1);    # => ello Phper
echo substr($s, -4, 3);# => hpe

echo strtoupper($s);   # => HELLO PHPER
echo strtolower($s);   # => hello phper

echo strpos($s, "l");      # => 2
var_dump(strpos($s, "L")); # => false
```

See: [String Functions](https://www.php.net/manual/en/ref.strings.php)
