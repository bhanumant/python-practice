from collections import deque

d = [1, 2, 3, 4, 5, 6]
q = deque(d)
print("Initial deque:", q)

# append(x): Add to right end
q.append(66)
print("After append(66):", q)


# appendleft(x): Add to left end
q.appendleft(5555)
print("After appendleft(5555):", q)


# pop(): Remove from right end
q.pop()
print("After pop():", q)


# popleft(): Remove from left end
q.popleft()
print("After popleft():", q)


# extend(iterable): Add multiple elements to right end
q.extend([10, 20, 30])
print("After extend([10, 20, 30]):", q)


# extendleft(iterable): Add multiple to left end (in reverse)
q.extendleft([11, 22, 33])
print("After extendleft([11, 22, 33]):", q)
# deque becomes [33, 22, 11, ..., 30]


# rotate(n): Rotate right by n steps
q.rotate(2)
print("After rotate(2):", q)


# rotate(-n): Rotate left by n steps
q.rotate(-3)
print("After rotate(-3):", q)


# clear(): Remove all elements
q.clear()
print("After clear():", q)


# Re-initialize for more methods
q = deque([100, 200, 300, 400, 500])
print("\nReinitialized deque:", q)


# len(): Get number of elements
print("Length of deque:", len(q))


# index(x): Return index of first occurrence
print("Index of 300:", q.index(300))


# count(x): Count occurrences of x
q.append(300)
print("Count of 300:", q.count(300))  # Should be 2


# insert(i, x): Insert x at position i
q.insert(2, 999)
print("After insert(2, 999):", q)

# remove(x): Remove first occurrence of x
q.remove(300)
print("After remove(300):", q)

# maxlen: Set fixed length deque (newest pushes out oldest)
fixed_q = deque([1, 2, 3], maxlen=4)
fixed_q.append(4)
fixed_q.append(5)
print("Fixed-length deque:", fixed_q)  # deque([2, 3, 4, 5])
