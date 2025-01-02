import re

def process_string_generator(input_string):
    """
    Generator to yield only valid 'mul(...)' instructions 
    based on 'do()' and 'don't()' states.
    """
    do_pattern = r"do\(\)"
    dont_pattern = r"don't\(\)"
    mul_pattern = r"mul\(\d{1,3},\d{1,3}\)"
    combined_pattern = f"{do_pattern}|{dont_pattern}|{mul_pattern}"

    active = True

    for match in re.finditer(combined_pattern, input_string):
        match_str = match.group()
        if match_str == "do()":
            active = True
        elif match_str == "don't()":
            active = False
        elif active and match_str.startswith("mul"):
            yield match_str

def find_mul_instructions(input_string):
    """
    Generator to find all 'mul' instructions in the format "mul(A,B)"
    where A and B are integers with 1 to 3 digits.

    Parameters:
    input_string (str): The string to search for instructions.

    Yields:
    str: The next complete 'mul' instruction found.
    """
    # Regular expression for the "mul(A,B)" pattern
    pattern = re.compile(r"mul\(\d{1,3},\d{1,3}\)")

    # At the beginning of the program, mul instructions are enabled
    do_sum = True

    # Use re.finditer to lazily find all matches
    for match in pattern.finditer(input_string):
        yield match.group()  # Yield the matched string


# Example usage
test_string = "random text mul(12,34) more text mul(123,456) invalid mul(12,3x)"
test_string = ''.join(line.strip() for line in open('aoc03-inp.txt'))
generator = find_mul_instructions(test_string)

def mul(a, b):
    return a*b

count = 0
count2 = 0
sum = 0
sum2 = 0
for instruction in generator:
    count += 1
    sum += eval(instruction)
    # print(count, instruction)

generator2 = process_string_generator(test_string)
for valid_mul in generator2:
    count2 += 1
    sum2 += eval(valid_mul)
    # print(valid_mul)

print(f"Sum of {count} instructions is {sum}")
print(f"Sum of {count2} filtered instructions is {sum2}")