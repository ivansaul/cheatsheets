# Combination Method

## Combination method

- `&` Returns a new array containing each element found in array and array other_array; duplicates are omitted; use eql?
  to compare items
- `intersection` Returns a new array containing each element found in self and all given arrays other_arrays; duplicates
  are omitted; use eql? to compare items
- `+` Returns an array containing all elements of self followed by all elements of the given array
- `-` Returns an array containing all elements of self not found in the given array
- `union` Returns an array containing all elements of self and all elements of the given array, with duplicates removed
- `difference` Returns an array containing all elements of self not found in any given array
- `product` self Returns or produces all combinations of elements from self and the given array

## &

```ruby
[0, 1, 2, 3] & [1, 2] # => [1, 2]
[0, 1, 0, 1] & [0, 1] # => [0, 1]
```

## intersection

```ruby
[0, 1, 2, 3].intersection([0, 1, 2], [0, 1, 3])
# => [0, 1]
[0, 0, 1, 1, 2, 3].intersection([0, 1, 2], [0, 1, 3])
# => [0, 1]
```

## +

```ruby
a = [0, 1] + [2, 3]
a # => [0, 1, 2, 3]
```

## -

```ruby
[0, 1, 1, 2, 1, 1, 3, 1, 1] - [1]
# => [0, 2, 3]
[0, 1, 2, 3] - [3, 0]
# => [1, 2]
[0, 1, 2] - [4]
# => [0, 1, 2]
```

## union

```ruby
[0, 1, 2, 3].union([4, 5], [6, 7])
# => [0, 1, 2, 3, 4, 5, 6, 7]
[0, 1, 1].union([2, 1], [3, 1])
# => [0, 1, 2, 3]
[0, 1, 2, 3].union([3, 2], [1, 0])
# => [0, 1, 2, 3]
```

## difference

```ruby
[0, 1, 1, 2, 1, 1, 3, 1, 1].difference([1])
# => [0, 2, 3]
[0, 1, 2, 3].difference([3, 0], [1, 3])
# => [2]
[0, 1, 2].difference([4])
# => [0, 1, 2]
```

## product

```ruby
a = [0, 1, 2]
a1 = [3, 4]
p = a.product(a1)
p.size # => 6 # a.size * a1.size
p # => [[0, 3], [0, 4], [1, 3], [1, 4], [2, 3], [2, 4]]
```
