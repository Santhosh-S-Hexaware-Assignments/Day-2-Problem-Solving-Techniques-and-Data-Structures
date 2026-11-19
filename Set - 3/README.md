# Set 3 – Logistics Network and Delivery Windows

## Algorithm Decision Table

| Problem | Data Structure / Algorithm | Reason |
|---|---|---|
| Hub Code Management | Binary Search Tree (BST) | Supports insertion, searching, and ordered traversal of hub codes. |
| Duplicate Parcel Scans | Hash Map | Provides efficient lookup using tracking number and hub as a composite key. |
| Hub-to-Hub Routing | Graph (BFS / DFS) | BFS finds the route with the fewest hops, while DFS identifies reachable hubs. |
| Peak Delivery Window | Sliding Window | Finds the highest average across consecutive 4-hour windows efficiently. |
| Palindrome Route Check | Two Pointers | Compares hub codes from both ends without creating a reversed copy. |

## Graph Adjacency List

The following directed graph represents the 10 hubs and their direct routes:

```text
HUB-01 -> HUB-02, HUB-03
HUB-02 -> HUB-04, HUB-05
HUB-03 -> HUB-05, HUB-06
HUB-04 -> HUB-07
HUB-05 -> HUB-04, HUB-07, HUB-08
HUB-06 -> HUB-08
HUB-07 -> HUB-09
HUB-08 -> HUB-07, HUB-09, HUB-10
HUB-09 -> HUB-10
HUB-10 -> None
```

Routes are treated as directed: a listed connection can be followed in the listed direction.