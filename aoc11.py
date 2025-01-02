
BLINK_COUNT = 1000


def new_arrangement(array1, iter): # See how the array will behave for each iteration
    newarray = []
    spaces = 6 * iter
    for stone in array1:
        if stone == 0:
            print(f"{0:{spaces}d} ---> 1")
            newarray.append(1)
        elif len(str(stone)) % 2 == 0:  # Even length number
            stone = str(stone)
            print(
                f"{int(stone):{spaces}d} ---> {stone[:len(stone)//2]} and {stone[len(stone)//2:]}")
            newarray.append(int(stone[:len(stone)//2]))
            newarray.append(int(stone[len(stone)//2:]))
        else:
            print(f"{stone:{spaces}d} --->  * 2024 ")
            newarray.append(stone * 2024)

    return newarray


def get_stones_for(a_stone):
    if a_stone == 0:
        return [1]
    elif len(str(a_stone)) % 2 == 0:
        a_stone = str(a_stone)
        return [int(a_stone[:len(a_stone)//2]), int(a_stone[len(a_stone)//2:])]
    else:
        return [a_stone * 2024]


def get_counts_for(stone_map, iter):
    new_map = {}
    for a_key in stone_map.keys():
        next_counts = get_stones_for(a_key)
        for a_count in next_counts:
            if new_map.get(a_count) is None:
                new_map[a_count] = 0 # initialise count for a stone
            new_map[a_count] += stone_map[a_key]
            pass
        pass
    pass
    return new_map

# arrangement = [int(y) for y in open('aoc11-inp.txt').read().strip().split()]
# arrangement = [0, 0]
arrangement = [0, 89741, 316108, 7641, 756, 9, 7832357, 91]

from collections import Counter
stone_map =  dict(Counter(arrangement))

import time
start = time.perf_counter()
for i in range(BLINK_COUNT):
    # print(i)
    # arrangement = new_arrangement(arrangement, i)
    stone_map = get_counts_for(stone_map, i)
end = time.perf_counter()

print(f"Input = {arrangement}")
print(f"Elapsed time for {BLINK_COUNT} iter = {(end - start):.6f} sec ")
print(f"stone_map keys count = {len(stone_map.keys())}")
print('Array length:', sum(stone_map.values()), len(arrangement))
