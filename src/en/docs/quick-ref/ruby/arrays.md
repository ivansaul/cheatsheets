# Arrays

## Initialize an empty array

```ruby
array = Array.new   #=> []
# or
array = []
```

## Array containing objects of different types

```ruby
array = [1, "two", 3.0]
#=> [1, "two", 3.0]
```

## Fill array with initial size and default objects

```ruby
numbers = Array.new(3)
#=> [nil, nil, nil]
numbers = Array.new(3, 7)
#=> [7, 7, 7]
numbers = Array.new(3, true)
#=> [true, true, true]
numbers = []
numbers.fill(7, 0..2)   #=> [7, 7, 7]
```

## array of different hashes

```ruby
array_with_hashes = Array.new(2) { {} } #=> [{}, {}]
array_with_hashes[0][:name] = "Bob"
array_with_hashes[0][:id] = 10          #=> [{:name=>"Bob", :id=>10}, {}]
```

## Two-dimensional array

```ruby
temperature_data = [
              ["A908", 38],
              ["A909", 37],
              ["A910", 38],
          ]
temperature_data[0]    #=> ["A908", 38]
temperature_data[0][0] #=> "A908"
temperature_data[0][1] #=> 38
```

## array index

```ruby
str_array = [
  "This", "is", "a", "small", "array"
]
str_array[0]            #=> "This"
str_array[1]            #=> "is"
str_array[4]            #=> "array"
```

## negative index

```ruby
str_array = [
  "This", "is", "a", "small", "array"
]
# Index -1 represents the last element
str_array[-1]        #=> "array"
# Index -2 represents the second to last element
str_array[-2]        #=> "small"
str_array[-6]        #=> nil
```

## array method at

```ruby
str_array = [
  "This", "is", "a", "small", "array"
]

puts str_array.at(0)      #=> "This"
```

## Range acquisition

```ruby
arr = [1, 2, 3, 4, 5, 6]
arr[100]                  #=> nil
arr[-3]                   #=> 4
arr[2, 3]                 #=> [3, 4, 5]
arr[1..4]                 #=> [2, 3, 4, 5]
arr[1..-3]                #=> [2, 3, 4]
```

## Array method fetch

```ruby
arr = ['a', 'b', 'c', 'd', 'e', 'f']
arr.fetch(100)
#=> IndexError: Index outside array bounds 100：-6...6
arr.fetch(100, "oops")    #=> "oops"
```

Out of bounds, give default value

## Get array elements

```ruby
arr = [1, 2, 3, 4, 5, 6]

arr.first     # first value => 1
arr.last      # last value => 6
# take Returns the first n elements
arr.take(3)   #=> [1, 2, 3]
# drop after n elements have been deleted
arr.drop(3)   #=> [4, 5, 6]
```

## Add value to end of array push

```ruby
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numbers.push(11)
#=> [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
numbers.push(12, 13, 14)
#=> [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
```

## Delete the value at the end of the array pop

```ruby
num_array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
num_array.pop             #=> 10
num_array
#=> [1, 2, 3, 4, 5, 6, 7, 8, 9]
```

## Add value to beginning of array unshift

```ruby
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numbers.unshift(0)
#=> [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numbers.unshift(-3, -2, -1)
#=> [-3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
```

## Retrieve and simultaneously delete the first element shift

```ruby
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numbers.shift #=> 1
numbers
#=> [2, 3, 4, 5, 6, 7, 8, 9, 10]
```

## Remove element at specific index delete_at

```ruby
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numbers.delete_at(2) #=> 4
numbers
#=> [2, 3, 5, 6, 7, 8, 9, 10]
```

## Remove a specific element anywhere in an array

```ruby
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numbers.delete(2) #=> 2
numbers           #=> [3, 5, 6, 7, 8, 9, 10]
```

## Insert value at given index insert

```ruby
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numbers.insert(0, 0)
#=> [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numbers.insert(0, -3, -2, -1)
#=> [-3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

numbers.insert(-1, 12, 13, 14)
#=> [-3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 13, 14]
numbers.insert(-4, 11)
#=> [-3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
```

## A block to fill the array with values

```ruby
numbers = Array.new(10) { |n| n = n * 2 }
#=> [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
```

## Filling arrays becomes easier

```ruby
numbers = Array(100..110)
#=> [100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110]

# Or we can convert the range to an array
(100..110).to_a
#=> [100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110]
```

## Remove nil value from array

```ruby
arr = ['foo', 0, nil, 'bar', 7, nil]
arr.compact  #=> ['foo', 0, 'bar', 7]
arr      #=> ['foo', 0, nil, 'bar', 7, nil]
arr.compact! #=> ['foo', 0, 'bar', 7]
arr      #=> ['foo', 0, 'bar', 7]
```

## Remove duplicates uniq

```ruby
arr = [2, 5, 6, 556, 6, 6, 8, 9, 0, 123, 556]
arr.uniq #=> [2, 5, 6, 556, 8, 9, 0, 123]
arr # => [2, 5, 6, 556, 6, 6, 8, 9, 0, 123, 556]
arr.uniq! #=> [2, 5, 6, 556, 8, 9, 0, 123]
arr #=> [2, 5, 6, 556, 8, 9, 0, 123]
```

## Check if a value exists in an array（`include？`）

```ruby
planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
planets.include? "Mars"
# output => true
planets.include? "Pluto"
# output => false
```

## Get array size

```ruby
planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
planets.size
# output => 8
planets.length
# output => 8
```

You can use size or length, both are synonyms

## clear array

```ruby
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numbers.clear
# output => []
```

## Get the first element of the array

```ruby
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numbers[0]
# or
numbers.first
# output => 1
```

## Get the last element of the array

```ruby
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numbers[-1]
# or
numbers.last
# output => 10
```

## Merge two arrays

```ruby
a = ["tom", "mot", "otm"]
b = [2, 3, 5]
a.zip(b)
# output
# [["tom", 2], ["mot", 3], ["otm", 5]]
```

## Sort array

```ruby
primes = [7, 2, 3, 5]
sorted_primes = primes.sort
puts "#{sorted_primes}"
# output => [2, 3, 5, 7]
```

or in-place sort

```ruby
primes = [7, 2, 3, 5]
primes.sort!
puts "#{primes}"
# output => [2, 3, 5, 7]
```

```ruby
planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
planets.sort
# output
# ["Earth", "Jupiter", "Mars", "Mercury", "Neptune", "Saturn", "Uranus", "Venus"]
planets.sort_by { |p| p }
# output
# ["Earth", "Jupiter", "Mars", "Mercury", "Neptune", "Saturn", "Uranus", "Venus"]
planets.sort_by { |p| p.length }
# output
# ["Mars", "Earth", "Venus", "Saturn", "Uranus", "Neptune", "Jupiter", "Mercury"]
```

## Get maximum value from array

```ruby
primes = [7, 2, 3, 5]
primes.max_by { |p| p }
# output => 7
```

## Get array elements using range

```ruby
# numbers[start..end], both index are inclusive
puts numbers[0..3]
# 1
# 2
# 3
# 4
# numbers[start..end], end index is exclusive
puts numbers[0...3]
# 1
# 2
# 3
# or numbers[start..length]
puts numbers[0, 1]
# 1
```

## Get the first n elements of the array

```ruby
primes = [7, 2, 3, 5]
primes.take(3)
# [7, 2, 3]
```

## access element

```ruby
primes = [7, 2, 3, 5]
primes.fetch(3)
# 5
# Fetch will throw an error if the element does not exist
primes.fetch(10)
# (index 10 outside of array bounds: -4...4)
# or get an default value
primes.fetch(10, -1)
# -1
```

## Delete first n elements

```ruby
primes = [7, 2, 3, 5]
primes.drop(3)
# [5]
```

## Delete the first element

```ruby
primes = [7, 2, 3, 5]
primes.shift
# [2, 3, 5]
```

## Remove last element

```ruby
primes = [7, 2, 3, 5]
primes.pop
# [7, 2, 3]
```

## Delete element with index

```ruby
primes = [7, 2, 3, 5]
primes.delete_at(-1)
# [7, 2, 3]
```

## Remove all occurrences of elements

```ruby
primes = [7, 2, 3, 5, 5]
primes.delete(5)
# [7, 2, 3]
```

## each

```ruby
# When you have single line blocks
salary = [399, 234, 566, 533, 233]
salary.each { |s| puts s }
# output
# 399
# 234
# 566
# 533
# 233
```

When you have a multi-line block, you can replace the curly braces `{}` with `do` and `end`

```ruby
salary.each do |s|
  a = 10
  res = a * s
  puts res
end
# output
# 3990
# 2340
# 5660
# 5330
# 2330
```

Or you can do the same thing using braces {} and semicolon as separator instead of newline

```ruby
salary.each { |s| a = 10 ; res = a * s ; puts res }
```

## each_with_index

```ruby
salary = [399, 234, 566, 533, 233]
salary.each_with_index { |value, index| puts "#{index} #{value}" }
# output
# 0 399
# 1 234
# 2 566
# 3 533
# 4 233
```

## each_index

```ruby
salary = [399, 234, 566, 533, 233]
salary.each_index { |i| puts i}
# output
# 0
# 1
# 2
# 3
# 4
```

## map

```ruby
salary = [399, 234, 566, 533, 233]
salary.map { |s|  s * 10  }
# return
# [3990, 2340, 5660, 5330, 2330]
# On the other hand, each returns the original value
salary = [399, 234, 566, 533, 233]
salary.each { |s|  s * 10  }
# return
# [399, 234, 566, 533, 233]
```

## collect

```ruby
salary = [399, 234, 566, 533, 233]
salary.collect { |s| s > 400 }
# output
# [false, false, true, true, false]
```

## for

```ruby
for value in [2, 3, 5, 7]
    puts value
end
```

## each_with_object

```ruby
colors = [
  {color: "red", count: 3}, {color: "red", count: 5}, {color: "black", count: 4}
]
colors.each_with_object(Hash.new(0)) { |color, hash| hash["color_"+color[:color]] = color[:color].upcase; hash["count_"+color[:color]] += color[:count] }
# output
{"color_red"=>"RED", "count_red"=>8, "color_black"=>"BLACK", "count_black"=>4}

[1, 2, 3].each_with_object(0) { |number, sum| sum += number}
# output
# 0
# Because 0 is immutable, and since the initial object is 0, the method returns 0
```

## while

```ruby
planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
index = 0
while index < planets.size
    puts "#{planets[index]}"
    index += 1
end
```

---

```ruby
a = 1
star = '*'
while a <= 10
    puts star
    star += '*'
    a += 1
end
```

## do while

```ruby
planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
index = 0
loop do
    puts "#{planets[index]}"
    index += 1
    break if planets[index] == "Mars" or index > planets.size
end
```

## until

```ruby
planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
index = planets.size - 1
until index < 0
    puts "#{planets[index]}"
    index -= 1
end
```

```ruby
a = 1
star = '*'
until star.length > 10
    puts star
    star += '*'
    a += 1
end
```

## times

```ruby
10.times { puts "#{rand(1..100)}"}
# output
# will print 10 random numbers
```

Just because you can doesn't mean you should iterate over an array like this

```ruby
data_sample = [2, 3, 5, 7]
data_sample.size.times { |index| puts "#{data_sample[index]}" }
# output
# 2
# 3
# 5
# 7
```

## upto

```ruby
data_sample = [2, 3, 5, 7]
0.upto((data_sample.size - 1) / 2) { |index| puts "#{data_sample[index]}" }
# output
# 2
# 3
```

## downto

```ruby
data_sample = [2, 3, 5, 7]
(data_sample.size - 1).downto(data_sample.size / 2) { |index| puts "#{data_sample[index]}" }
# output
# 7
# 5
```

## step

```ruby
1.step(20, 2) { |number| puts "#{number}"}
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

---

```ruby
19.step(1, -2) { |number| puts "#{number}"}
# output
# 19
# 17
# 15
# 13
# 11
# 9
# 7
# 5
# 3
# 1
```

## inject

```ruby
numbers = [2, 2, 2, 2, 2]
numbers.inject{ |res, n| res + n }
# The output is the sum of all numbers
# If no initial value is set for res, the first element of the array is used as the initial value of res.
#10
# Now set the value of res to 11
numbers = [2, 2, 2, 2, 2]
numbers.inject(11) { |res, n| res + n }
# so 11 + 2, 13 + 2, 15 + 2, 17 + 2 and 19 + 2
# 21
# using symbol
numbers = [2, 2, 2, 2, 2]
numbers.inject(:+)
# output
# 10
```

Use initial values and symbols

```ruby
numbers = [2, 2, 2, 2, 2]
numbers.inject(11, :+)
# output
# 21
```

## reduce

```ruby
numbers = [2, 2, 2, 2, 2]
numbers.reduce(11, :+)
# output
# 21
```

## detect

```ruby
planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
planets.detect { |name| name.start_with?("E") and name.end_with?("h") }
# output
# Earth
salary = [399, 234, 566, 533, 233]
salary.detect { |s| s > 1000 }
# output
# nil
```

## find

```ruby
planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
planets.find { |name| name.start_with?("E") and name.end_with?("h") }
# output
# Earth
```

## select

```ruby
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numbers.select { |n| n % 2 == 0 }
# Now you have an even array
# [2, 4, 6, 8, 10]
# If there are no values that satisfy your logic, return an empty array
[1, 1, 1].select { |n| n % 2 == 0 }
# no even numbers
# []
```

## reject

```ruby
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numbers.reject { |n| n % 2 == 0 }
# Reject if the number is even, so now we have an odd array
# [1, 3, 5, 7, 9]
```

## keep_if

```ruby
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numbers.keep_if { |n| n % 2 == 0 }
# numbers Array contains only even numbers
# [2, 4, 6, 8, 10]
```

## delete_if

```ruby
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numbers.delete_if { |n| n % 2 == 0 }
# numbers Array contains only odd numbers
# [1, 3, 5, 7, 9]
```

## drop_while

```ruby
numbers = [1, 2, 3, 1, 2, 3, 0]
numbers.drop_while { |n| n < 3 }
# is 3 less than 3, returns false, so delete 1, 2
# [3, 1, 2, 3, 0]
```

## reverse_each

```ruby
words = %w[first second third fourth fifth sixth]
str = ""
words.reverse_each {|word| str += "#{word} "}
p str #=> "sixth fifth fourth third second first "
```
