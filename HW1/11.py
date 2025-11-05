def count_paths(rows, cols):
    dp = [[0 for _ in range(cols)] for _ in range(rows)]
    for i in range(rows):
        dp[i][0] = 1
    for j in range(cols):
        dp[0][j] = 1
    for i in range(1, rows):
        for j in range(1, cols):
            dp[i][j] = dp[i-1][j] + dp[i][j-1]
    
    return dp[rows-1][cols-1]


def print_all_paths(rows, cols):
    def find_paths(i, j, path, all_paths):
        if i == rows - 1 and j == cols - 1:
            all_paths.append(path[:])
            return
        if i < rows - 1:
            path.append('↓')
            find_paths(i + 1, j, path, all_paths)
            path.pop()
        if j < cols - 1:
            path.append('→')
            find_paths(i, j + 1, path, all_paths)
            path.pop()
    
    all_paths = []
    find_paths(0, 0, [], all_paths)
    return all_paths


rows, cols = 2, 2

total_paths = count_paths(rows, cols)
print(f"number of currect path in network {rows}x{cols}: {total_paths}")

print("\nAll allowed paths:")
paths = print_all_paths(rows, cols)
for i, path in enumerate(paths, 1):
    print(f"path {i}: {' '.join(path)}")

print("\n" + "-"*50)

print("\nnumber of currect path for different networks:")
for n in range(2, 6):
    result = count_paths(n, n)
    print(f"network {n}x{n}: {result} path")