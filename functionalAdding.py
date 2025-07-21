sum = 0

for num in range(5, 101, 5):
    if num % 5 == 0:
        sum += num

print("Sum is ", sum)