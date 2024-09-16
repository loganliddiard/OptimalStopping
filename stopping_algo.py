import random
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

# Function to find optimal stopping point and calculate the net reward
def run_optimal_stop(distribution):
    len_candidates = 100
    solution_found_count = {}
    optimal_solution_count = {}
    net_rewards = []
    for i in range(1, len_candidates):
        solution_found_count[str(i)] = 0
        optimal_solution_count[str(i)] = 0

    for experiment in range(1000):
        # Generate candidates based on the distribution
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
                        # Calculate net reward
                        optimal_solution_count[str(i)] += candidate - i  
                        # Store net reward
                        net_rewards.append(optimal_candidate - i) 
                    break

    return optimal_solution_count, net_rewards

def convert_index_to_percentage(index, len_candidates):
    return (index / len_candidates) * 100

def plot_optimal_stopping_and_net_rewards(distribution):
    len_candidates = 100

    # Get the results from the optimal stopping function
    optimal_solution_count, net_rewards = run_optimal_stop(distribution)

    # Plot optimal stopping points with x-axis as percentage of candidates seen
    x, y = zip(*optimal_solution_count.items())
    x_percentage = []

    for i in x:
        i = int(i)
        percentage = (i / len_candidates) * 100
        x_percentage.append(percentage)

    # Plot for optimal stopping points
    plt.figure(figsize=(10, 6))
    sns.histplot(y, kde=True, label=f'{distribution.capitalize()} Distribution')
    plt.title(f'{distribution.capitalize()} Dist. Optimal Stopping Points')
    plt.xlabel('Frequency of Optimal Candidate')
    plt.ylabel('Count')
    plt.legend()
    plt.tight_layout()
    plt.savefig(f"{distribution}_optimal_stopping_plot.png")
    plt.clf()

    # Plot for net rewards
    plt.figure(figsize=(10, 6))
    sns.histplot(net_rewards, bins=20, kde=True, label=f'{distribution.capitalize()} Net Rewards', color='green' if distribution == 'normal' else 'blue')
    plt.title(f'{distribution.capitalize()} Dist. Net Reward Distribution')
    plt.xlabel('Net Reward')
    plt.ylabel('Frequency')
    plt.legend()
    plt.tight_layout()
    plt.savefig(f"{distribution}_net_rewards_plot.png")
    plt.clf()

plot_optimal_stopping_and_net_rewards("uniform")
plot_optimal_stopping_and_net_rewards("normal")