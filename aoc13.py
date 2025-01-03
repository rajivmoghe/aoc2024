

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
            print(f"Cost of prize is {cost}")
            return (m_value, n_value, cost)
    pass
    return (None, None)


def part_two(record, jump=False):
    """
    We have to solve a system of linear equations with two variables
    Learned this one at university: https://en.wikipedia.org/wiki/Cramer%27s_rule
    """

    def determinant(v0, v1) -> int:
        ax, ay = v0
        bx, by = v1
        # print(f"V1 {ax}, {ay} :: V2 {bx}, {by}.\nExpr : {ax} * {by} - {bx} * {ay}")
        return ax * by - bx * ay

    cost = 0
    A_ = (record['Ax'], record['Ay'])
    B_ = (record['Bx'], record['By'])
    px, py = record['Px'], record['Py']
    if jump:
        px += OFFSET
        py += OFFSET

    prize = (px, py)

    det = determinant(v0=A_, v1=B_)
    denom = (record['Ax'] * record['By'] - record['Bx'] * record['Ay'])
    # print(f"det vs denom values {det} vs {denom} \n")

    dx = determinant(v0=prize, v1=B_)
    # print(
        # f"num_m: {record['Px']} * {record['By']} - {record['Bx']} * {record['Py']}")
    num_m = (record['Px'] * record['By'] - record['Bx'] * record['Py'])
    # print(f"dm vs num_m values {dx} vs {num_m} \n")

    dy = determinant(v0=B_, v1=prize)
    # print(
        # f"num_n: {record['Ax']} * {record['Py']} - {record['Px']} * {record['Ay']}")
    num_n = (record['Ax'] * record['Py'] - record['Px'] * record['Ay'])
    # print(f"dy vs num_n values {dy} vs {num_n} \n")
    x = dx/det
    y = dy/det
    if x.is_integer() and y.is_integer():
        cost += x * 3
        cost += y
        print(f"Cost of prize is {cost}")

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


# Example usage
file_path = "aoc13-inp.txt"  # Replace with the actual file path
parsed_data = parse_multiple_records(file_path)
# parsed_data = [{'Ax': 69, 'Ay': 23, 'Bx': 27, 'By': 71,
#                 'Px': 18641, 'Py': 10279}]
tokens = 0

for i, record in enumerate(parsed_data):
    print(f"Record {i + 1}: ")
    # prizesteps = check_prize_jumps(record, True)
    prizesteps = part_two(record, True)
    if prizesteps[0] and prizesteps[1]:
        token_cost = prizesteps[2]
        print(f"Prize details {prizesteps}")
        tokens += token_cost
    else:
        print(f"gets no prize")

print(f"\nTotal tokens spent = {tokens}")
