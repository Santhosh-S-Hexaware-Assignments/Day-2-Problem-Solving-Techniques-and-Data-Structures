
from collections import deque
from time import time


# ============================================================
# TASK 1 - BINARY SEARCH TREE
# ============================================================

# Node Class
class Node:
    def __init__(self, value: str) -> None:
        self.value = value
        self.left = None
        self.right = None


# Binary Search Tree Class
class BinarySearchTree:
    def __init__(self) -> None:
        self.root = None

    # Insert Function
    def insert(self, value: str) -> None:
        if self.root is None:
            self.root = Node(value)
        else:
            self.__insert(self.root, value)

    # Recursive Insert
    def __insert(self, root: Node, value: str) -> None:
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
    def search(self, value: str) -> bool:
        return self.__search(self.root, value)

    # Recursive Search
    def __search(self, root: Node | None, value: str) -> bool:
        if root is None:
            return False

        if root.value == value:
            return True

        if value < root.value:
            return self.__search(root.left, value)

        return self.__search(root.right, value)

    # Inorder Traversal
    def inorder(self) -> list[str]:
        result = []
        self.__inorder(self.root, result)
        return result

    def __inorder(self, root: Node | None, result: list[str]) -> None:
        if root is not None:
            self.__inorder(root.left, result)
            result.append(root.value)
            self.__inorder(root.right, result)

    # Preorder Traversal
    def preorder(self) -> list[str]:
        result = []
        self.__preorder(self.root, result)
        return result

    def __preorder(self, root: Node | None, result: list[str]) -> None:
        if root is not None:
            result.append(root.value)
            self.__preorder(root.left, result)
            self.__preorder(root.right, result)

    # Postorder Traversal
    def postorder(self) -> list[str]:
        result = []
        self.__postorder(self.root, result)
        return result

    def __postorder(self, root: Node | None, result: list[str]) -> None:
        if root is not None:
            self.__postorder(root.left, result)
            self.__postorder(root.right, result)
            result.append(root.value)


# Sample Product Categories
categories = [
    "Electronics",
    "Clothing",
    "Footwear",
    "Books",
    "Furniture",
    "Groceries",
    "Beauty",
    "Sports",
    "Toys",
    "Automotive",
    "Jewellery",
    "Kitchen",
    "Stationery",
    "Luggage",
    "Pet Supplies"
]

# Creating Binary Search Tree
category_tree = BinarySearchTree()

for category in categories:
    category_tree.insert(category)

# Display Traversals
print("\n========== TASK 1: BINARY SEARCH TREE ==========")

print("Inorder Traversal   :", category_tree.inorder())
print("Preorder Traversal  :", category_tree.preorder())
print("Postorder Traversal :", category_tree.postorder())

# Search Test Cases
print("\nSearch Results:")
print("Electronics :", category_tree.search("Electronics"))
print("Furniture   :", category_tree.search("Furniture"))
print("Medicines   :", category_tree.search("Medicines"))


# ============================================================
# TASK 2 - HASHING AND HASH MAPS
# ============================================================

# Hash Table Class using Separate Chaining
class HashTable:
    def __init__(self, capacity: int = 200003) -> None:
        self.capacity = capacity
        self.table = [[] for _ in range(capacity)]

    # Hash Function
    def __hash_function(self, key: str) -> int:
        hash_value = 0

        for character in key:
            hash_value = (hash_value * 31 + ord(character)) % self.capacity

        return hash_value

    # Insert Function
    def insert(self, key: str, value: str) -> None:
        index = self.__hash_function(key)

        for pair in self.table[index]:
            if pair[0] == key:
                pair[1] = value
                return

        self.table[index].append([key, value])

    # Search Function
    def search(self, key: str) -> str | None:
        index = self.__hash_function(key)

        for stored_key, stored_value in self.table[index]:
            if stored_key == key:
                return stored_value

        return None


print("\n========== TASK 2: HASHING AND HASH MAPS ==========")

# Demonstrating Collision Handling
collision_table = HashTable(capacity=10)

# Finding Two SKUs that Produce the Same Hash Index
candidate_skus = [f"SKU-{number:03d}" for number in range(100)]

collision_pair = None
occupied_indices = {}

for sku in candidate_skus:
    index = collision_table._HashTable__hash_function(sku)

    if index in occupied_indices:
        collision_pair = (occupied_indices[index], sku)
        break

    occupied_indices[index] = sku

# Inserting Colliding SKUs
if collision_pair is not None:
    first_sku, second_sku = collision_pair

    collision_table.insert(first_sku, "Wireless Headphones")
    collision_table.insert(second_sku, "Bluetooth Speaker")

    print("Collision Demonstration:")
    print("SKU 1:", first_sku)
    print("SKU 2:", second_sku)
    print("Both SKUs are stored in the same bucket using chaining.")
    print("SKU 1 Search:", collision_table.search(first_sku))
    print("SKU 2 Search:", collision_table.search(second_sku))


# Generating 100,000 SKUs
sku_count = 100000

sku_data = {
    f"SKU-{number:06d}": f"Product-{number:06d}"
    for number in range(sku_count)
}

# Creating Custom Hash Table
custom_hash_table = HashTable()

for sku, product in sku_data.items():
    custom_hash_table.insert(sku, product)

# Creating Built-in Hash Map
built_in_hash_map = dict(sku_data)

# Preparing Lookup Keys
lookup_keys = [
    f"SKU-{number:06d}"
    for number in range(99000, 100000)
]

# Benchmarking Custom Hash Table
start_time = time()

for _ in range(20):
    for sku in lookup_keys:
        custom_hash_table.search(sku)

custom_time = time() - start_time

# Benchmarking Built-in Hash Map
start_time = time()

for _ in range(20):
    for sku in lookup_keys:
        built_in_hash_map.get(sku)

built_in_time = time() - start_time

print("\nLookup Performance Comparison:")
print("Total SKUs       :", sku_count)
print("Total Lookups    :", len(lookup_keys) * 20)
print(f"Custom Hash Table: {custom_time:.6f} seconds")
print(f"Built-in Hash Map: {built_in_time:.6f} seconds")


# ============================================================
# TASK 3 - GRAPH AND DEPLOYMENT DEPENDENCIES
# ============================================================

# Graph Representation
# Each service maps to the services it depends on.
dependencies = {
    "cart": ["pricing"],
    "pricing": ["inventory"],
    "inventory": ["warehouse"],
    "warehouse": [],
    "payment": ["pricing"],
    "notification": ["payment"]
}


# Converting Dependencies into Prerequisite-to-Service Edges
def build_deployment_graph(graph: dict) -> dict:
    deployment_graph = {service: [] for service in graph}

    for service, required_services in graph.items():
        for dependency in required_services:
            deployment_graph[dependency].append(service)

    return deployment_graph


# BFS Topological Sorting using Kahn's Algorithm
def bfs_deployment_order(graph: dict) -> list[str] | None:
    indegree = {service: 0 for service in graph}

    for service in graph:
        for dependent in graph[service]:
            indegree[dependent] += 1

    queue = deque(
        service for service in graph
        if indegree[service] == 0
    )

    order = []

    while queue:
        current = queue.popleft()
        order.append(current)

        for dependent in graph[current]:
            indegree[dependent] -= 1

            if indegree[dependent] == 0:
                queue.append(dependent)

    if len(order) != len(graph):
        return None

    return order


# DFS Topological Sorting
def dfs_deployment_order(graph: dict) -> list[str] | None:
    visited = set()
    recursion_stack = set()
    order = []

    def dfs(service: str) -> bool:
        visited.add(service)
        recursion_stack.add(service)

        for dependent in graph[service]:
            if dependent not in visited:
                if not dfs(dependent):
                    return False

            elif dependent in recursion_stack:
                return False

        recursion_stack.remove(service)
        order.append(service)

        return True

    for service in graph:
        if service not in visited:
            if not dfs(service):
                return None

    return order[::-1]


print("\n========== TASK 3: GRAPH AND DEPENDENCIES ==========")

deployment_graph = build_deployment_graph(dependencies)

print("Deployment Graph:", deployment_graph)

bfs_order = bfs_deployment_order(deployment_graph)
dfs_order = dfs_deployment_order(deployment_graph)

print("\nBFS Deployment Order :", bfs_order)
print("DFS Deployment Order :", dfs_order)


# Detecting Circular Dependency
cyclic_dependencies = {
    "cart": ["pricing"],
    "pricing": ["inventory"],
    "inventory": ["cart"]
}

cyclic_graph = build_deployment_graph(cyclic_dependencies)

print("\nCircular Dependency Test:")
print("BFS Result:", bfs_deployment_order(cyclic_graph))
print("DFS Result:", dfs_deployment_order(cyclic_graph))

if bfs_deployment_order(cyclic_graph) is None:
    print("Circular dependency detected!")


# ============================================================
# TASK 4 - SLIDING WINDOW
# ============================================================

# Requests per Minute for 24 Hours
requests_per_minute = [
    120, 135, 110, 150, 180, 200,
    220, 250, 300, 280, 260, 240,
    230, 210, 190, 170, 160, 180,
    220, 270, 310, 330, 290, 250
]


# Find Busiest Continuous 3-Hour Window
def busiest_window(requests: list[int], window_size: int = 3) -> tuple:
    if not requests or window_size <= 0 or window_size > len(requests):
        return None

    # Calculate Initial Window Sum
    current_sum = sum(requests[:window_size])
    maximum_sum = current_sum
    maximum_start = 0

    # Slide the Window
    for index in range(window_size, len(requests)):
        current_sum += requests[index]
        current_sum -= requests[index - window_size]

        if current_sum > maximum_sum:
            maximum_sum = current_sum
            maximum_start = index - window_size + 1

    return (
        maximum_start,
        maximum_start + window_size - 1,
        maximum_sum
    )


print("\n========== TASK 4: SLIDING WINDOW ==========")

result = busiest_window(requests_per_minute)

if result is not None:
    start_hour, end_hour, total_requests = result

    print("Busiest 3-Hour Window:")
    print(f"Start Hour     : {start_hour}:00")
    print(f"End Hour       : {end_hour + 1}:00")
    print("Total Requests :", total_requests)


# Edge Case
print("Empty Input Test:", busiest_window([]))


# ============================================================
# TASK 5 - TWO POINTERS
# ============================================================

# Sorted Order Values
order_values = [
    100, 150, 200, 250, 300,
    350, 400, 450, 500, 550
]

gift_card_value = 600


# Find All Pairs Matching the Gift Card Value
def find_gift_card_pairs(values: list[int], target: int) -> list[tuple]:
    left = 0
    right = len(values) - 1

    pairs = []

    while left < right:
        current_sum = values[left] + values[right]

        if current_sum == target:
            pairs.append((values[left], values[right]))

            left += 1
            right -= 1

        elif current_sum < target:
            left += 1

        else:
            right -= 1

    return pairs


print("\n========== TASK 5: TWO POINTERS ==========")

pairs = find_gift_card_pairs(order_values, gift_card_value)

print("Order Values     :", order_values)
print("Gift Card Value  :", gift_card_value)
print("Matching Pairs   :", pairs)


# Edge Case
print("Empty Input Test :", find_gift_card_pairs([], gift_card_value))