def minimax(node, depth, isMax, tree, path=""):
    if depth == 0:
        print("Visited leaf:", node)
        return node

    if isMax:
        best = -1000
        for child in tree[node]:
            val = minimax(child, depth - 1, False, tree)
            best = max(best, val)
        print("Max node", node, "=", best)
        return best
    else:
        best = 1000
        for child in tree[node]:
            val = minimax(child, depth - 1, True, tree)
            best = min(best, val)
        print("Min node", node, "=", best)
        return best

tree = {
    "Root": ["N1", "N2"],
    "N1": ["N3", "N4"],
    "N2": ["N5", "N6"],
    "N3": [4, 7],
    "N4": [2, 5],
    "N5": [1, 8],
    "N6": [3, 6]
}

result = minimax("Root", 3, True, tree)
print("Final Result:", result)
