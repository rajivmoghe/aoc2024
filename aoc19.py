

def can_form_design_rec(towel_patterns, design):
    # Base case: if design is empty, it can be formed
    if design == "":
        return True
    # Try to match the beginning of the design with each towel pattern
    for pattern in towel_patterns:
        if design.startswith(pattern):
            # Recursively check if the rest of the design can be formed
            if can_form_design_rec(towel_patterns, design[len(pattern):]):
                return True
    return False


def can_form_design_itr(towel_patterns, design):
    # Create a queue for iterative processing
    queue = [design]

    while queue:
        current_design = queue.pop(0)
        # If the current design is empty, it can be formed
        if current_design == "":
            return True
        # Try to match the beginning of the current design with each towel pattern
        for pattern in towel_patterns:
            if current_design.startswith(pattern):
                # Add the remaining part of the design to the queue for further processing
                queue.append(current_design[len(pattern):])

    return False


def can_form_design_dyn(towel_patterns, design):
    n = len(design)
    dp = [0] * (n + 1)
    dp[0] = 1  # There is one way to form an empty design

    for i in range(1, n + 1):
        for pattern in towel_patterns:
            pattern_len = len(pattern)
            if i >= pattern_len and design[i - pattern_len:i] == pattern:
                dp[i] += dp[i - pattern_len]

    # print(f"Ways of design {design} \n {dp}")
    return dp[n]


def main():
    towel_patterns = []
    designs = 0
    ways = 0
    linenum = 1

    with open("aoc19-inp.txt", "r") as file:
        # Read towel patterns from the first line
        towel_patterns = next(file).strip().split(", ")

        # Skip the second line
        next(file)

        # Stream read designs line by line
        for line in file:
            design = line.strip()
            waycount = can_form_design_dyn(towel_patterns, design)
            if waycount > 0:
                # print(f"{design} {linenum} can be formed in {waycount} ways.")
                designs += 1
                ways += waycount
            else:
                # print(f"{design} {linenum} cannot be formed.")
                pass
            linenum += 1

    print(f"Number of designs that can be formed = {designs}")
    print(f"Number of ways in which those be formed = {ways}")


if __name__ == "__main__":
    main()
