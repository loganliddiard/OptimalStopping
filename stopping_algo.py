import random
import matplotlib.pyplot as plt
def run_optimal_stop(len_candidates, experiments):
    # len_candidates = 100
    solution_found_count = {}
    optimal_solution_found_count = {}
    for i in range(1, len_candidates):
        solution_found_count[str(i)] = 0
        optimal_solution_found_count[str(i*(100/len_candidates))] = 0



    for experiment in range(experiments):
        candidates = random.sample(range(0,experiments), len_candidates)
        optimal_candidate = max(candidates)

        for i in range(1, len_candidates):
            for candidate in candidates[i:-1]:
                if candidate > max(candidates[0:i]):
                    solution_found_count[str(i)] += 1
                    if candidate == optimal_candidate:
                        optimal_solution_found_count[str(i*(100/len_candidates))] += 1
                    break
    return optimal_solution_found_count


bestRuns = {}
for i in range (1,6):
    optimal_count = run_optimal_stop(i*20,i*200)
    maxStopCount = 0
    bestStop = 0
    for x,y in optimal_count.items():
        # print(y)
        if y>maxStopCount:
            maxStopCount = y
            bestStop = x
    if bestStop == "0":
        print(i)
        print(optimal_count)
    if bestStop not in bestRuns.keys():
        bestRuns[bestStop] = {"count":1,"indexes":[i]}
    else:
        bestRuns[bestStop]["count"] += 1
        bestRuns[bestStop]["indexes"].append(i)
    x, y = zip(*optimal_count.items())
    plt.plot(x,y)
    plt.show()
print(bestRuns)

# plt.plot(x,y)
# plt.show()

