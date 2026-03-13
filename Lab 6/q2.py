goal = 20
beam_width = 2

def h(n):
    return abs(goal - n)

beam = [(1, [1])]
level = 0
while beam:
    print("\nLevel", level)
    next_states = []

    for state, path in beam:
        print("Exploring:", state)
        if state == goal:
            print("\nGoal reached!")
            print("Path:", path)
            exit()

      
        neighbors = [state+2, state+3, state*2]
        for n in neighbors:
            if n <= 50:  
                next_states.append((n, path + [n]))

    next_states.sort(key=lambda x: h(x[0]))
    beam = next_states[:beam_width]

    print("Selected states:", [s[0] for s in beam])

    level += 1
