#task 3 

def minimax(node, depth, isMax, tree):
    if depth == 0 or not isinstance(node, str):
        return node

    if isMax:
        best = -1000
        for child in tree[node]:
            val = minimax(child, depth-1, False, tree)
            best = max(best, val)
        return best
    else:
        best = 1000
        for child in tree[node]:
            val = minimax(child, depth-1, True, tree)
            best = min(best, val)
        return best


#modified
tree = {
    "Root": ["N1", "N2"],
    "N1": ["N3", "N4"],
    "N2": ["N5", "N6"],
    "N3": [4, 9], #n3 changed
    "N4": [2, 5],
    "N5": [1, 8],
    "N6": [3, 6]
}

result = minimax("Root", 3, True, tree)
print("Updated Minimax Result:", result)

print("Optimal Path: Root -> N2 -> N6 -> 6")

#the optimal path may change based on the values 
