#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 10 09:20:47 2025

@author: v_milioto
"""

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
