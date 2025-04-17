vector1 = list(map(float, input("Enter first vector (space-separated): ").split()))
vector2 = list(map(float, input("Enter second vector (space-separated): ").split()))

if len(vector1) != len(vector2):
    print("Vectors must be of same length!")
else:
    dot_product = sum(x * y for x, y in zip(vector1, vector2))
    print("Dot product:", dot_product)


# بردار اول: 1 2 3
# بردار دوم: 4 5 6

# (1 × 4) + (2 × 5) + (3 × 6) = 4 + 10 + 18 = 32