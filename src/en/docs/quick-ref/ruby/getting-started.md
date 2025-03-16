# Getting Started

## Install

```bash
# Debian, Ubuntu
$ sudo apt-get install ruby-full
# Windows
$ winget install RubyInstallerTeam.Ruby
$ brew install ruby # macOS
$ docker run -it --rm ruby:latest # Docker
```

## What is Gemfile and Gemfile.lock

- [Gemfile](https://bundler.io/v2.3/man/gemfile.5.html) Is the Bundler (also gem) configuration file that contains the
  project's gem list (dependencies)

```ruby
# Specify gem in the Gemfile in the project root directory
ruby '3.1.2'

source 'https://rubygems.org'
gem 'nokogiri'
gem 'rack', '~>3.0.10'
gem 'rspec', :require => 'spec'
```

Install all gems in Gemfile

```bash
bundle install
```

Solve the problem of Gemfile.lock inconsistency between mac for development and linux for production

```bash
bundle lock --add-platform x86_64-linux
```

## Install a specific version of a specific ruby gem

```bash
gem install bundler -v 2.4.20
gem install minitest -v 5.22.3
```

## Update gems using Bundler

```bash
# Updating a single gem using Bundler
$ bundle update nokogiri
# Use Bundler to update each gem in the Gemfile
$ bundle update
```

## Comment

```ruby
# This is a single line comments.
=begin
Multi-line
Comment
=end
puts "Hello world!"  # Inline comments for code
```

## reserved words

| Reserved words | Description                                                                                                |
| :------------- | :--------------------------------------------------------------------------------------------------------- |
| `__ENCODING__` | The script encoding of the current file                                                                    |
| `__LINE__`     | The line number of this keyword in the current file                                                        |
| `__FILE__`     | The path of the current file                                                                               |
| `BEGIN`        | Code enclosed in { } is run before the program is run                                                      |
| `END`          | Code enclosed in { } is run at the end of the program                                                      |
| `alias`        | Create an alias for an existing method, operator, or global variable                                       |
| `and`          | Logical AND operator                                                                                       |
| `begin`        | Begin a block of code                                                                                      |
| `break`        | Terminate a loop                                                                                           |
| `case`         | Compare an expression with matching `when` clauses, terminated with <br/> `end`                            |
| `class`        | Define a class                                                                                             |
| `def`          | define a function/method                                                                                   |
| `defined?`     | Check if a variable or function exist                                                                      |
| `do`           | Start a block of code, terminated with the <br/> `end` keyword                                             |
| `else`         | Execute the following code if previous conditions are not met                                              |
| `elsif`        | Alternative condition for if expressions                                                                   |
| `end`          | End blocks of code starting with keywords like `begin`, `class`,`def`,`do`,`if`, etc.                      |
| `ensure`       | Always execute at the end of a block                                                                       |
| `false`        | Logical boolean value false                                                                                |
| `for`          | Start a `for` loop                                                                                         |
| `if`           | Execute the code block `if` the condition is `true`                                                        |
| `in`           | Used with `for` loop                                                                                       |
| `module`       | Define a module                                                                                            |
| `next`         | jump to the point before the evaluation of the loop condition                                              |
| `nil`          | Stand for null, invalid, or always false                                                                   |
| `not`          | Logical NOT operator                                                                                       |
| `or`           | Logical OR operator                                                                                        |
| `redo`         | Jump back to the loop condition evaluation                                                                 |
| `rescue`       | Evaluate expressions after an exception is raised                                                          |
| `retry`        | Repeat method calls when called outside `rescue`, jump to the top of the block when called inside `rescue` |
| `return`       | Return a value from a method or block                                                                      |
| `self`         | Refer to the current object                                                                                |
| `super`        | Call the same-named method in the superclass                                                               |
| `then`         | Used as a separator with`if`,`unless`,`when`,`case`,`rescue`                                               |
| `true`         | Logical boolean value true                                                                                 |
| `undef`        | Undefine methods/functions within the current class                                                        |
| `until`        | Execute the code block until the condition is false                                                        |
| `when`         | Begin a clause under a `case` statement                                                                    |
| `while`        | Execute the code block while the condition is true                                                         |
| `yield`        | Execute the code block passed to a method                                                                  |

## Operator

### Logical Operators

- `and`
- `or`
- `not`
- `&&`
- `||`
- `!`

### Bit operators

- `&`
- `|`
- `^`
- `~`
- `<<`
- `>>`

### Arithmetic operators

- `+`
- `-`
- `*`
- `/`
- `%`
- `**`

### Comparison operator

- `==`
- `!=`
- `>`
- `<`
- `>=`
- `<=`
- `<=>`
- `===`
- `eql?`
- `equal?`

### Operator examples

```bash
# Addition
1 + 1   #=> 2
# Subtraction
2 - 1   #=> 1
# Multiplication
2 * 2   #=> 4
# Division
10 / 5  #=> 2
17 / 5    #=> 3, not 3.4
17 / 5.0  #=> 3.4
# Exponentiation
2 ** 2  #=> 4
3 ** 4  #=> 81
# Modulus (remainder of division)
8 % 2   #=> 0  (8 / 2 = 4; no remainder)
10 % 4  #=> 2  (10 / 4 = 2 remainder 2)
a = 10
b = 20
a == b #=> false
a != b #=> true
a > b #=> false
a < b #=> true
a >= b #=> false
a <= b #=> true

# Comparison operators
a <=> b #=> -1
c = 20
c <=> b #=> 0
c <=> a  #=> 1
# Equality used in when clauses for case statements
(1...10) === 5 #=> true
# True if the receiver and the argument have the same type and equal values
1.eql?(1.0) #=> false
c = a + b  #=> 30
c += a #=> 40
c -= a #=> 30
c *= a #=> 300
c /= a #=> 30
c %= a #=> 3
c **= a #=> 59049

# Ruby parallel assignment
a = 10
b = 20
c = 30
a, b, c = 10, 20, 30
# Ruby bitwise operators
a = 60
b = 13
# & Binary AND operator copies a bit to the result if it exists in both operands.
a & b #=> 12
# | Binary OR operator copies a bit if it exists in either operand.
a | b #=> 61
# ^ Binary XOR operator copies a bit if it is set in one operand but not both.
a ^ b #=> 49
# ~ Binary Ones Complement is unary and has the effect of 'flipping' bits.
~a
# << Binary Left Shift Operator. The left operand's value is moved
# left by the number of bits specified by the right operand.
a << 2
# >> Binary Right Shift Operator. The left operand's value is moved
# right by the number of bits specified by the right operand.
a >> 2

# Ruby logical operators
a and b #=> true.
a or b #=> true.
a && b #=> true.
(a || b) #=> true.
!(a && b) #=> false.
not(a && b) #=> false.
# Ruby ternary operator
# ? :
# If condition is true ? Then value X : Otherwise value Y
a == 10 ? puts 'Right' : puts 'Wrong'
# Ruby range operators
# .. Creates a range from the start point to the end point (inclusive)
1..10 #=> Creates a range from 1 to 10 (inclusive of 1 and 10)
# ... Creates an exclusive range from the start point to the end point
1...10 #=> Creates an exclusive range from 1 to 10
```

## Operator precedence table

From highest to lowest, this is the precedence table for ruby. High precedence operations happen before low precedence
operations.

- !, ~, unary +
- \*\*
- unary -
- \*, /, %
- +, -
- <<, >>
- &
- |, ^
- > , >=, <, <=
- <=>, ==, ===, !=, =~, !~
- &&
- ||
- .., ...
- ?, :
- modifier-rescue
- =, +=, -=, etc.
- defined?
- not
- or, and
- modifier-if, modifier-unless, modifier-while, modifier-until
- { } blocks

## Variables and scope

| -              | -                 | -                             | -                                                                                                |
| -------------- | ----------------- | ----------------------------- | :----------------------------------------------------------------------------------------------- |
| Name           | Scope             | Example                       | Explanation                                                                                      |
| `[a-z]` or `_` | Local             | `count = 10` or `_count = 10` | Local variables must be initialized                                                              |
| `@`            | Instance variable | `@id = []`                    | Instance variables have a "nil" value before initialization                                      |
| `@@`           | Class variable    | `@@name = []`                 | Class variables must be initialized                                                              |
| `$`            | Global variable   | `$version = "0.8.9"`          | Global variables have a "nil" value before initialization                                        |
| `[A-Z]`        | Constant          | `PI = 3.14`                   | Constant variables must be initialized, you can change constants, but you will receive a warning |

There are five different types of variables. The first character determines the range To read in deap about variables
check [User Guide](https://ruby-doc.org/docs/ruby-doc-bundle/UsersGuide/rg/) cap 19,20,21,22,23
[Pre-Defined Variables and Constants](https://ruby-doc.org/docs/ruby-doc-bundle/Manual/man-1.4/variable.html)

## Check the scope of a variable

```ruby
defined? count
"local-variable"
defined? @id
"instance-variable"
defined? @@name
"class variable"
defined? $version
"global-variable"
defined? PI
"constant"
```

## Data Types

| -         | -                            | -                                                  | -                                                                                                               |
| :-------- | :--------------------------- | :------------------------------------------------- | :-------------------------------------------------------------------------------------------------------------- |
| Type      | Example                      | Class                                              | Documentation                                                                                                   |
| `Integer` | a = 17                       | a.class > Integer <br>a.class.superclass > Numeric | [#](<(https://ruby-doc.org/3.3.1/Integer.html)>)                                                                |
| `Float`   | a = 87.23                    | a.class > Float <br>a.class.superclass > Numeric   | [#](https://ruby-doc.org/3.3.1/Float.html)                                                                      |
| `String`  | a = "Hello universe"         | a.class > String                                   | [#](https://ruby-doc.org/3.3.1/String.html)                                                                     |
| `Array`   | a = [12, 34]                 | a.class > Array                                    | [#](https://ruby-doc.org/3.3.1/Array.html)                                                                      |
| `Hash`    | a = {type: "tea", count: 10} | a.class > Hash                                     | [#](https://ruby-doc.org/3.3.1/Hash.html)                                                                       |
| `Boolean` | a = false<br>a = true        | a.class > FalseClass <br>a.class > TrueClass       | [TrueClass](https://ruby-doc.org/3.3.1/TrueClass.html) [FalseClass](https://ruby-doc.org/3.3.1/FalseClass.html) |
| `Symbol`  | a = :status                  | a.class > Symbol                                   | [#](https://ruby-doc.org/3.3.1/Symbol.html)                                                                     |
| `Range`   | a = 1..3                     | a.class > Range                                    | [#](https://ruby-doc.org/3.3.1/Range.html)                                                                      |
| `Nil`     | a = nil                      | a.class > NilClass                                 | [#](https://ruby-doc.org/3.3.1/NilClass.html)                                                                   |

[further reading](https://www.digitalocean.com/community/tutorials/understanding-data-types-in-ruby)

## Check data type

```ruby
# Both are synonyms
a = 37
a.kind_of? Integer
# true
a.is_a? Integer
# true
```

## Symbol

```ruby
week_days = {sunday: 11, monday: 222}
```

## Integer useful methods

```ruby
2.even?
# true
3.even?
# false
```

## Range

`..` Used to create inclusive ranges

```ruby
range = 1..10
range.to_a
# output => [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
```

`...` Used to create exclusive ranges

```ruby
range = 1...10
range.to_a
# output => [1, 2, 3, 4, 5, 6, 7, 8, 9]
```

some useful methods

| Method name | Output                                |
| :---------- | :------------------------------------ |
| `cover?`    | `(1..5).cover?(5)` => `true`          |
| `end`       | `('a'..'z').end` => `"z"`             |
| `first`     | `(1..5).first` => `1`                 |
| `first(3)`  | `('A'..'Z').first(2)` => `["A", "B"]` |
| `eql?`      | `((0..2).eql?(0..5)` => `false`       |

## Using `step` in Range

```ruby
(1..20).step(2) { |number| puts "#{number}"}
# output
# 1
# 3
# 5
# 7
# 9
# 11
# 13
# 15
# 17
# 19
```
