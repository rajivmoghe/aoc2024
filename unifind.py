from collections import deque, defaultdict

def calculate_regions(grid):
    """
    Calculate the area and boundary length for each region in a grid.
    :param grid: List of lists representing the 2D grid.
    :return: Dictionary containing regions and their areas and boundaries.
    """
    rows, cols = len(grid), len(grid[0])
    visited = [[False] * cols for _ in range(rows)]  # Track visited cells
    regions = defaultdict(lambda: {"area": 0, "boundary": 0})  # Store results
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Up, down, left, right

    def bfs(start_row, start_col):
        """
        Perform BFS to explore a region and calculate its area and boundary.
        :param start_row: Starting row index.
        :param start_col: Starting column index.
        :return: None. Updates `regions` dictionary directly.
        """
        queue = deque([(start_row, start_col)])
        visited[start_row][start_col] = True
        region_type = grid[start_row][start_col]
        area = 0
        boundary = 0

        while queue:
            row, col = queue.popleft()
            area += 1  # Increment area for the current cell

            # Check all four neighbors
            for dr, dc in directions:
                nr, nc = row + dr, col + dc

                # If out of bounds or a different type, count as boundary
                if not (0 <= nr < rows and 0 <= nc < cols) or grid[nr][nc] != region_type:
                    boundary += 1
                # If valid neighbor and not visited, add to queue
                elif not visited[nr][nc]:
                    visited[nr][nc] = True
                    queue.append((nr, nc))

        # Update region info
        regions[region_type]["area"] += area
        regions[region_type]["boundary"] += boundary

    # Traverse the grid
    for r in range(rows):
        for c in range(cols):
            if not visited[r][c]:  # Unvisited cell, start a new region
                bfs(r, c)

    return regions


# Example Usage
import random

# Generate a 100x100 grid with 100+ object types
object_types = [f"O{i}" for i in range(1, 101)]  # Object types: Obj1, Obj2, ..., Obj100
grid = [[random.choice(object_types) for _ in range(100)] for _ in range(100)]

# Calculate regions
regions = calculate_regions(grid)
print(grid)
# Display results
for region, info in regions.items():
    print(f"Region {region}: Area = {info['area']}, Boundary = {info['boundary']}")
