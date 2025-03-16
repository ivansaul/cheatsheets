# Procs

## Proc

```ruby
p = Proc.new { puts "Hello World" }

def give_me_data(proc)
    proc.call
end

give_me_data p

# output
# Hello World
```

proc is like a block that can be stored in a variable

## any parameter

```ruby
p = Proc.new { |count| "Hello World " * count }

def give_me_data(proc)
    proc.call 5, 2
end

give_me_data p

# output
# "Hello World Hello World Hello World Hello World Hello World "
```

## proc will attempt to return from the current context

```ruby
p = Proc.new { return 10 }
p.call
# output
LocalJumpError: unexpected return
```

## Cannot return from top-level context

```ruby
def give_me_data
    puts "I'm inside the give_me_data method"
    p = Proc.new { return 10 }
    p.call # Code returns from here
    puts "I am back in give_me_data method"
end

return_value = give_me_data
puts return_value

# output
# I'm inside the give_me_data method
# 10
```
