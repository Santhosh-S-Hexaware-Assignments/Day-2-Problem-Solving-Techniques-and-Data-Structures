from collections import deque


# ============================================================
# TASK 1 - BINARY SEARCH TREE
# ============================================================

# Node Class
class Node:
    def __init__(self, value: int) -> None:
        self.value = value
        self.left = None
        self.right = None


# Binary Search Tree Class
class BinarySearchTree:
    def __init__(self) -> None:
        self.root = None

    # Insert Function
    def insert(self, value: int) -> None:
        if self.root is None:
            self.root = Node(value)
        else:
            self.__insert(self.root, value)

    # Recursive Insert
    def __insert(self, root: Node, value: int) -> None:
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
    def search(self, value: int) -> bool:
        return self.__search(self.root, value)

    # Recursive Search
    def __search(self, root: Node | None, value: int) -> bool:
        if root is None:
            return False

        if root.value == value:
            return True

        if value < root.value:
            return self.__search(root.left, value)

        return self.__search(root.right, value)

    # Inorder Traversal
    def inorder(self) -> list[int]:
        result = []
        self.__inorder(self.root, result)
        return result

    def __inorder(self, root: Node | None, result: list[int]) -> None:
        if root is not None:
            self.__inorder(root.left, result)
            result.append(root.value)
            self.__inorder(root.right, result)

    # Preorder Traversal
    def preorder(self) -> list[int]:
        result = []
        self.__preorder(self.root, result)
        return result

    def __preorder(self, root: Node | None, result: list[int]) -> None:
        if root is not None:
            result.append(root.value)
            self.__preorder(root.left, result)
            self.__preorder(root.right, result)

    # Postorder Traversal
    def postorder(self) -> list[int]:
        result = []
        self.__postorder(self.root, result)
        return result

    def __postorder(self, root: Node | None, result: list[int]) -> None:
        if root is not None:
            self.__postorder(root.left, result)
            self.__postorder(root.right, result)
            result.append(root.value)


print("\n========== TASK 1: BINARY SEARCH TREE ==========")

# Sample Claim IDs
claim_ids = [
    1050, 1020, 1080, 1010, 1030,
    1060, 1090, 1005, 1025, 1040,
    1070, 1100, 1015, 1035, 1085
]

# Creating Binary Search Tree
claim_tree = BinarySearchTree()

for claim_id in claim_ids:
    claim_tree.insert(claim_id)

# Display Traversals
print("Inorder Traversal   :", claim_tree.inorder())
print("Preorder Traversal  :", claim_tree.preorder())
print("Postorder Traversal :", claim_tree.postorder())

# Search Test Cases
print("\nSearch Results:")
print("Claim 1050:", claim_tree.search(1050))
print("Claim 1100:", claim_tree.search(1100))
print("Claim 9999:", claim_tree.search(9999))

# Duplicate and Empty Input Tests
duplicate_tree = BinarySearchTree()
duplicate_tree.insert(1050)
duplicate_tree.insert(1050)

print("\nDuplicate Claim Test:", duplicate_tree.inorder())
print("Empty Tree Search Test:", BinarySearchTree().search(1050))


# ============================================================
# TASK 2 - HASHING AND DUPLICATE CLAIM DETECTION
# ============================================================

# Normalize Claim Details
def normalize(policy_number: str, incident_date: str) -> tuple:
    normalized_policy = "".join(
        character.upper()
        for character in policy_number
        if character.isalnum()
    )

    normalized_date = incident_date.strip()

    return normalized_policy, normalized_date


# Detect Duplicate and Near-Duplicate Claims
def detect_duplicates(claims: list[dict]) -> list[tuple]:
    claim_lookup = {}
    duplicates = []

    for claim in claims:
        claim_id = claim["ClaimID"]

        key = normalize(
            claim["PolicyNumber"],
            claim["IncidentDate"]
        )

        if key in claim_lookup:
            duplicates.append((claim_lookup[key], claim_id))
        else:
            claim_lookup[key] = claim_id

    return duplicates


print("\n========== TASK 2: HASHING ==========")

# Sample Claim Records
claims = [
    {"ClaimID": 201, "PolicyNumber": "POL-1001", "IncidentDate": "2026-10-01"},
    {"ClaimID": 202, "PolicyNumber": "pol 1002", "IncidentDate": "2026-10-02"},
    {"ClaimID": 203, "PolicyNumber": "POL 1001", "IncidentDate": "2026-10-01"},
    {"ClaimID": 204, "PolicyNumber": "POL-1003", "IncidentDate": "2026-10-03"},
    {"ClaimID": 205, "PolicyNumber": "pol-1002", "IncidentDate": "2026-10-02"},
    {"ClaimID": 206, "PolicyNumber": "POL-1004", "IncidentDate": "2026-10-04"}
]

duplicate_claims = detect_duplicates(claims)

print("Duplicate / Near-Duplicate Claim Pairs:")

for first_claim, second_claim in duplicate_claims:
    print(f"Claim {first_claim} and Claim {second_claim}")

# Empty Input Test
print("\nEmpty Input Test:", detect_duplicates([]))

# Collision Handling Explanation
print("\nHash Collision Handling:")
print("Python dictionaries handle hash collisions internally.")
print("They compare keys for equality before treating them as identical.")
print("Our normalized tuple keys identify claims with matching policy")
print("numbers and incident dates, even if their formatting differs.")


# ============================================================
# TASK 3 - GRAPH AND CLAIM APPROVAL ROUTING
# ============================================================

# Directed Graph of Claim Approval Stages
approval_graph = {
    "Registration": ["Assessment"],
    "Assessment": ["Surveyor", "Settlement"],
    "Surveyor": ["Settlement"],
    "Settlement": []
}


# BFS - Find Shortest Path
def shortest_path(graph: dict, start: str, destination: str) -> list | None:
    if start not in graph or destination not in graph:
        return None

    queue = deque([(start, [start])])
    visited = {start}

    while queue:
        current, path = queue.popleft()

        if current == destination:
            return path

        for neighbour in graph[current]:
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append((neighbour, path + [neighbour]))

    return None


# DFS - Detect Cycles
def has_cycle(graph: dict) -> bool:
    visited = set()
    recursion_stack = set()

    def dfs(stage: str) -> bool:
        visited.add(stage)
        recursion_stack.add(stage)

        for neighbour in graph[stage]:
            if neighbour not in visited:
                if dfs(neighbour):
                    return True

            elif neighbour in recursion_stack:
                return True

        recursion_stack.remove(stage)
        return False

    for stage in graph:
        if stage not in visited:
            if dfs(stage):
                return True

    return False


print("\n========== TASK 3: GRAPH ==========")

# Find Shortest Approval Route
route = shortest_path(
    approval_graph,
    "Registration",
    "Settlement"
)

print("Shortest Approval Path:", route)

# Detect Cycles
print("Circular Dependency:", has_cycle(approval_graph))

# Cyclic Graph Test
cyclic_approval_graph = {
    "Registration": ["Assessment"],
    "Assessment": ["Surveyor"],
    "Surveyor": ["Registration", "Settlement"],
    "Settlement": []
}

print("\nCircular Approval Flow Test:")
print("Cycle Detected:", has_cycle(cyclic_approval_graph))

# Empty Graph Test
print("Empty Graph Test:", has_cycle({}))


# ============================================================
# TASK 4 - SLIDING WINDOW
# ============================================================

# Daily Claim Counts
daily_claims = [
    80, 120, 135, 150, 90, 110, 125,
    140, 160, 95, 105, 115, 130, 70
]


# Find Longest Consecutive Run Above Threshold
def longest_claim_spike(claims: list[int], threshold: int = 100) -> tuple:
    left = 0
    maximum_length = 0
    best_start = -1
    best_end = -1

    for right in range(len(claims)):
        if claims[right] <= threshold:
            left = right + 1

        current_length = right - left + 1

        if current_length > maximum_length:
            maximum_length = current_length
            best_start = left
            best_end = right

    if maximum_length == 0:
        return 0, None, None

    return maximum_length, best_start, best_end


print("\n========== TASK 4: SLIDING WINDOW ==========")

result = longest_claim_spike(daily_claims)

longest_run, start_day, end_day = result

print("Daily Claim Counts:", daily_claims)
print("Longest Run Above 100 Claims:", longest_run)

if start_day is not None:
    print(f"Start Day: Day {start_day + 1}")
    print(f"End Day  : Day {end_day + 1}")

# Empty Input Test
print("\nEmpty Input Test:", longest_claim_spike([]))

# No Claims Above Threshold Test
print("No Spike Test:", longest_claim_spike([40, 70, 90, 100]))


# ============================================================
# TASK 5 - TWO POINTERS
# ============================================================

# Merge Two Sorted Claim Lists
def merge_claims(first: list[int], second: list[int]) -> list[int]:
    left = 0
    right = 0

    merged = []

    while left < len(first) and right < len(second):
        if first[left] <= second[right]:
            merged.append(first[left])
            left += 1
        else:
            merged.append(second[right])
            right += 1

    # Append Remaining Elements
    merged.extend(first[left:])
    merged.extend(second[right:])

    return merged


print("\n========== TASK 5: TWO POINTERS ==========")

# Sorted Claim Lists from Two Regional Offices
north_region_claims = [101, 105, 110, 115, 120, 130]
south_region_claims = [102, 105, 112, 118, 125, 130]

merged_claims = merge_claims(
    north_region_claims,
    south_region_claims
)

print("North Region Claims:", north_region_claims)
print("South Region Claims:", south_region_claims)
print("Merged Claim List  :", merged_claims)

# Empty Input Tests
print("\nBoth Empty:", merge_claims([], []))
print("First Empty:", merge_claims([], [101, 102, 103]))
print("Second Empty:", merge_claims([104, 105, 106], []))

# Duplicate Values Test
print("Duplicate Values:", merge_claims([101, 105], [101, 105]))