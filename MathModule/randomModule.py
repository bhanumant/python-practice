import random

# random.random(): Random float between 0.0 and 1.0
print("random():", random.random())


# random.uniform(a, b): Random float between a and b
print("uniform(10, 20):", random.uniform(10, 20))


# random.randint(a, b): Random integer between a and b (inclusive)
print("randint(1, 100):", random.randint(1, 100))


# random.randrange(start, stop[, step]): Like range(), returns a random element
print("randrange(1, 10):", random.randrange(1, 10))         # e.g., 3
print("randrange(0, 100, 5):", random.randrange(0, 100, 5))  # e.g., 85


# random.choice(seq): Random item from a non-empty sequence
colors = ["red", "green", "blue", "yellow"]
print("choice(colors):", random.choice(colors))


# random.choices(seq, k=): Returns a list of k random items (with replacement)
print("choices(colors, k=3):", random.choices(colors, k=3))


# random.sample(seq, k): Returns k unique random items (no replacement)
print("sample(colors, k=2):", random.sample(colors, k=2))


# random.shuffle(seq): Shuffles the list in place
numbers = [1, 2, 3, 4, 5]
random.shuffle(numbers)
print("shuffle(numbers):", numbers)


# random.betavariate(alpha, beta): Beta distribution
print("betavariate(2, 5):", random.betavariate(2, 5))


# random.expovariate(lambda): Exponential distribution
print("expovariate(1):", random.expovariate(1))


# random.gauss(mu, sigma): Gaussian distribution (normal distribution)
print("gauss(0, 1):", random.gauss(0, 1))


# random.normalvariate(mu, sigma): Similar to gauss
print("normalvariate(0, 1):", random.normalvariate(0, 1))


# random.lognormvariate(mu, sigma): Log-normal distribution
print("lognormvariate(0, 1):", random.lognormvariate(0, 1))


# random.triangular(low, high, mode): Triangular distribution
print("triangular(10, 20, 15):", random.triangular(10, 20, 15))


# random.weibullvariate(alpha, beta): Weibull distribution
print("weibullvariate(1, 1.5):", random.weibullvariate(1, 1.5))



# Set seed for reproducibility (same output each time)
random.seed(42)
print("random() with seed 42:", random.random())

# Reset seed and get same result again
random.seed(42)
print("random() again with seed 42:", random.random())
