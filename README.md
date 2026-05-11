# The Torchbearer

**Student Name:** Amelia Grevin
**Student ID:** 827571622
**Course:** CS 460 – Algorithms | Spring 2026

> This README is your project documentation. Write it the way a developer would document
> their design decisions , bullet points, brief justifications, and concrete examples where
> required. You are not writing an essay. You are explaining what you built and why you built
> it that way. Delete all blockquotes like this one before submitting.

---

## Part 1: Problem Analysis

> Document why this problem is not just a shortest-path problem. Three bullet points, one
> per question. Each bullet should be 1-2 sentences max

- **Why a single shortest-path run from S is not enough:**
  *The single shortest-path method is usually a single greedy algorithm, which doesn't always work in cases like this. This is because we can't decide the shortest path without considering future path combinations and comparing the shortest results.

- **What decision remains after all inter-location costs are known:**
  *We need to choose what path to take with the shortest path/min cost total.

- **Why this requires a search over orders (one sentence):**
  *This requires a search to find the best, most optimal path. Other methods, such as greedy, will likely only find one path, but it isn't compared to the other, possibly more minimal, solutions.

---

## Part 2: Precomputation Design

### Part 2a: Source Selection

> List the source node types as a bullet list. For each, one-line reason.

| Source Node Type | Why it is a source |
|---|---|
| Start node | The start node acts as the source for each iteration to all the other nodes|
| relic in set M | May need to know the shortest path from a relic to the end(following each other node) |
| End node | I added the end node later on because I included it in the source selection function in the case that it is the only node in the set|

### Part 2b: Distance Storage

> Fill in the table. No prose required.

| Property | Your answer |
|---|---|
| Data structure name |priority queue/dictionary|
| What the keys represent |the keys are the S, R, and T values, meaning the start, end, and all relic nodes|
| What the values represent |The values represent the cost from a start node to the current node(or chamber)|
| Lookup time complexity |O(1)|
| Why O(1) lookup is possible |This complexity is possible because of the dictionary layout, you can directly look up values|

### Part 2c: Precomputation Complexity

> State the total complexity and show the arithmetic. Two to three lines max.

- **Number of Dijkstra runs:** number of relic chambers + start node+ end node
- **Cost per run:** m log n
- **Total complexity:** (M+2)(m log n)
- **Justification (one line):** M+2 represents the set of relic chambers + the starting and ending node and m log n is the cost of a single min cost run

---

## Part 3: Algorithm Correctness

> Document your understanding of why Dijkstra produces correct distances.
> Bullet points and short sentences throughout. No paragraphs.

### Part 3a: What the Invariant Means

> Two bullets: one for finalized nodes, one for non-finalized nodes.
> Do not copy the invariant text from the spec.

- **For nodes already finalized (in S):**
  The invarient here is that the minimum path for this iteration of the active source node to the end node is found.

- **For nodes not yet finalized (not in S):**
  Nodes that arent yet finalized should hold the minumum path cost so far, if not iterated though it should hold infinity.

### Part 3b: Why Each Phase Holds

> One to two bullets per phase. Maintenance must mention nonnegative edge weights.

- **Initialization : why the invariant holds before iteration 1:**
  This is because the cost from the source node is always 0. We initialize nodeDist[source] = 0.

- **Maintenance : why finalizing the min-dist node is always correct:**
  The minimum cost/distance node is always correct because it is already compared to all possible options and selected as the shortest path/min cost.

- **Termination : what the invariant guarantees when the algorithm ends:**
  Each source node should contain a min cost value/shortest path.

### Part 3c: Why This Matters for the Route Planner

> One sentence connecting correct distances to correct routing decisions.

We need to make sure invarients remain true so that the route selected also results in the minimum possible cost/shortest path.

---

## Part 4: Search Design

### Why Greedy Fails

> State the failure mode. Then give a concrete counter-example using specific node names
> or costs (you may use the illustration example from the spec). Three to five bullets.

- **The failure mode:** _Your answer here._
- **Counter-example setup:** _Your answer here._
- **What greedy picks:** _Your answer here._
- **What optimal picks:** _Your answer here._
- **Why greedy loses:** _Your answer here._

### What the Algorithm Must Explore

> One bullet. Must use the word "order."

- _Your answer here._

---

## Part 5: State and Search Space

### Part 5a: State Representation

> Document the three components of your search state as a table.
> Variable names here must match exactly what you use in torchbearer.py.

| Component | Variable name in code | Data type | Description |
|---|---|---|---|
| Current location | | | |
| Relics already collected | | | |
| Fuel cost so far | | | |

### Part 5b: Data Structure for Visited Relics

> Fill in the table.

| Property | Your answer |
|---|---|
| Data structure chosen | |
| Operation: check if relic already collected | Time complexity: |
| Operation: mark a relic as collected | Time complexity: |
| Operation: unmark a relic (backtrack) | Time complexity: |
| Why this structure fits | |

### Part 5c: Worst-Case Search Space

> Two bullets.

- **Worst-case number of orders considered:** _Your answer (in terms of k)._
- **Why:** _One-line justification._

---

## Part 6: Pruning

### Part 6a: Best-So-Far Tracking

> Three bullets.

- **What is tracked:** _Your answer here._
- **When it is used:** _Your answer here._
- **What it allows the algorithm to skip:** _Your answer here._

### Part 6b: Lower Bound Estimation

> Three bullets.

- **What information is available at the current state:** _Your answer here._
- **What the lower bound accounts for:** _Your answer here._
- **Why it never overestimates:** _Your answer here._

### Part 6c: Pruning Correctness

> One to two bullets. Explain why pruning is safe.

- _Your answer here._

---

## References

> Bullet list. If none beyond lecture notes, write that.

- _Your references here._
