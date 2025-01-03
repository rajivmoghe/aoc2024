OFFSET = 10000000000000


def check_prize_jumps(record, jump=False):
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


# Example usage
file_path = "aoc13-inp.txt"  # Replace with the actual file path
parsed_data = parse_multiple_records(file_path)
# parsed_data = [{'Ax': 69, 'Ay': 23, 'Bx': 27, 'By': 71,
#                 'Px': 18641, 'Py': 10279}]

tokens = 0

for i, record in enumerate(parsed_data):
    print(f"Record {i + 1}: ", end='')
    prizesteps = check_prize_jumps(record, True)
    if prizesteps[0]:
        token_cost = prizesteps[2]
        print(f"Prize details {prizesteps}")
        tokens += token_cost
    else:
        print(f"gets no prize")

print(f"\nTotal tokens spent = {tokens:.0f}")
