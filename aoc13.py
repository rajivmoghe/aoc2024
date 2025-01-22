OFFSET = 10000000000000


def check_prize_jumps(record, jump=False):
    """This works correctly with the Offset (part 2)"""
    if jump:
        record['Px'] += OFFSET
        record['Py'] += OFFSET

    denom = record['Ax'] * record['By'] - record['Bx'] * record['Ay']
    num_m = record['Px'] * record['By'] - record['Bx'] * record['Py']
    m_value = num_m / denom

    if m_value.is_integer():
        num_n = record['Ax'] * record['Py'] - record['Px'] * record['Ay']
        n_value = num_n / denom

        if n_value.is_integer():
            cost = m_value * 3 + n_value
            # print(f"Cost of prize is {cost}")
            return (m_value, n_value, cost)

    return (None, None, None)


def solve_linear_system(mc, jump=False):
    """
    Solves:
    a*x + b*y = e
    c*x + d*y = f

    For some strange reason this does not work correctly for part 2
    """
    a, b = mc['Ax'], mc['Ay']
    c, d = mc['Bx'], mc['By']

    e, f = mc['Px'], mc['Py']
    
    if jump:
        e += OFFSET
        f += OFFSET
    print(a,b, c, d, e, f)
    # Determinant of the coefficient matrix
    det = a * d - b * c
    print(f"det {det}")
 
    if det == 0:
        raise ValueError("The system has no unique solution (determinant is zero).")
 
    # Using Cramer's Rule to find x and y
    x = (d * e - c * f)
    print(f"x-det {x}")
    x = x / det
    print(x)
    y = (a * f - b * e)
    print(f"y-det {y}")
    y = y / det
    print(y)
    cost = 3 * x + y
    print(f"Cost = {cost}")
 
    return (x, y, cost)

def parse_multiple_records(file_path):
    """
    Parses a file with multiple records separated by empty lines.

    Parameters:
    file_path (str): Path to the input file.

    Returns:
    list[dict]: A list of dictionaries, each containing keys Ax, Ay, Bx, By, Px, Py.
    """
    all_records = []
    record = {"Ax": None, "Ay": None, "Bx": None,
              "By": None, "Px": None, "Py": None}

    with open(file_path, 'r') as file:
        for line in file:
            line = line.strip()
            if not line:  # Empty line indicates end of a record
                if any(record.values()):  # Save the record if it contains any data
                    all_records.append(record)
                    record = {"Ax": None, "Ay": None, "Bx": None,
                              "By": None, "Px": None, "Py": None}
            elif line.startswith("Button A:"):
                parts = line.split(", ")
                record["Ax"] = int(parts[0].split("+")[1])
                record["Ay"] = int(parts[1].split("+")[1])
            elif line.startswith("Button B:"):
                parts = line.split(", ")
                record["Bx"] = int(parts[0].split("+")[1])
                record["By"] = int(parts[1].split("+")[1])
            elif line.startswith("Prize:"):
                parts = line.split(", ")
                record["Px"] = int(parts[0].split("=")[1])
                record["Py"] = int(parts[1].split("=")[1])

    # Add the last record if the file doesn't end with an empty line
    if any(record.values()):
        all_records.append(record)

    return all_records


test = False
file_path = "aoc13-inp.txt"  # Replace with the actual file path
parsed_data = []

if not test:
    parsed_data = parse_multiple_records(file_path)
else: 
    parsed_data = [{'Ax': 94, 'Ay': 34, 'Bx': 22, 'By': 67,
                    'Px': 8400, 'Py': 5400}] # 1
    parsed_data.append({'Ax': 26, 'Ay': 66, 'Bx': 67, 'By': 21,
                    'Px': 12748, 'Py': 12176}) # 2
    parsed_data.append({'Ax': 17, 'Ay': 86, 'Bx': 84, 'By': 37,
                    'Px': 7870, 'Py': 6450}) #3
    parsed_data.append({'Ax': 69, 'Ay': 23, 'Bx': 27, 'By': 71,
                    'Px': 18641, 'Py': 10279}) #4

tokens = 0

for i, mc in enumerate(parsed_data):
    # print(f"\nRecord {i + 1}: ", end='')
    prizesteps = check_prize_jumps(mc, True)
    # prizesteps = solve_linear_system(mc, True)
    if prizesteps[0] and prizesteps[0].is_integer():
        token_cost = prizesteps[2]
        # print(f"Prize details {prizesteps}")
        tokens += token_cost
    else:
        pass
        # print(f"gets no prize")

print(f"\nTotal tokens spent = {tokens:.0f}")
