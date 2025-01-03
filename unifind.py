from collections import deque, defaultdict

def find_regions_and_aggregates(grid):
    """
    Finds individual region parameters and aggregated totals for each object type.

    Parameters:
    grid (list[list[str]]): 2D grid containing object types as elements.

    Returns:
    tuple: (regions, aggregates)
           regions: dict with {(object_type, region_id): (area, boundary)}
           aggregates: dict with {object_type: (total_area, total_boundary)}
    """
    rows, cols = len(grid), len(grid[0])
    visited = [[False] * cols for _ in range(rows)]  # Track visited cells
    regions = {}  # Individual region data
    aggregates = defaultdict(lambda: [0, 0])  # Aggregated totals for each object type
    region_id = 0  # Unique ID for each region

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Neighbor directions

    def bfs(start_row, start_col):
        """Perform BFS to traverse the region and calculate area and boundary."""
        nonlocal region_id
        obj_type = grid[start_row][start_col]
        queue = deque([(start_row, start_col)])
        visited[start_row][start_col] = True
        area = 0
        boundary = 0

        while queue:
            r, c = queue.popleft()
            area += 1

            # Check all 4 neighbors
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols:
                    if grid[nr][nc] == obj_type and not visited[nr][nc]:
                        visited[nr][nc] = True
                        queue.append((nr, nc))
                    elif grid[nr][nc] != obj_type:
                        boundary += 1
                else:
                    # Out-of-bounds contributes to the boundary
                    boundary += 1

        # Save individual region data
        regions[(obj_type, region_id)] = (area, boundary)

        # Update aggregate data
        aggregates[obj_type][0] += area
        aggregates[obj_type][1] += boundary

        region_id += 1

    # Traverse the grid to identify all regions
    for r in range(rows):
        for c in range(cols):
            if not visited[r][c]:
                bfs(r, c)

    return regions, aggregates


# Example usage
if __name__ == "__main__":
    # Example 100x100 grid with up to 100 object types (use smaller for demonstration)
    import random
    random.seed(42)
    object_types = [chr(65 + i) for i in range(26)]  # Object types: 'A' to 'Z'
    grid = [[random.choice(object_types) for _ in range(100)] for _ in range(100)]

    # Process the grid
    regions, aggregates = find_regions_and_aggregates(grid)

    # Print results
    print("Individual Regions:")
    for (obj_type, region_id), (area, boundary) in list(regions.items())[:10]:  # Show only first 10 for brevity
        print(f"Object: {obj_type}, Region ID: {region_id}, Area: {area}, Boundary: {boundary}")

    print("\nAggregated Totals:")
    for obj_type, (total_area, total_boundary) in aggregates.items():
        print(f"Object: {obj_type}, Total Area: {total_area}, Total Boundary: {total_boundary}")
