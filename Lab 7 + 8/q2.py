#task 2

def alphabeta(node, depth, alpha, beta, isMax, tree):
    if isinstance(node, int):
        return node
      
    if depth == 0:
        if node in tree: 
            if isMax:
                return max(tree[node])
            else:
                return min(tree[node])
        else:
            return node 

    if isMax:
        value = -float('inf')
        for child in tree[node]:
            val = alphabeta(child, depth-1, alpha, beta, False, tree)
            value = max(value, val)
            alpha = max(alpha, value)

            if alpha >= beta:
                print("Pruned at:", child)
                break

        print("Max node", node, "=", value)
        return value

    else:
        value = float('inf')
        for child in tree[node]:
            val = alphabeta(child, depth-1, alpha, beta, True, tree)
            value = min(value, val)
            beta = min(beta, value)

            if beta <= alpha:
                print("Pruned at:", child)
                break

        print("Min node", node, "=", value)
        return value


tree = {
    "Root": ["N1", "N2"],
    "N1": ["N3", "N4"],
    "N2": ["N5", "N6"],
    "N3": [4, 7],
    "N4": [2, 5],
    "N5": [1, 8],
    "N6": [3, 6]
}

print("Full Depth")
result = alphabeta("Root", 3, -float('inf'), float('inf'), True, tree)
print("Final Result:", result)

print("Depth = 2")
result = alphabeta("Root", 2, -float('inf'), float('inf'), True, tree)
print("Final Result:", result)



#number of nodes visited are the same as minimax because no pruning is done 
#Alpha -beta pruning avoids branches that wont effect the final decision 
#with a specific condition (aplha<=beta) it carries out prungin 
