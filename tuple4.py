combined = [("Alice", 25), ("Bob", 30), ("Charlie", 35)]

names, ages = zip(*combined)
print("Names:", names)
print("Ages:", ages)