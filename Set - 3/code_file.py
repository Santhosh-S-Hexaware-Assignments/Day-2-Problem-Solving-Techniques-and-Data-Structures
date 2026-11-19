
# ------------------------------------------------------------
# 1. Binary Search Tree - Hub Codes
# ------------------------------------------------------------

# Node Class
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


# Binary Search Tree Class
class BinarySearchTree:
    def __init__(self):
        self.root = None

    # Insert Function
    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            self.__insert(self.root, value)

    def __insert(self, root, value):
        if value < root.value:
            if root.left is None:
                root.left = Node(value)
            else:
                self.__insert(root.left, value)

        elif value > root.value:
            if root.right is None:
                root.right = Node(value)
            else:
                self.__insert(root.right, value)

    # Search Function
    def search(self, value):
        return self.__search(self.root, value)

    def __search(self, root, value):
        if root is None:
            return False

        if root.value == value:
            return True
        elif value < root.value:
            return self.__search(root.left, value)
        else:
            return self.__search(root.right, value)

    # Inorder Traversal
    def inorder(self):
        values = []
        self.__inorder(self.root, values)
        return values

    def __inorder(self, root, values):
        if root is not None:
            self.__inorder(root.left, values)
            values.append(root.value)
            self.__inorder(root.right, values)

    # Height of the Tree
    def height(self):
        return self.__height(self.root)

    def __height(self, root):
        if root is None:
            return -1

        left_height = self.__height(root.left)
        right_height = self.__height(root.right)

        return 1 + max(left_height, right_height)


# Sample Hub Codes
hub_codes = [
    "HUB-05", "HUB-03", "HUB-08", "HUB-02", "HUB-04",
    "HUB-07", "HUB-10", "HUB-01", "HUB-06", "HUB-09"
]

bst = BinarySearchTree()

for hub in hub_codes:
    bst.insert(hub)

print("1. BINARY SEARCH TREE")
print("Inorder Traversal:", bst.inorder())
print("Search HUB-07:", bst.search("HUB-07"))
print("Search HUB-11:", bst.search("HUB-11"))
print("Tree Height:", bst.height(), "edges")

# Empty Tree Test
empty_bst = BinarySearchTree()
print("Empty Tree Height:", empty_bst.height())


# ------------------------------------------------------------
# 2. Hash Map - Duplicate Parcel Scans
# ------------------------------------------------------------

def find_duplicate_scans(scans):
    scanned_parcels = {}
    duplicates = []

    for tracking_number, hub in scans:
        key = (tracking_number, hub)

        if key in scanned_parcels:
            duplicates.append(key)
        else:
            scanned_parcels[key] = True

    return duplicates


# Sample Parcel Scan Records
parcel_scans = [
    ("TRK100", "HUB-01"),
    ("TRK101", "HUB-02"),
    ("TRK100", "HUB-01"),
    ("TRK100", "HUB-03"),
    ("TRK102", "HUB-05"),
    ("TRK101", "HUB-02"),
    ("TRK103", "HUB-04"),
    ("TRK102", "HUB-06")
]

print("\n2. HASH MAP - DUPLICATE PARCEL SCANS")
print("Duplicate Scans:", find_duplicate_scans(parcel_scans))

# Empty Input Test
print("Empty Scan List:", find_duplicate_scans([]))


# ------------------------------------------------------------
# 3. Graph - Hub Routes (BFS and DFS)
# ------------------------------------------------------------

# Adjacency List
hub_graph = {
    "HUB-01": ["HUB-02", "HUB-03"],
    "HUB-02": ["HUB-04", "HUB-05"],
    "HUB-03": ["HUB-05", "HUB-06"],
    "HUB-04": ["HUB-07"],
    "HUB-05": ["HUB-04", "HUB-07", "HUB-08"],
    "HUB-06": ["HUB-08"],
    "HUB-07": ["HUB-09"],
    "HUB-08": ["HUB-07", "HUB-09", "HUB-10"],
    "HUB-09": ["HUB-10"],
    "HUB-10": []
}


# Breadth First Search - Fewest Hops
def shortest_route(graph, start, destination):
    if start not in graph or destination not in graph:
        return None

    queue = [(start, [start])]
    visited = {start}

    while queue:
        current, path = queue.pop(0)

        if current == destination:
            return path

        for neighbour in graph[current]:
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append((neighbour, path + [neighbour]))

    return None


# Depth First Search - Reachable Hubs
def reachable_hubs(graph, start):
    if start not in graph:
        return []

    visited = set()
    traversal = []

    def dfs(current):
        visited.add(current)
        traversal.append(current)

        for neighbour in graph[current]:
            if neighbour not in visited:
                dfs(neighbour)

    dfs(start)
    return traversal


print("\n3. GRAPH - HUB ROUTES")
print("Adjacency List:")

for hub, routes in hub_graph.items():
    print(hub, "->", routes)

print("Shortest Route (HUB-01 to HUB-10):",
      shortest_route(hub_graph, "HUB-01", "HUB-10"))

print("Hubs Reachable from HUB-01:",
      reachable_hubs(hub_graph, "HUB-01"))

# Unreachable Destination Test
print("Route to Unknown Hub:",
      shortest_route(hub_graph, "HUB-01", "HUB-11"))


# ------------------------------------------------------------
# 4. Sliding Window - Highest Average 4-Hour Window
# ------------------------------------------------------------

def highest_average_window(parcel_counts, window_size):
    if window_size <= 0 or window_size > len(parcel_counts):
        return None

    current_sum = sum(parcel_counts[:window_size])
    max_sum = current_sum
    best_start = 0

    for i in range(window_size, len(parcel_counts)):
        current_sum += parcel_counts[i]
        current_sum -= parcel_counts[i - window_size]

        if current_sum > max_sum:
            max_sum = current_sum
            best_start = i - window_size + 1

    average = max_sum / window_size

    return best_start, best_start + window_size - 1, average


# Hourly Parcel Counts (24 Hours)
hourly_parcels = [
    42, 50, 48, 65, 70, 68,
    55, 80, 90, 85, 75, 95,
    100, 88, 92, 110, 105, 98,
    120, 115, 108, 130, 125, 118
]

result = highest_average_window(hourly_parcels, 4)

print("\n4. SLIDING WINDOW - PARCEL COUNTS")

if result is not None:
    start, end, average = result
    print("Highest Average 4-Hour Window:")
    print("Starting Hour:", start + 1)
    print("Ending Hour:", end + 1)
    print("Average Parcels:", round(average, 2))

# Invalid Window Test
print("Invalid Window:",
      highest_average_window(hourly_parcels, 25))


# ------------------------------------------------------------
# 5. Two Pointers - Palindrome Route Description
# ------------------------------------------------------------

def is_palindrome_route(route):
    # Split using common route separators.
    # Hyphens inside hub codes are preserved.
    import re

    hubs = [
        hub.strip().upper()
        for hub in re.split(r"\s*(?:->|[,|/])\s*", route)
        if hub.strip()
    ]

    left = 0
    right = len(hubs) - 1

    while left < right:
        if hubs[left] != hubs[right]:
            return False

        left += 1
        right -= 1

    return True


# Sample Route Descriptions
route_one = "HUB-01 -> HUB-03 -> HUB-05 -> HUB-03 -> HUB-01"
route_two = "HUB-01 -> HUB-02 -> HUB-04 -> HUB-05"
route_three = "hub-01 | hub-03 | hub-01"

print("\n5. TWO POINTERS - PALINDROME ROUTE")
print("Route 1:", is_palindrome_route(route_one))
print("Route 2:", is_palindrome_route(route_two))
print("Route 3:", is_palindrome_route(route_three))

# Empty Route Test
print("Empty Route:", is_palindrome_route(""))
