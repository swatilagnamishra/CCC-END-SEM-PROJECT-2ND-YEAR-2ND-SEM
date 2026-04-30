# 0/1 Knapsack Problem Solver (Dynamic Programming)

## Overview
This project is a Python GUI application built using Tkinter that solves the classic 0/1 Knapsack Problem using Dynamic Programming.

The program allows users to:
- Add items with weight and value
- Enter knapsack capacity
- Compute maximum possible value
- Display selected items that give the optimal solution

---

## Problem Statement
The 0/1 Knapsack Problem is a well-known optimization problem where:
- Each item has a weight and value
- A bag has limited capacity
- Objective: Maximize total value without exceeding capacity

---

## Features
- Interactive graphical user interface
- Dynamic Programming solution
- Displays selected items
- Input validation
- Reset/Clear option

---

## Algorithm Used
Dynamic Programming

### DP Formula:
if weight <= capacity:
dp[i][w] = max(value + dp[i-1][w-weight], dp[i-1][w])
else:
dp[i][w] = dp[i-1][w]

---

## How to Run

### Step 1: Install Python
Make sure Python 3 is installed.

### Step 2: Save File
Save the code as:

```bash
knapsack.py
## step 3: run program
python knapsack.py

Example Input

Items:

Weight = 2, Value = 3
Weight = 3, Value = 4
Weight = 4, Value = 5
Capacity = 5
Example Output

Maximum Value: 7

Selected Items:

Weight: 2, Value: 3
Weight: 3, Value: 4
