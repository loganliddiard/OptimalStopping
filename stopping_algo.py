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

    total_weighted_values = sum(int(x[i]) * y[i] for i in range(len(x)))
    total_frequencies = sum(y)
    average_best_threshold = total_weighted_values / total_frequencies

    # Print the average best threshold
    print(f"Average best threshold (as percentage) for {distribution}: {average_best_threshold:.2f}%")

    
    # Plot for optimal stopping points
    plt.figure(figsize=(10, 6))
    sns.histplot(x=x_percentage, weights=[max(0, weight) for weight in y], bins=20, kde=True, label=f'{distribution.capitalize()} Distribution', color='green' if distribution == 'normal' else 'blue')

    plt.title(f'Optimal Stopping for {distribution.capitalize()} Distribution')
    plt.xlabel('Percentage of Candidates Seen')
    plt.ylabel('Frequency of Optimal Candidate')
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