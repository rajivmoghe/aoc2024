
def check_good_array(report):
    """
    Checks if the array is good and finds the index of the first anomaly.

    Parameters:
    arr (list): List of integers (elements between -3 and +3).

    Returns:
    tuple: (is_good, anomaly_index)
           is_good (bool): True if the array is good, False otherwise.
           anomaly_index (int): Index of the first anomaly, or -1 if the array is good.
    """
    differences = [report[i+1] - report[i] for i in range(len(report) - 1)]
    loop = True
    while(loop):
        loop = False
        if not differences:  # Handle empty array case
            return True, -1

        # Determine the expected sign of the array based on the first non-zero element
        expected_sign = None
        for i, num in enumerate(differences):
            if num > 0:
                expected_sign = 1
                break
            elif num < 0:
                expected_sign = -1
                break

        # If no non-zero elements, the array is bad (all zeros)
        if expected_sign is None:
            return False, 0  # All zeros, anomaly at the start

        # Traverse the array to check for anomalies
        for i, num in enumerate(differences):
            if num == 0:  # Check for zero
                return False, i
            if (expected_sign == 1 and (num < 0 or num > 3)) or (expected_sign == -1 and (num < -3 or num > 0)):  # Sign-flip check
                return False, i

        # If no anomalies are found, the array is good
        return True, -1


# Define a function to check if a report is safe
def is_safe(ii, report, v=0):
    differences = [report[i+1] - report[i] for i in range(len(report) - 1)]

    # Check if all differences are within the allowed range
    if not all(1 <= abs(diff) <= 3 for diff in differences):
        print(f"Safe Function Report {ii}-{v} {report} fails differences")
        return False
    print(f"Safe Function Report {ii}-{v} {report} is Safe")
    return True

    # Check if all differences are either strictly positive (increasing) or strictly negative (decreasing)
    # is_increasing = all(diff > 0 for diff in differences)
    # is_decreasing = all(diff < 0 for diff in differences)
    # return is_increasing or is_decreasing

def check_report(idxr, report):
    print(f"\nReport Number: {idxr} start.")
    retVal = True

    is_good, anomaly_index = check_good_array(report)
    if is_good:
        print(f"Report {idxr}-0 good. Checking differences")
        retVal = is_safe(idxr, report,0)
    else:
        print(f"Report {idxr}-0 {report} fails at {anomaly_index}. Checking splits")

        report1 = report[:anomaly_index] + report[anomaly_index+1:]
        r1ok, _ = check_good_array(report1)
        if not r1ok :
            print(f"Report {idxr}-1 {report1} fails at {anomaly_index}. No further splits")
            r1cok = False
        else:
            r1cok = is_safe(idxr, report1, 1) 
        
        report2 = report[:anomaly_index+1] + report[anomaly_index+2:]
        r2ok , _ = check_good_array(report2)
        if not r2ok :
            print(f"Report {idxr}-2 {report2} fails at {anomaly_index}. No further splits")
            r2cok = False
        else:
            r2cok = is_safe(idxr, report2, 2) 

        retVal = r1cok or r2cok

    return retVal


# Read the input data (replace 'data.txt' with the actual file name if needed)
filename = "aoc02-inp.txt"
safe_count = 0  # Counter for safe reports
index = 0

# with open(filename, 'r') as file:
#     for line in file:
#         if line.strip():  # Ensure the line is not empty
#             index += 1
#             report = list(map(int, line.split()))  # Convert the line into a list of integers
#             if check_report(index, report):
#                 print(f"Report {index} is Safe")
#                 safe_count += 1
#             else:
#                 print(f"Report {index} is Not Safe")
#                 pass
#         # if index >= 10:
#         #     break

def is_safe_row(row):  
    inc = [row[i + 1] - row[i] for i in range(len(row) - 1)]
    xx = set(inc)
    return xx <= {1, 2, 3} or xx <= {-1, -2, -3}

data = [[int(y) for y in x.split(' ')] for x in open('aoc02-inp.txt').read().split('\n')]

# safe_count = 0
# for arow in data:
#     if is_safe_row(arow):
#         safe_count += 1
# safe_count = sum(is_safe_row(row) for row in data)


# Brute force hacking - not much fun to do check all and be happy at the first good one
safe_count = sum(any( \
        is_safe_row(row[:i] + row[i + 1:]) for i in range(len(row)) \
        ) for row in data)

# Print the number of safe reports
print(f"Number of safe reports: {safe_count}")
