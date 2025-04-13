# Multicriteria Optimization and Decision Analysis (MODA) course - Bicycle Routing problem



## Overview

This repository contains the code, dataset and report for Assignment 2 of the MODA course. The project's main goal is to **minimise distance** while **maximising comfort** by solving a multi-objective bicycle routing problem. Comfort is determined by factors including slope, safety, roughness, and scenic beauty.

The optimization was performed using Python and the **DESDEO** library. Pareto fronts were used to analyze trade-offs between distance and comfort.

**Authors**:  
Myriana Miltiadous (s3699463)  
Katerina Zacharia (s3783049)  

## Contents

- `output.csv`: Generated dataset of valid bicycle routes with corresponding metrics.
- Python scripts: Code for generating paths, modeling the problem, and computing the Pareto front.
- `report.pdf`: **Full technical report** explaining the problem setup, approach, and results in detail.

## Usage

1. Clone this repository.
2. Install required libraries:
```bash
pip install pandas matplotlib desdeo pygmo
 ```

## Notes

- The data represents valid paths from node 0 to node 19 in a 20-node network.
- Only paths of length 7 to 10 nodes are considered.
- Optimization is subject to constraints on comfort score and distance.

For full explanation and results, refer to the `report.pdf`.
