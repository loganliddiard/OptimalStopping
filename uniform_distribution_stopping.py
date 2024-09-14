import numpy as np
import math

len_candidates = 100
num_experiments = 1000

# Function to run many experiments to find the optimal stopping threshold for a uniform distribution. As an infinite number of experiments are performed, the threshold would approach the 'magical' 37%.
def explore_optimal_thresholds_uniform(len_candidates, num_experiments):
    optimal_solution_found_count = {}

    for i in range(1, len_candidates):                              
        optimal_solution_found_count[str(i)] = 0

    for experiment in range(num_experiments):
        candidates = np.random.uniform(1, 1000, len_candidates)     
        optimal_candidate = max(candidates)                         

        for i in range(1, len_candidates):                          
            for candidate in candidates[i:-1]:                        
                if candidate > max(candidates[0:i]):                   
                    if candidate == optimal_candidate:                      
                        optimal_solution_found_count[str(i)] += 1               
                    break                                                   

    optimal_candidate_threshold = max(zip(optimal_solution_found_count.values(), optimal_solution_found_count.keys()))[1]       #optimal candidate to stop at according to these completed experiments
    optimal_stopping_threshold = round(float(optimal_candidate_threshold) / len_candidates, 4)                                  #optimal stopping threshold as a percentage
    print(f"After running {num_experiments} experiments, it was optimal to stop searching through candidates and make the desision after seeing {optimal_stopping_threshold * 100}% of the candidates. In other words, it was optimal to choose a candidate after seeing {optimal_candidate_threshold} out of {len_candidates}.")

    return optimal_stopping_threshold

# The stopping algorithm. It takes a group of candidates, along with a threshold at which it should begin making a decision (a percentage, expressed as a decimal between 0 and 1). Its chosen candidate is returned.
def stopping_algorithm(candidates, threshold):
    best_candidate_pre_threshold = 0

    for i in range(0, math.ceil((len(candidates)-1)*threshold)):
        if candidates[i] > best_candidate_pre_threshold:
            best_candidate_pre_threshold = candidates[i]
    for i in range(math.ceil((len(candidates)-1)*threshold), len(candidates)):
        if i == len(candidates)-1:
            return candidates[i]
        if candidates[i] > best_candidate_pre_threshold:
            return candidates[i]

# Function to run a test on our algorithm.
def run_algorithm_test_uniform():
    test_threshold = explore_optimal_thresholds_uniform(len_candidates, num_experiments)            # 'num_experiments' tests are conducted to find an optimal stopping threshold. (We know the optimal threshold is .37 in actuality)

    test_candidates = np.random.uniform(1, 1000, 1000)                                      # a random group of 1000 candidates is generated with a uniform distribution.
    test_optimal_candidate = max(test_candidates)                                           # the objectively optimal candidate is recorded, for comparison purposes

    test_chosen_candidate = stopping_algorithm(test_candidates, test_threshold)     # Our algorithm is run on the group and it chooses a candidate.

    print(f"After running our algorithm on a test group of size {len_candidates}, using a stopping threshold of {test_threshold}, it chose a candidate with value {test_chosen_candidate}. The best candidate in the group had value {test_optimal_candidate}.")



for i in range(0,2):
    print(f"\nTest #{i}:")
    run_algorithm_test_uniform()


