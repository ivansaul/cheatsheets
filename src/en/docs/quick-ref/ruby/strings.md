# Strings

## String interpolation

```ruby
name = "World"
puts "Hello #{name}"
puts "The total is #{1+1}"
# "the total is 2"
```

String interpolation allows you to combine strings together

## Extract substring

```ruby
string = "abc123"
string[0,3]
# "abc"
string[3,3]
# "123"
string[0..-2]
# "abc12"
#remove or replace the substring
string[0..2] = ""
puts string
# "123"
```

A substring is a small part of a string, which is useful if you only want that specific part, like the beginning,
middle, or end

## Convert a string to lowercase or uppercase

```ruby
"HELLO World".downcase  # "hello world"
"hello worlD".upcase    # "HELLO WORLD"
"hEllo wOrlD".capitalize # "Hello world"
"hEllo WOrlD".swapcase  # "HeLLO woRLd"
```

## useful methods

| Function Name                  | Output                                                                                                | Note                                                                                                                                                                                |
| :----------------------------- | :---------------------------------------------------------------------------------------------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| length or size                 | `"HELLO World".length` => `11` <br> `"HELLO World".size` => `11`                                      | Returns the length of the string                                                                                                                                                    |
| reverse                        | `"hello worlD".reverse` => `"Dlrow olleh"`                                                            | Returns the reversed string                                                                                                                                                         |
| include? other_str             | `"hEllo wOrlD".include? "w"` => `true`                                                                | Returns true if the string or character exists, otherwise returns false                                                                                                             |
| gsub(pattern, replacement)     | `"hEllo wOrlD".gsub(" ", "_")` => `"hEllo_wOrlD"`                                                     | gsub or global substitute replaces one or more strings with the provided string                                                                                                     |
| gsub(pattern, hash)            | `"organization".gsub("z", 'z' => 's')` => `"organisation"`                                            | gsub or global substitute replaces one or more strings with the provided hash                                                                                                       |
| gsub(pattern) {\|match\|block} | `"Price of the phone is 1000 AUD".gsub(/\d+/) {\| s\| '$'+s }`<br>`"Price of the phone is $1000 AUD"` | gsub or global substitute replaces one or more strings with the provided block                                                                                                      |
| strip                          | `" hEllo WOrlD ".strip` <br> `"hEllo WOrlD"`                                                          | It will remove (trim) any leading and trailing characters: null (“\x00”), horizontal tab (“\t”), newline (\n), vertical tab (“\v”), form feed (f), carriage return(\r), space (" ") |
| prepend                        | `a = "world" <br> a.prepend("hello ")` <br> `"hello world"`                                           | Adds the string before another string                                                                                                                                               |
| insert                         | `a = "hello" <br> a.insert(a.length, " world")` <br> `"hello world"`                                  | Inserts the string at a specific position                                                                                                                                           |
| start_with?                    | `string = "ruby programming"` <br> `string.start_with? "ruby"` <br> `true`                            | Checks if the string starts with a specific prefix                                                                                                                                  |
| end_with?                      | `string = "ruby programming"` <br> `string.end_with? "ruby"` <br> `false`                             | Checks if the string ends with a specific prefix                                                                                                                                    |
| delete_suffix                  | `string = "sausage is expensive"` <br> `string.delete_suffix(" is expensive")` <br> `"sausage"`       | Deletes the suffix from the string                                                                                                                                                  |
| delete_prefix                  | `string = "sausage is expensive"` <br> `string.delete_prefix("sausage")` <br> `" is expensive"`       | Deletes the prefix from the string                                                                                                                                                  |
| split                          | `string = "a b c d" <br> string.split` <br> `["a", "b", "c", "d"]`                                    | Converts the string into an array of characters                                                                                                                                     |
| join                           | `arr = ['a', 'b', 'c'] <br> arr.join` => `"abc"`                                                      | Converts an array into a string                                                                                                                                                     |
| to_i                           | `a = "49" <br> a.to_i` => `49`                                                                        | Converts the string into an integer                                                                                                                                                 |
| chop                           | `"abcd?".chop("?")` => `"abcd"`                                                                       | Deletes the last character from the string                                                                                                                                          |
| count                          | `str = "aaab" <br> str.count("a")` <br> `3`                                                           | Counts the characters in the string                                                                                                                                                 |
| to_f                           | `a = "49"` <br> `a.to_f` <br> `49.0`                                                                  | Converts the string into a floating point number                                                                                                                                    |
| to_sym                         | `a = "key"` <br> `a.to_sym` <br> `:key`                                                               | Converts the string into a symbol                                                                                                                                                   |
| match                          | `"abcd?".match(/ab/)` => `#<MatchData "ab">`                                                          | Converts the pattern into a regular expression and calls its match method on the string                                                                                             |
| empty?                         | `"hello".empty?` => `false`                                                                           | Returns true if the length of the string is zero                                                                                                                                    |
| squeeze                        | `"Booook".squeeze` => `"Bok"`                                                                         | Returns a copy of the string where runs of the same character are replaced by a single character                                                                                    |
| \*                             | `puts "Ruby " * 4` => `Ruby Ruby Ruby Ruby`                                                           | Returns the concatenation of multiple copies of self                                                                                                                                |
| +                              | `"sammy " + "shark"` => `"sammyshark"`                                                                | Returns the concatenation of self and the given other string                                                                                                                        |
| eql?                           | `s = 'foo'` => `true` <br> `s.eql?('foo')` => `true`                                                  | Returns true if the objects have the same length and content; false otherwise                                                                                                       |
