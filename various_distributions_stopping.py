import numpy as np
import math
from scipy.stats import beta
import matplotlib.pyplot as plt
import seaborn as sns

len_candidates = 100
num_experiments = 1000

# Function to run many experiments to find the optimal stopping threshold for the given distribution.
def explore_optimal_thresholds(distribution, len_candidates, num_experiments):
    optimal_solution_found_count = {}

    for i in range(1, len_candidates):                              
        optimal_solution_found_count[str(i)] = 0

    for experiment in range(num_experiments):
        match distribution:
            case "beta":
                a = 2
                b = 7
                candidates = beta.rvs(a,b,size=len_candidates)
            case "uniform":
                candidates = np.random.uniform(1, 1000, len_candidates)     
            case "normal":
                candidates = np.random.normal(50, 10, len_candidates)  

        optimal_candidate = max(candidates)                         

        for i in range(1, len_candidates):                          
            for candidate in candidates[i:-1]:                        
                if candidate > max(candidates[0:i]):                   
                    if candidate == optimal_candidate:                      
                        optimal_solution_found_count[str(i)] += 1               
                    break                                                   

    optimal_candidate_threshold = max(zip(optimal_solution_found_count.values(), optimal_solution_found_count.keys()))[1]       #optimal candidate to stop at according to these completed experiments
    optimal_stopping_threshold = round(float(optimal_candidate_threshold) / len_candidates, 4)                                  #optimal stopping threshold as a percentage
    print(f"After running {num_experiments} experiments with a {distribution} distribution, it was optimal to stop searching through candidates and make the desision after seeing {optimal_stopping_threshold * 100}% of the candidates. In other words, it was optimal to choose a candidate after seeing {optimal_candidate_threshold} out of {len_candidates}.")

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
def run_algorithm_test(distribution,largeTest):
    test_threshold = explore_optimal_thresholds(distribution, len_candidates, num_experiments)            # 'num_experiments' tests are conducted to find an optimal stopping threshold. (We know the optimal threshold is .37 usually)

    match distribution:                                                                                   # a random group of 1000 candidates is generated with the given distribution.
            case "uniform":
                test_candidates = np.random.uniform(1, 1000, len_candidates)     
            case "normal":
                test_candidates = np.random.normal(50, 10, len_candidates)  
            case "beta":
                a = 2
                b = 7
                test_candidates = beta.rvs(a,b,size=len_candidates)
                                   
    test_optimal_candidate = max(test_candidates)                                           # the objectively optimal candidate is recorded, for comparison purposes

    test_chosen_candidate = stopping_algorithm(test_candidates, test_threshold)     # Our algorithm is run on the group and it chooses a candidate.

    if not largeTest:
        print(f"After running our algorithm on a test group of size {len_candidates} with a {distribution} distribution, using a stopping threshold of {test_threshold}, it chose a candidate with value {test_chosen_candidate}. The best candidate in the group had value {test_optimal_candidate}.")

    return test_threshold

## This value will determine if 2 smaller test of each or 
largeTest = True

small_iterations = 2
large_iterations = 50

# Run the tests using varous distributions.
if not largeTest:
    for i in range(0,small_iterations):
        print(f"\nSkewed Beta Test #{i}:")
        run_algorithm_test("beta",largeTest)

    for i in range(0,small_iterations):
        print(f"\nUniform Test #{i}:")
        run_algorithm_test("uniform",largeTest)
        print(f"\nUniform Test for Part 3 #{i}:")

    for i in range(0,small_iterations):
        print(f"\nNormal Test #{i}:")
        run_algorithm_test("normal",largeTest)
        print(f"\nNormal Test for Part 3 #{i}:")

# run larger tests across each type of distibution
else:

    beta_data = []
    for i in range(0,large_iterations):
        print(f"\nRunning Skewed Beta Test #{i}...")
        beta_data.append(run_algorithm_test("beta",largeTest))

    uniform_data = []
    for i in range(0,large_iterations):
        print(f"\nRunning Uniform Test #{i}:")
        uniform_data.append(run_algorithm_test("uniform",largeTest))
    normal_data = []
    for i in range(0,large_iterations):
        print(f"\nRunning Normal Test #{i}:")
        normal_data.append(run_algorithm_test("normal",largeTest))
    
    print("\nNow plotting graphs...")

    ##plotting beta data
    sns.histplot(beta_data, kde=True)

    average = np.mean(beta_data)

    plt.title(f"Beta Dist. Optimal Stopping Points with an average of {average}")
    plt.savefig('beta_optimal_stopping_plot.png')
    plt.clf()
    

    ##plotting uniform data
    sns.histplot(uniform_data, kde=True)

    average = np.mean(uniform_data)

    plt.title(f"Uniform Dist. Optimal Stopping Points with an average of {average}")
    plt.savefig('uniform_optimal_stopping_plot.png')
    plt.clf()

    ##plotting normal data
    sns.histplot(normal_data, kde=True)

    average = np.mean(normal_data)

    plt.title(f"Normal Dist. Optimal Stopping Points with an average of {average}")
    plt.savefig('normal_optimal_stopping_plot.png')
    plt.clf()

    print("\Done!")
    

