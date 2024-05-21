#https://www.hackerrank.com/challenges/walking-the-approximate-longest-path/problem?isFullScreen=false
#https://www.hackerrank.com/challenges/walking-the-approximate-longest-path/problem?isFullScreen=false

def longest_path(adj_list, start):
    visited = set()
    stack = [(start, 0)]
    max_distance = 0

    while stack:
        node, distance = stack.pop()
        visited.add(node)
        max_distance = max(max_distance, distance)

        for neighbor in adj_list[node]:
            if neighbor not in visited:
                stack.append((neighbor, distance + 1))

    return max_distance

# Example usage
if __name__ == "__main__":
    n = int(input())
    adj_list = [[] for _ in range(n + 1)]

    for _ in range(n - 1):
        u, v = map(int, input().split())
        adj_list[u].append(v)
        adj_list[v].append(u)

    start_node = 1  # Choose any node as the starting point
    result = longest_path(adj_list, start_node)
    print(result)

                            