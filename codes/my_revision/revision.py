# The enumerate function adds a counter to an iterable and returns it as an enumerate object. 
fruits = ["apple", "banana", "cherry"]

for index, fruit in enumerate(fruits):
    print(index, fruit)


# The range function generates a sequence of numbers, which is often used for looping a specific number of times in for loops. It can take one, two, or three arguments.
for i in range(5):  # 0, 1, 2, 3, 4
    print(i)

# You can use enumerate in a list comprehension:
fruits = ["apple", "banana", "cherry"]
indexed_fruits = [(index, fruit) for index, fruit in enumerate(fruits)]
print(indexed_fruits)


sum_even = sum(range(0, 11, 2))
print(sum_even)  # Output: 30 (0 + 2 + 4 + 6 + 8 + 10)


words = ["hello", "world"]
print(" ".join(words))  # Output: "hello world"


text = "hello world"
print(text.replace("world", "Python"))  # Output: "hello Python"
