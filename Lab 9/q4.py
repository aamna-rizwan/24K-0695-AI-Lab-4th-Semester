#task 4 
import numpy as np
states = ["Sunny", "Cloudy", "Rainy"]

transition_matrix = np.array([
    [0.6, 0.3, 0.1],
    [0.3, 0.4, 0.3],
    [0.2, 0.3, 0.5]
])

def simulate(initial_state, steps):
    current = initial_state
    result = [current]

    for _ in range(steps):
        index = states.index(current)
        next_state = np.random.choice(states, p=transition_matrix[index])
        result.append(next_state)
        current = next_state

    return result

sequence = simulate("Sunny", 10)
print(sequence)
