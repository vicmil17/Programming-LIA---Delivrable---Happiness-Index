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

# ----------------------------------------------------------
# 2) Two SUBPLOTS side-by-side in the same figure (counts as 1)
# ----------------------------------------------------------
# THOUGHT PROCESS 
    # Show two related scatter plots side-by-side for quick comparison.
    # These two side-by-side plots let us visually compare how happiness
    # changes with GDP vs with social support. Both tend to show positive patterns
# ----------------------------------------------------------

plt.figure(figsize=(12, 5))

# Left subplot: Ladder vs Logged GDP
plt.subplot(1, 2, 1)                 # 1 row, 2 columns, left subplot
plt.scatter(gdp, ladder, alpha=0.7)  # scatter shows relationship
plt.title("Ladder vs Logged GDP per capita")
plt.xlabel("Logged GDP per capita")
plt.ylabel("Ladder (happiness)")
plt.grid(True)  # grid can help see spread

# Right subplot: Ladder vs Social support
plt.subplot(1, 2, 2)                 # 1 row, 2 columns, right subplot
plt.scatter(support, ladder, alpha=0.7)
plt.title("Ladder vs Social Support")
plt.xlabel("Social support (0–1)")
plt.ylabel("Ladder (happiness)")
plt.grid(True)

# ----------------------------------------------------------
# 3) SCATTER plot: Ladder vs Freedom (explicit separate figure)
# ----------------------------------------------------------
# THOUGHT PROCESS 
    # This scatter tests whether greater personal freedom aligns with higher
    # reported happiness. The cloud should trend upward if there’s a positive relation.
    # alpha=0.7 → adds transparency so overlapping dots are visible.
# ----------------------------------------------------------

plt.figure(figsize=(7, 5))
plt.scatter(freedom, ladder, alpha=0.7)
plt.title("Ladder vs Freedom to make life choices")
plt.xlabel("Freedom (0–1)")
plt.ylabel("Ladder (happiness)")
plt.grid(True)

# ----------------------------------------------------------
# 4) BAR plot: Top 10 happiest countries (by Ladder score)
# ----------------------------------------------------------
# THOUGHT PROCESS 
    # Sort by ladder and take the top 10 for a readable bar chart.
# ----------------------------------------------------------

top_n = 10
top_idx = np.argsort(ladder)[-top_n:][::-1]  # indices for top N, in descending order
top_countries = country[top_idx]
top_ladder    = ladder[top_idx]

plt.figure(figsize=(12, 6))
plt.bar(top_countries, top_ladder)
plt.title(f"Top {top_n} Countries by Happiness (Ladder score)")
plt.xlabel("Country")
plt.ylabel("Ladder (happiness)")
plt.xticks(rotation=45, ha="right")  # rotate names for readability
plt.tight_layout()

# ----------------------------------------------------------
# 5) HISTOGRAM: Distribution of Ladder scores
# ----------------------------------------------------------
plt.figure(figsize=(8, 5))
plt.hist(ladder, bins=12)  # choose a reasonable number of bins
plt.title("Distribution of Happiness (Ladder scores)")
plt.xlabel("Ladder score")
plt.ylabel("Number of countries")
plt.grid(True)

# ----------------------------------------------------------
# 6) PIE chart: Share of countries by Region
# ----------------------------------------------------------
# THOUGHT PROCESS 
    # Count countries per region; if there are many, group the smaller ones
    # The pie chart gives a quick sense of the dataset’s regional composition.
    # autopct="%1.1f%%" → automatically prints percentages on slices.
    # startangle=90 → rotates the chart so the first slice starts at the top.
# ----------------------------------------------------------

# Compute counts per region
unique_regions, counts = np.unique(region, return_counts=True)

# Sort regions by count descending
order = np.argsort(counts)[::-1]
unique_regions = unique_regions[order]
counts = counts[order]

# If too many slices, keep top 6 and group the rest as "Other"
max_slices = 6
if len(counts) > max_slices:
    top_regions = unique_regions[:max_slices - 1]
    top_counts  = counts[:max_slices - 1]
    other_count = counts[max_slices - 1:].sum()
    labels = list(top_regions) + ["Other"]
    sizes  = list(top_counts)  + [other_count]
else:
    labels = list(unique_regions)
    sizes  = list(counts)

plt.figure(figsize=(7, 7))
plt.pie(sizes, labels=labels, autopct="%1.1f%%", startangle=90)
plt.title("Share of Countries by Region")
plt.tight_layout()
