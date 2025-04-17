set1 = set(input("Enter first set (comma-separated): ").split(','))
set2 = set(input("Enter second set (comma-separated): ").split(','))

print(f"Difference (set1 - set2): {set1 - set2}")
print(f"Intersection: {set1 & set2}")
print(f"Union: {set1 | set2}")