# Multicriteria Optimization and Decision Analysis (MODA) course - Bicycle Routing problem



## Overview

This repository contains the code, dataset and report for Assignment 2 of the MODA course. The project's main goal is to **minimise distance** while **maximising comfort** by solving a multi-objective bicycle routing problem. Comfort is determined by factors including slope, safety, roughness, and scenic beauty.

The optimization was performed using Python and the **DESDEO** library. Pareto fronts were used to analyze trade-offs between distance and comfort.

**Authors**:  
Myriana Miltiadous (s3699463)  
Katerina Zacharia (s3783049)  

## Files

 - **create_dataset.py :**	Script that generates the adjacency matrix, factor matrices (beauty, safety, etc.), and computes all valid paths from node 0 to node 19. Outputs a CSV file.
 - **moda_assignment2_code.ipynb :**	Main notebook where the optimization is performed using DESDEO and Pareto front visualized using pygmo.
 - **output.csv :**	Generated dataset containing: paths, sum of each comfort factor, and total distance for 126 valid routes.
 - **report.pdf :** Report explaining the problem setup, approach, and results in detail.


## How to Run

1. Generate the dataset:
```bash
python create_dataset.py
```
2. Open the Jupyter Notebook: moda_assignment2_code.ipynb
3. Run all cells to visualize the Pareto fronts and compare NSGA-III results with the original dataset.


## Notes

 - The data represents valid paths from node 0 to node 19 in a 20-node network.
 - Only paths of length 7 to 10 nodes are considered.
 - Optimization is subject to constraints on comfort score and distance.

For full explanation and results, refer to the `report.pdf`.
