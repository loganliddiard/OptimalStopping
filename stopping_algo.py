import random
import matplotlib.pyplot as plt
import numpy as np
def run_optimal_stop(distribution):
    len_candidates = 100
    solution_found_count = {}
    optimal_solution_found_count = {}
    for i in range(1, len_candidates):
        solution_found_count[str(i)] = 0
        optimal_solution_found_count[str(i)] = 0

    for experiment in range(1000):
        candidates = []
        match distribution:
            case "uniform":
                candidates = np.random.uniform(1, 99, len_candidates)
            case "normal":
                candidates = np.random.normal(50, 10, len_candidates)
                candidates = np.clip(candidates, 0, 99)
        optimal_candidate = max(candidates)

        for i in range(1, len_candidates):
            for candidate in candidates[i:-1]:
                if candidate > max(candidates[0:i]):
                    solution_found_count[str(i)] += 1
                    if candidate == optimal_candidate:
                        optimal_solution_found_count[str(i)] += candidate-i
                    break
    return optimal_solution_found_count

# print(run_optimal_stop().items())
x,y = zip(*run_optimal_stop("uniform").items())

plt.plot(x,y)
plt.show()
x,y = zip(*run_optimal_stop("normal").items())

plt.plot(x,y)
plt.show()

