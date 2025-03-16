# Blocks

## Block example

```ruby
# return value
def give_me_data
    data = yield
    puts "data = #{data}"
end
give_me_data { "Big data" }
# output => data = Big data
```

The code between `do` and `end` (for multiple lines) or curly braces `{` and `}` (for a single line) is called a block,
and they can define multiple parameters between two pipes `( |arg1, arg2|)`

## Single line block

```ruby
salary = [399, 234, 566, 533, 233]
salary.each { |s| puts s }
# puts s = block body
# |s| = block arguments
```

## Multi-line block

```ruby
salary.each do |s|
    a = 10
    res = a * s
    puts res
end
# Block
# a = 10
# res = a * s
# puts res
# block parameters
# |s|
```

Blocks can be passed as method parameters or associated with method calls. block returns the last evaluated statement

## Implicitly passing a block

```ruby
def give_me_data
    puts "I am inside give_me_data method"
    yield
    puts "I am back in give_me_data method"
end

give_me_data { puts "Big data" }

# output
# I am inside give_me_data method
# Big data
# I am back in give_me_data method
```

## Called multiple times

```ruby
def give_me_data
    yield
    yield
    yield
end

give_me_data { puts "Big data" }

# output
# Big data
# Big data
# Big data
```

## Called with block parameters

```ruby
def give_me_data
    yield 10
    yield 100
    yield 30
end

give_me_data { |data| puts "Big data #{data} TB" }

# output
# Big data 10 TB
# Big data 100 TB
# Big data 30 TB
```

## Called with multiple block parameters

```ruby
def give_me_data
    yield "Big data", 10, "TB"
    yield "Big data", 100, "GB"
    yield "Big data", 30, "MB"
end

give_me_data { |text, data, unit| puts "#{text} #{data} #{unit}" }

# output
# Big data 10 TB
# Big data 100 GB
# Big data 30 MB
```

## Block will attempt to return from the current context

```ruby
give_me_data
    puts "I'm inside the give_me_data method"
end

def test
  puts "I'm inside the test method"
  give_me_data { return 10 } # Code returns from here
  puts "I am back in test method"
end

return_value = test

# output
# I'm inside the test method
# I'm inside the give_me_data method
# 10
```

## Pass the block explicitly by using the & parameter

```ruby
def give_me_data(&block)
    block.call
    block.call
end

give_me_data { puts "Big data" }

# output
# Big data
# Big data
```

## Check if block is given

```ruby
def give_me_data
    yield
end

give_me_data

# output
# LocalJumpError: no block given (yield)
```

## Ways to handle exceptions and make blocks optional

```ruby
def give_me_data
    return "no block" unless block_given?
    yield
end

give_me_data { puts "Big data" }
give_me_data

# output
# Big data
```
