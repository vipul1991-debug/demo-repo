# Print all even numbers until 10 without mentiong iterator in range
counter = 0
for number in range(2, 10):
    if number % 2 == 0:
        print(number)
        counter += 1
print(f"we have {counter} even numbers until 10")
