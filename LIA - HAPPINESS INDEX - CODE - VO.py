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
hi 
