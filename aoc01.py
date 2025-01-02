from collections import Counter

# Define the hardcoded filename
filename = "input01-1.txt"

# Initialize two empty arrays
array1 = []
array2 = []

# Read the file and populate the arrays
with open(filename, 'r') as file:
    for line in file:
        if line.strip():  # Ensure the line is not empty
            col1, col2 = map(int, line.split())  # Convert to float (or int if needed)
            array1.append(col1)
            array2.append(col2)

counts = Counter(array2)
similarity = 0

# Sum of distances - for part 1
# sumarr1 = sorted(array1)
# sumarr2 = sorted(array2)
# sum = 0
# for idx in range(len(array1)):
#     sum += abs(array1[idx] - array2[idx])

# print(f"End of Function Distance {sum}")

# print(counts)
for i in range(len(array1)):
    similarity += array1[i] * counts[array1[i]]
    # print (f"{array1[i]}\t{counts[array1[i]]}")

print(similarity)
