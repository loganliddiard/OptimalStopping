# OptimalStopping

## Team Members:
* Kaden Hart
* Logan Liddiard
* Joel Pierson
* Ben Tomlinson

## Project Overview

This project focuses on applying the Optimal Stopping Problem across different scenarios. There were three main parts:
1. Determining the General Optimum
2. Exploring Alternative Distributions
3. Maximizing Benefit in Investment Decisions

## Requirements:

* Python 3.x
* Required packages: `numpy`, `scipy`, `matplotlib`, `seaborn`
These can be installed by running:
```
pip install numpy scipy matplotlib seaborn
```

## How to run:

The main python file for submission is `HW1_Lastname_Firstname.py` which accepts an argument to control the size of the test (`small` or `large`).

* `small` runs a quick version of the tests with only two iterations.
* `large` runs a longer version of the tests with 50 iterations.

### For example:
```
python HW1_Lastname_Firstname.py small
```
or
```
python HW1_Lastname_Firstname.py large
```

The program wilil execute the algorithm on various distributions and generate results based on the selected mode. For **large** mode, it will also generate graphs comparing the results for different strategies and save them as PNG files in the current directory.

## Analysis of the Results:

### Part 1: General Optimum

Upon testing this algorithm rigorously, we have determined that the optimal stopping point is closer to 37% for this optimal stopping problem.

### Part 2: Alternative Distributions

Interestingly enough after running about 50,000 experiments and taking the best outcome of each 1000, we graphed a distribution plot for each of the distributions

Ironically they were all close to .37% with slight variances for each. The following is the results of these three serparate runs of these experiments:

    - Beta Dist. 37.68%
    - Normal Dist. 36.36%
    - Uniform Dist. 37.68%

To save the the hastle of rerunning our larger experiment the graphs for each are provided and labeled below as so:

<p align="center">
  <img src="Test_beta_optimal_stopping_plot.png" alt="roadmap">
</p>
<p align="center">
  <img src="Test_normal_optimal_stopping_plot.png" alt="roadmap">
</p>
<p align="center">
  <img src="Test_uniform_optimal_stopping_plot.png" alt="roadmap">
</p>


### Part 3: Investment Strategy


## Conclusion

