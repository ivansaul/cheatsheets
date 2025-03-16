# Collections Framework

## Java Collections

| Collection                                                                                                         | Interface   | Ordered | Sorted | Thread safe | Duplicate | Nullable           |
| ------------------------------------------------------------------------------------------------------------------ | ----------- | ------- | ------ | ----------- | --------- | ------------------ |
| [ArrayList](https://docs.oracle.com/javase/8/docs/api/java/util/ArrayList.html)                                    | List        | Y       | _N_    | _N_         | Y         | Y                  |
| [Vector](https://docs.oracle.com/javase/8/docs/api/java/util/Vector.html)                                          | List        | Y       | _N_    | Y           | Y         | Y                  |
| [LinkedList](https://docs.oracle.com/javase/8/docs/api/java/util/LinkedList.html)                                  | List, Deque | Y       | _N_    | _N_         | Y         | Y                  |
| [CopyOnWriteArrayList](https://docs.oracle.com/javase/8/docs/api/java/util/concurrent/CopyOnWriteArrayList.html)   | List        | Y       | _N_    | Y           | Y         | Y                  |
| [HashSet](https://docs.oracle.com/javase/8/docs/api/java/util/HashSet.html)                                        | Set         | _N_     | _N_    | _N_         | _N_       | One `null`         |
| [LinkedHashSet](https://docs.oracle.com/javase/8/docs/api/java/util/LinkedHashSet.html)                            | Set         | Y       | _N_    | _N_         | _N_       | One `null`         |
| [TreeSet](https://docs.oracle.com/javase/8/docs/api/java/util/TreeSet.html)                                        | Set         | Y       | Y      | _N_         | _N_       | _N_                |
| [CopyOnWriteArraySet](https://docs.oracle.com/javase/8/docs/api/java/util/concurrent/CopyOnWriteArraySet.html)     | Set         | Y       | _N_    | Y           | _N_       | One `null`         |
| [ConcurrentSkipListSet](https://docs.oracle.com/javase/8/docs/api/java/util/concurrent/ConcurrentSkipListSet.html) | Set         | Y       | Y      | Y           | _N_       | _N_                |
| [HashMap](https://docs.oracle.com/javase/8/docs/api/java/util/HashMap.html)                                        | Map         | _N_     | _N_    | _N_         | _N (key)_ | One `null` _(key)_ |
| [HashTable](https://docs.oracle.com/javase/8/docs/api/java/util/Hashtable.html)                                    | Map         | _N_     | _N_    | Y           | _N (key)_ | _N (key)_          |
| [LinkedHashMap](https://docs.oracle.com/javase/8/docs/api/java/util/LinkedHashMap.html)                            | Map         | Y       | _N_    | _N_         | _N (key)_ | One `null` _(key)_ |
| [TreeMap](https://docs.oracle.com/javase/8/docs/api/java/util/TreeMap.html)                                        | Map         | Y       | Y      | _N_         | _N (key)_ | _N (key)_          |
| [ConcurrentHashMap](https://docs.oracle.com/javase/8/docs/api/java/util/concurrent/ConcurrentHashMap.html)         | Map         | _N_     | _N_    | Y           | _N (key)_ | _N_                |
| [ConcurrentSkipListMap](https://docs.oracle.com/javase/8/docs/api/java/util/concurrent/ConcurrentSkipListMap.html) | Map         | Y       | Y      | Y           | _N (key)_ | _N_                |
| [ArrayDeque](https://docs.oracle.com/javase/8/docs/api/java/util/ArrayDeque.html)                                  | Deque       | Y       | _N_    | _N_         | Y         | _N_                |
| [PriorityQueue](https://docs.oracle.com/javase/8/docs/api/java/util/PriorityQueue.html)                            | Queue       | Y       | _N_    | _N_         | Y         | _N_                |
| [ConcurrentLinkedQueue](https://docs.oracle.com/javase/8/docs/api/java/util/concurrent/ConcurrentLinkedQueue.html) | Queue       | Y       | _N_    | Y           | Y         | _N_                |
| [ConcurrentLinkedDeque](https://docs.oracle.com/javase/8/docs/api/java/util/concurrent/ConcurrentLinkedDeque.html) | Deque       | Y       | _N_    | Y           | Y         | _N_                |
| [ArrayBlockingQueue](https://docs.oracle.com/javase/8/docs/api/java/util/concurrent/ArrayBlockingQueue.html)       | Queue       | Y       | _N_    | Y           | Y         | _N_                |
| [LinkedBlockingDeque](https://docs.oracle.com/javase/8/docs/api/java/util/concurrent/LinkedBlockingDeque.html)     | Deque       | Y       | _N_    | Y           | Y         | _N_                |
| [PriorityBlockingQueue](https://docs.oracle.com/javase/8/docs/api/java/util/concurrent/PriorityBlockingQueue.html) | Queue       | Y       | _N_    | Y           | Y         | _N_                |

{.show-header .left-text}

## ArrayList

```java
List<Integer> nums = new ArrayList<>();

// Adding
nums.add(2);
nums.add(5);
nums.add(8);

// Retrieving
System.out.println(nums.get(0));

// Indexed for loop iteration
for (int i = 0; i < nums.size(); i++) {
    System.out.println(nums.get(i));
}

nums.remove(nums.size() - 1);
nums.remove(0); // VERY slow

for (Integer value : nums) {
    System.out.println(value);
}
```

## HashMap

```java
Map<Integer, String> m = new HashMap<>();
m.put(5, "Five");
m.put(8, "Eight");
m.put(6, "Six");
m.put(4, "Four");
m.put(2, "Two");

// Retrieving
System.out.println(m.get(6));

// Lambda forEach
m.forEach((key, value) -> {
    String msg = key + ": " + value;
    System.out.println(msg);
});
```

## HashSet

```java
Set<String> set = new HashSet<>();
if (set.isEmpty()) {
    System.out.println("Empty!");
}

set.add("dog");
set.add("cat");
set.add("mouse");
set.add("snake");
set.add("bear");

if (set.contains("cat")) {
    System.out.println("Contains cat");
}

set.remove("cat");
for (String element : set) {
    System.out.println(element);
}
```

## ArrayDeque

```java
Deque<String> a = new ArrayDeque<>();

// Using add()
a.add("Dog");

// Using addFirst()
a.addFirst("Cat");

// Using addLast()
a.addLast("Horse");

// [Cat, Dog, Horse]
System.out.println(a);

// Access element
System.out.println(a.peek());

// Remove element
System.out.println(a.pop());
```
