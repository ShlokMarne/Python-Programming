def get_min_max(numbers):
    return min(numbers), max(numbers)

numbers = [4, 1, 7, 3, 9, 5]
minimum, maximum = get_min_max(numbers)
print("Minimum:", minimum)
print("Maximum:", maximum)