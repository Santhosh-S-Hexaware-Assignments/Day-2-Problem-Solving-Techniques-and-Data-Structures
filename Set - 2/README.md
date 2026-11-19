# Set 2 – Insurance Claims Processing

## Complexity Table

| Problem | Technique | Time Complexity | Space Complexity |
|:---|:---|:---|:---|
| Claim ID Management | Binary Search Tree (BST) | Average: O(log n), Worst: O(n); Traversal: O(n) | O(n) |
| Duplicate Claim Detection | Hashing / Hash Map | Average: O(n), Worst: O(n²) | O(n) |
| Claim Approval Routing | Graph (BFS / DFS) | BFS: O(V + E) for traversal, O(V²) worst-case with path copying; DFS: O(V + E) | O(V + E) |
| Claim Spike Detection | Sliding Window | O(n) | O(1) |
| Merging Regional Claim Lists | Two Pointers | O(n + m) | O(n + m) |

**Where:**
- `n` = Number of elements or claims.
- `m` = Number of elements in the second sorted list.
- `V` = Number of graph vertices (approval stages).
- `E` = Number of graph edges (stage connections).

**Note:** Hash map complexities are based on average-case and worst-case behaviour. The BST assumes no self-balancing mechanism.