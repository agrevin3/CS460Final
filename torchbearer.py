"""
CS 460 – Algorithms: Final Programming Assignment
The Torchbearer

Student Name: Amelia Grevin
Student ID:   827571622

INSTRUCTIONS
------------
- Implement every function marked TODO.
- Do not change any function signature.
- Do not remove or rename required functions.
- You may add helper functions.
- Variable names in your code must match what you define in README Part 5a.
- The pruning safety comment inside _explore() is graded. Do not skip it.

Submit this file as: torchbearer.py
"""

import heapq


# =============================================================================
# PART 1
# =============================================================================

def explain_problem():
    """
    Returns
    -------
    str
        Your Part 1 README answers, written as a string.
        Must match what you wrote in README Part 1.

    TODO
    """
    return "*The single shortest-path method is usually a single greedy algorithm, which doesn't always work in cases like this. This is because we can't decide the shortest path without considering future path combinations and comparing the shortest results. /n *We need to choose what path to take with the shortest path/min cost total. \n*This requires a search to find the best, most optimal path. Other methods, such as greedy, will likely only find one path, but it isn't compared to the other, possibly more minimal, solutions."


# =============================================================================
# PART 2
# =============================================================================

def select_sources(spawn, relics, exit_node):
    """
    Parameters
    ----------
    spawn : node
    relics : list[node]
    exit_node : node

    Returns
    -------
    list[node]
        No duplicates. Order does not matter.

    TODO
    """
    #Create a list to hold all the source nodes
    sourceNodes = []
    #the for loop should iterate through the length of the relics list +2, so it includes start and end nodes
    for i in range(len(relics)+2):
        #This should append the start node
        if(i == 0):
            sourceNodes.append(spawn)
        #This should append the end node
        elif(i==len(relics)+1):
            sourceNodes.append(exit_node)
        #The rest of the list should be filled with the relic list nodes
        else:
            sourceNodes.append(relics[i-1])
    #Return it as a set so there are no dupes
    return list(set(sourceNodes))


def run_dijkstra(graph, source):
    """
    Parameters
    ----------
    graph : dict[node, list[tuple[node, int]]]
        graph[u] = [(v, cost), ...]. All costs are nonnegative integers.
    source : node

    Returns
    -------
    dict[node, float]
        Minimum cost from source to every node in graph.
        Unreachable nodes map to float('inf').

    TODO
    """
    #Code framed after the canvas graphs practice quiz example!
    #Node dist should store all the node values and their distance from the start source
    nodeDist = {}
    #This should initialize all their costs at "infinity"
    for i in graph:
        nodeDist[i] = 999999
    #Source cost should be 0 b/c it is at a distance 0 to itself
    nodeDist[source] = 0
    cost =0
    #The priotity queue should store the cost value and the source compared 
    pq = [(cost,source)]
    #This while loop should work until the pq is empty
    while(len(pq)!=0):
        shortestVal =0
        #This loop finds the smallest cost up to the current index
        for i in range(len(pq)):
            if(pq[i][0]<pq[shortestVal][0]):
                shortestVal=i
        #pop the shortest cost node!
        (curr, u) = pq.pop(shortestVal)
        #Check if the current shortest dist is greater than the dist to node u(the acc current node)
        if((curr)>nodeDist[u]):
            continue
        #The loop should check all nearby nodes and see if there is a cheaper known choice
        for i in range(len(graph[u])):
            v = graph[u][i][0]
            w = graph[u][i][1]
            #Here we can update the pq with a shorter path if one is found
            if(nodeDist[u]+w<nodeDist[v]):
                nodeDist[v] = nodeDist[u]+w
                pq.append((nodeDist[v],v))
    return nodeDist


def precompute_distances(graph, spawn, relics, exit_node):
    """
    Parameters
    ----------
    graph : dict[node, list[tuple[node, int]]]
    spawn : node
    relics : list[node]
    exit_node : node

    Returns
    -------
    dict[node, dict[node, float]]
        Nested structure supporting dist_table[u][v] lookups
        for every source u your design requires.

    TODO
    """
    #Create another dict to hold the costs starting at each source node
    distFromEach = {}
    #Take them from the select source function
    everySourceNode = select_sources(spawn, relics, exit_node)
    #For loop should run dijkstras at each source node
    for i in everySourceNode:
        distFromEach[i] = run_dijkstra(graph,i)
    return distFromEach


# =============================================================================
# PART 3
# =============================================================================

def dijkstra_invariant_check():
    """
    Returns
    -------
    str
        Your Part 3 README answers, written as a string.
        Must match what you wrote in README Part 3.

    TODO
    """
    return "*The invarient here is that the minimum path for this iteration of the active source node to the end node is found. \n *Nodes that arent yet finalized should hold the minumum path cost so far, if not iterated though it should hold infinity. \n *This is because the cost from the source node is always 0. We initialize nodeDist[source] = 0. \n *The minimum cost/distance node is always correct because it is already compared to all possible options and selected as the shortest path/min cost. \n *Each source node should contain a min cost value/shortest path. *We need to make sure invarients remain true so that the route selected also results in the minimum possible cost/shortest path."


# =============================================================================
# PART 4
# =============================================================================

def explain_search():
    """
    Returns
    -------
    str
        Your Part 4 README answers, written as a string.
        Must match what you wrote in README Part 4.

    TODO
    """
    return "TODO"


# =============================================================================
# PARTS 5 + 6
# =============================================================================

def find_optimal_route(dist_table, spawn, relics, exit_node):
    """
    Parameters
    ----------
    dist_table : dict[node, dict[node, float]]
        Output of precompute_distances.
    spawn : node
    relics : list[node]
        Every node in this list must be visited at least once.
    exit_node : node
        The route must end here.

    Returns
    -------
    tuple[float, list[node]]
        (minimum_fuel_cost, ordered_relic_list)
        Returns (float('inf'), []) if no valid route exists.

    TODO
    """
    pass


def _explore(dist_table, current_loc, relics_remaining, relics_visited_order,
             cost_so_far, exit_node, best):
    """
    Recursive helper for find_optimal_route.

    Parameters
    ----------
    dist_table : dict[node, dict[node, float]]
    current_loc : node
    relics_remaining : collection
        Your chosen data structure from README Part 5b.
    relics_visited_order : list[node]
    cost_so_far : float
    exit_node : node
    best : list
        Mutable container for the best solution found so far.

    Returns
    -------
    None
        Updates best in place.

    TODO
    Implement: base case, pruning, recursive case, backtracking.

    REQUIRED: Add a 1-2 sentence comment near your pruning condition
    explaining why it is safe (cannot skip the optimal solution).
    This comment is graded.
    """
    pass


# =============================================================================
# PIPELINE
# =============================================================================

def solve(graph, spawn, relics, exit_node):
    """
    Parameters
    ----------
    graph : dict[node, list[tuple[node, int]]]
    spawn : node
    relics : list[node]
    exit_node : node

    Returns
    -------
    tuple[float, list[node]]
        (minimum_fuel_cost, ordered_relic_list)
        Returns (float('inf'), []) if no valid route exists.

    TODO
    """
    pass


# =============================================================================
# PROVIDED TESTS (do not modify)
# Graders will run additional tests beyond these.
# =============================================================================

def _run_tests():
    print("Running provided tests...")
    """
    # Test 1: Spec illustration. Optimal cost = 4.
    graph_1 = {
        'S': [('B', 1), ('C', 2), ('D', 2)],
        'B': [('D', 1), ('T', 1)],
        'C': [('B', 1), ('T', 1)],
        'D': [('B', 1), ('C', 1)],
        'T': []
    }
    cost, order = solve(graph_1, 'S', ['B', 'C', 'D'], 'T')
    assert cost == 4, f"Test 1 FAILED: expected 4, got {cost}"
    print(f"  Test 1 passed  cost={cost}  order={order}")

    # Test 2: Single relic. Optimal cost = 5.
    graph_2 = {
        'S': [('R', 3)],
        'R': [('T', 2)],
        'T': []
    }
    cost, order = solve(graph_2, 'S', ['R'], 'T')
    assert cost == 5, f"Test 2 FAILED: expected 5, got {cost}"
    print(f"  Test 2 passed  cost={cost}  order={order}")

    
    # Test 3: No valid path to exit. Must return (inf, []).
    graph_3 = {
        'S': [('R', 1)],
        'R': [],
        'T': []
    }
    cost, order = solve(graph_3, 'S', ['R'], 'T')
    assert cost == float('inf'), f"Test 3 FAILED: expected inf, got {cost}"
    print(f"  Test 3 passed  cost={cost}")

    # Test 4: Relics reachable only through intermediate rooms.
    # Optimal cost = 6.
    graph_4 = {
        'S': [('X', 1)],
        'X': [('R1', 2), ('R2', 5)],
        'R1': [('Y', 1)],
        'Y': [('R2', 1)],
        'R2': [('T', 1)],
        'T': []
    }
    cost, order = solve(graph_4, 'S', ['R1', 'R2'], 'T')
    assert cost == 6, f"Test 4 FAILED: expected 6, got {cost}"
    print(f"  Test 4 passed  cost={cost}  order={order}")

    # Test 5: Explanation functions must return non-placeholder strings.
    for fn in [explain_problem, dijkstra_invariant_check, explain_search]:
        result = fn()
        assert isinstance(result, str) and result != "TODO" and len(result) > 20, \
            f"Test 5 FAILED: {fn.__name__} returned placeholder or empty string"
    print("  Test 5 passed  explanation functions are non-empty")

    print("\nAll provided tests passed.")
    """


if __name__ == "__main__":
    print(select_sources('S',['B','C','D'],'T'))
    graph = {
        'S': [('B', 1), ('C', 2), ('D', 2)],
        'B': [('D', 1), ('T', 1)],
        'C': [('B', 1), ('T', 1)],
        'D': [('B', 1), ('C', 1)],
        'T': []
    }
    print(run_dijkstra(graph, 'S'))
    print(precompute_distances(graph, 'S', ['B', 'C', 'D'], 'T'))
    _run_tests()
