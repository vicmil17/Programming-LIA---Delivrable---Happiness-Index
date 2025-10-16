# ================================================================
# File: LIA - HAPPINESS INDEX - CODE - VO.py
# Author: OLIVIA MARAGOS and VICTORIA MILIOTO 
# Course: Python Programming 
# Date: October 2025
#
# Description:
#  This program contains all exercises for the Lia Deliverable .
#  It will be used to analyze the dataset of the WHI using GitHub.

# ================================================================
# Part 2: Loading with your dataset
# ---------------------------------------------------------------
# THOUGHT PROCESS 
# numeric columns: Ladder, GDP, Support, LifeExp, Freedom, Generosity, Corruption
# delimiter="," → tells Python that columns are separated by commas
# skiprows=1 → skips the header line with column names
# ---------------------------------------------------------------

import numpy as np

cols = (2, 6, 7, 8, 9, 10, 11)
data = np.loadtxt("world-happiness-report-2021.csv", delimiter=",", skiprows=1, usecols = cols )

# each column seperately
ladder, gdp, support, life, freedom, generosity, corruption = data.T
print("Ladder sample:", ladder[:5])

# ================================================================
# Part 3: Manipulating your data
# ---------------------------------------------------------------

import numpy as np

# Load only 2 columns: Ladder score (2) and Freedom (9)
data = np.loadtxt("world-happiness-report-2021.csv",
                  delimiter=",", skiprows=1, usecols=(2, 9))

ladder = data[:, 0]  # first column (Ladder score)
freedom = data[:, 1] # second column (Freedom score)

# We'll store only the values that meet our condition in these lists.
filtered_ladder = []     # will store ladder scores that pass the filter
filtered_freedom = []    # will store corresponding freedom values

# ---------------------------------------------------------------
# THOUGHT PROCESS 
# range(len(sequence)) = 
    #it first returns the length of the 
    #list and then creates a sequence starting from zero
# len() gives the number of elements (rows) in an array or list.
# We chose the condition "freedom > 0.5" because the freedom scores in this dataset
# range from 0 to 1. A value above 0.5 represents countries where people report
# relatively high personal freedom. This makes the filter easy to understand and
# meaningful for comparing with the Ladder (happiness) scores.
# ---------------------------------------------------------------


# range(len(freedom)) creates a sequence of indices from 0 to number of rows - 1.

for i in range(len(freedom)):

    # If the country's freedom score is greater than 0.5, we keep it.
    if freedom[i] > 0.5:
        
        filtered_ladder.append(ladder[i])
        filtered_freedom.append(freedom[i])
    
    # If the condition is false (freedom <= 0.5), do nothing → skip that country.

print("Original number of countries:", len(freedom))
print("After filtering (freedom > 0.5):", len(filtered_freedom))

# ================================================================
# Part 4: Plotting your data
# ---------------------------------------------------------------
# THOUGHT PROCESS 
    # np.genfromtxt() → similar to loadtxt, but allows text (string) data.
    # dtype=str → means "store this column as text".
    # usecols=(0,) → loads only the first column (the country names)
# ---------------------------------------------------------------

import numpy as np   
import matplotlib
print(matplotlib.__version__)

import matplotlib.pyplot as plt

country = np.genfromtxt("world-happiness-report-2021.csv", delimiter=",", skip_header=1, usecols=(0,), dtype=str)
region = np.genfromtxt("world-happiness-report-2021.csv", delimiter=",", skip_header=1, usecols=(1,), dtype=str)
  
# ----------------------------------------------------------
# 1) Multi-series LINE plot with different colors/styles + grid
# ----------------------------------------------------------
# THOUGHT PROCESS 
    # Sort countries by Ladder score (descending) and plot
    # Ladder vs rank alongside Freedom vs rank to compare trends.
    # This plot helps visualize how a country's reported happiness
    # (ladder) tends to move with its freedom score when countries are ordered
    # by happiness ranking.
    # plt.grid(True) => Adds horizontal and vertical reference lines to make the plot easier to read.
# ----------------------------------------------------------

idx = np.argsort(ladder)[::-1]  # indices that sort ladder high→low

ladder_sorted  = ladder[idx]
freedom_sorted = freedom[idx]

plt.figure(figsize=(9, 5))
# Plot 1 series (solid line, default color)
plt.plot(ladder_sorted, label="Ladder score (happiness)", linestyle="-")  # line style: solid
# Plot 2nd series (dashed line, automatically different color)
plt.plot(freedom_sorted, label="Freedom to make life choices", linestyle="--")  # dashed

# Title and axis labels (per spec a)
plt.title("Happiness vs Freedom (countries ranked by Ladder score)")
plt.xlabel("Country rank (by Ladder score)")
plt.ylabel("Score (unitless)")

plt.grid(True)

# Legend to distinguish the two series
plt.legend()























