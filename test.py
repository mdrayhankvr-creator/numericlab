"""
================================================================================
LAB EXAMINATION 2: NUMERICAL SOLUTION OF ORDINARY DIFFERENTIAL EQUATIONS
Complete Solution Manual - All 25 Problems (Fully Commented)
================================================================================
"""

# ================================================================================
# PROBLEM 1: EULER'S METHOD
# ================================================================================
# Problem: Solve the initial-value problem dy/dx = x + y, y(0) = 1
# Estimate y at x = 0.5 using Euler's Method
#
# Sample Input: x0=0, y0=1, h=0.1, x_target=0.5
# Sample Output: Approximate y(0.5) = 1.721020
#
# Method Formula: y_(n+1) = y_n + h*f(x_n, y_n)
#
# Pseudocode:
# read x0, y0, h, x_target
# n <- round((x_target - x0)/h)
# x <- x0; y <- y0
# repeat n times: y <- y + h*f(x,y); x <- x + h
# print y
#
# Reference Python Solution:
# def f(x, y):
#     return x + y
# x = 0
# y = 1
# h = 0.1
# x_target = 0.5
# n = round((x_target - x) / h)
# for _ in range(n):
#     y = y + h*f(x, y)
#     x = x + h
# print(f"Approximate y(0.5) = {y:.6f}")
#
# Computed Result: y(0.5) ≈ 1.721020
# Reference Exact Solution: y = 2*e^x - x - 1
#
# Answer Key:
# 1. Number of steps: n = (x_target - x0) / h = (0.5 - 0) / 0.1 = 5 steps
# 2. First update: f(0,1) = 1.000000; y1 = 1.000000 + 0.1(1.000000) = 1.100000
# 3. Loop Control: Use exactly n=5 iterations (for _ in range(n))
# 4. Global Accuracy: Euler's method is first-order. Halving h reduces error by ~2x
# 5. Programming Check: Verify h > 0, x_target >= x0, divisibility by h, finite f(x,y)

# ================================================================================
# PROBLEM 2: EULER'S METHOD
# ================================================================================
# Problem: Solve dy/dx = y - x^2 + 1, y(0) = 0.5
# Approximate y at x = 1.0
#
# Sample Input: x0=0, y0=0.5, h=0.2, x_target=1.0
# Sample Output: Approximate y(1.0) = 2.458176
#
# Method Formula: y_(n+1) = y_n + h*f(x_n, y_n)
#
# Pseudocode:
# read x0, y0, h, x_target
# n <- round((x_target - x0)/h)
# x <- x0; y <- y0
# repeat n times: y <- y + h*f(x,y); x <- x + h
# print y
#
# Reference Python Solution:
# def f(x, y):
#     return y - x**2 + 1
# x = 0
# y = 0.5
# h = 0.2
# x_target = 1.0
# n = round((x_target - x) / h)
# for _ in range(n):
#     y = y + h*f(x, y)
#     x = x + h
# print(f"Approximate y(1.0) = {y:.6f}")
#
# Computed Result: y(1.0) ≈ 2.458176
# Reference Exact Solution: y = (x + 1)^2 - 0.5*e^x
#
# Answer Key:
# 1. Number of steps: n = (1.0 - 0) / 0.2 = 5 steps
# 2. First update: f(0, 0.5) = 1.500000; y1 = 0.500000 + 0.2(1.500000) = 0.800000
# 3. Loop Control: Use exactly n=5 iterations
# 4. Global Accuracy: First-order, halving h reduces error by ~2x
# 5. Programming Check: h > 0, x_target >= x0, divisibility, finite values

# ================================================================================
# PROBLEM 3: EULER'S METHOD
# ================================================================================
# Problem: Solve dy/dx = x(1+y), y(0) = 1
# Approximate y at x = 1.0
#
# Sample Input: x0=0, y0=1, h=0.25, x_target=1.0
# Sample Output: Approximate y(1.0) = 1.838867
#
# Method Formula: y_(n+1) = y_n + h*f(x_n, y_n)
#
# Reference Python Solution:
# def f(x, y):
#     return x*(1+y)
# x = 0
# y = 1
# h = 0.25
# x_target = 1.0
# n = round((x_target - x) / h)
# for _ in range(n):
#     y = y + h*f(x, y)
#     x = x + h
# print(f"Approximate y(1.0) = {y:.6f}")
#
# Computed Result: y(1.0) ≈ 1.838867
# Reference Exact Solution: y = 2*e^(x^2/2) - 1
#
# Answer Key:
# 1. Number of steps: n = (1.0 - 0) / 0.25 = 4 steps
# 2. First update: f(0,1) = 0.000000; y1 = 1.000000 + 0.25(0.000000) = 1.000000
# 3. Loop Control: Use exactly n=4 iterations
# 4. Global Accuracy: First-order, error reduction factor ~2
# 5. Programming Check: Standard validation checks

# ================================================================================
# PROBLEM 4: EULER'S METHOD
# ================================================================================
# Problem: Solve dy/dx = -2xy, y(0) = 1
# Approximate y at x = 1.0
#
# Sample Input: x0=0, y0=1, h=0.2, x_target=1.0
# Sample Output: Approximate y(1.0) = 0.399383
#
# Method Formula: y_(n+1) = y_n + h*f(x_n, y_n)
#
# Reference Python Solution:
# def f(x, y):
#     return -2*x*y
# x = 0
# y = 1
# h = 0.2
# x_target = 1.0
# n = round((x_target - x) / h)
# for _ in range(n):
#     y = y + h*f(x, y)
#     x = x + h
# print(f"Approximate y(1.0) = {y:.6f}")
#
# Computed Result: y(1.0) ≈ 0.399383
# Reference Exact Solution: y = e^(-x^2)
#
# Answer Key:
# 1. Number of steps: n = (1.0 - 0) / 0.2 = 5 steps
# 2. First update: f(0,1) = 0.000000; y1 = 1.000000 + 0.2(0.000000) = 1.000000
# 3. Loop Control: Use exactly n=5 iterations
# 4. Global Accuracy: First-order, error reduction ~2x
# 5. Programming Check: Validation of parameters and function output

# ================================================================================
# PROBLEM 5: EULER'S METHOD
# ================================================================================
# Problem: Solve dy/dx = y/(1+x), y(0) = 2
# Approximate y at x = 1.0
#
# Sample Input: x0=0, y0=2, h=0.25, x_target=1.0
# Sample Output: Approximate y(1.0) = 4.000000
#
# Method Formula: y_(n+1) = y_n + h*f(x_n, y_n)
#
# Reference Python Solution:
# def f(x, y):
#     return y/(1+x)
# x = 0
# y = 2
# h = 0.25
# x_target = 1.0
# n = round((x_target - x) / h)
# for _ in range(n):
#     y = y + h*f(x, y)
#     x = x + h
# print(f"Approximate y(1.0) = {y:.6f}")
#
# Computed Result: y(1.0) ≈ 4.000000
# Reference Exact Solution: y = 2(1+x)
#
# Answer Key:
# 1. Number of steps: n = (1.0 - 0) / 0.25 = 4 steps
# 2. First update: f(0,2) = 2.000000; y1 = 2.000000 + 0.25(2.000000) = 2.500000
# 3. Loop Control: Use exactly n=4 iterations
# 4. Global Accuracy: First-order, error reduction ~2x
# 5. Programming Check: Standard validation

# ================================================================================
# PROBLEM 6: RUNGE-KUTTA 2ND ORDER - HEUN'S METHOD
# ================================================================================
# Problem: Solve dy/dx = x + y, y(0) = 1
# Estimate y at x = 0.5 using Heun's Method
#
# Sample Input: x0=0, y0=1, h=0.1, x_target=0.5
# Sample Output: Approximate y(0.5) = 1.794894
#
# Method Formula:
# k1 = f(x_n, y_n)
# k2 = f(x_n + h, y_n + h*k1)
# y_(n+1) = y_n + h*(k1 + k2)/2
#
# Pseudocode:
# read inputs; compute n; set x=x0, y=y0
# repeat n times:
#     k1 <- f(x,y)
#     k2 <- f(x+h, y+h*k1)
#     y <- y + h*(k1+k2)/2; x <- x+h
# print y
#
# Reference Python Solution:
# def f(x, y):
#     return x + y
# x = 0
# y = 1
# h = 0.1
# x_target = 0.5
# n = round((x_target - x) / h)
# for _ in range(n):
#     k1 = f(x, y)
#     k2 = f(x+h, y+h*k1)
#     y = y + h*(k1+k2)/2
#     x = x + h
# print(f"Approximate y(0.5) = {y:.6f}")
#
# Computed Result: y(0.5) ≈ 1.794894
# Reference Exact Solution: y = 2*e^x - x - 1
#
# Answer Key:
# 1. Number of steps: n = (0.5 - 0) / 0.1 = 5 steps
# 2. First update: k1=1.000000, predictor=1.100000, k2=1.200000; y1=1.110000
# 3. Loop Control: Use exactly n=5 iterations
# 4. Global Accuracy: RK2 is second-order. Halving h reduces error by ~4x
# 5. Programming Check: h > 0, x_target >= x0, divisibility, finite values

# ================================================================================
# PROBLEM 7: RUNGE-KUTTA 2ND ORDER - HEUN'S METHOD
# ================================================================================
# Problem: Solve dy/dx = y - x^2 + 1, y(0) = 0.5
# Approximate y at x = 1.0
#
# Sample Input: x0=0, y0=0.5, h=0.2, x_target=1.0
# Sample Output: Approximate y(1.0) = 2.617688
#
# Method Formula:
# k1 = f(x_n, y_n)
# k2 = f(x_n + h, y_n + h*k1)
# y_(n+1) = y_n + h*(k1 + k2)/2
#
# Reference Python Solution:
# def f(x, y):
#     return y - x**2 + 1
# x = 0
# y = 0.5
# h = 0.2
# x_target = 1.0
# n = round((x_target - x) / h)
# for _ in range(n):
#     k1 = f(x, y)
#     k2 = f(x+h, y+h*k1)
#     y = y + h*(k1+k2)/2
#     x = x + h
# print(f"Approximate y(1.0) = {y:.6f}")
#
# Computed Result: y(1.0) ≈ 2.617688
# Reference Exact Solution: y = (x+1)^2 - 0.5*e^x
#
# Answer Key:
# 1. Number of steps: n = (1.0 - 0) / 0.2 = 5 steps
# 2. First update: k1=1.500000, predictor=0.800000, k2=1.760000; y1=0.826000
# 3. Loop Control: Use exactly n=5 iterations
# 4. Global Accuracy: Second-order, error reduction ~4x
# 5. Programming Check: Standard validation checks

# ================================================================================
# PROBLEM 8: RUNGE-KUTTA 2ND ORDER - HEUN'S METHOD
# ================================================================================
# Problem: Solve dy/dx = sin(x) - y, y(0) = 1
# Approximate y at x = 1.0
#
# Sample Input: x0=0, y0=1, h=0.2, x_target=1.0
# Sample Output: Approximate y(1.0) = 0.706270
#
# Method Formula:
# k1 = f(x_n, y_n)
# k2 = f(x_n + h, y_n + h*k1)
# y_(n+1) = y_n + h*(k1 + k2)/2
#
# Reference Python Solution:
# import math
# def f(x, y):
#     return math.sin(x)-y
# x = 0
# y = 1
# h = 0.2
# x_target = 1.0
# n = round((x_target - x) / h)
# for _ in range(n):
#     k1 = f(x, y)
#     k2 = f(x+h, y+h*k1)
#     y = y + h*(k1+k2)/2
#     x = x + h
# print(f"Approximate y(1.0) = {y:.6f}")
#
# Computed Result: y(1.0) ≈ 0.706270
#
# Answer Key:
# 1. Number of steps: n = (1.0 - 0) / 0.2 = 5 steps
# 2. First update: k1=-1.000000, predictor=0.800000, k2=-0.601331; y1=0.839867
# 3. Loop Control: Use exactly n=5 iterations
# 4. Global Accuracy: Second-order, error reduction ~4x
# 5. Programming Check: Validation of parameters and function

# ================================================================================
# PROBLEM 9: RUNGE-KUTTA 2ND ORDER - HEUN'S METHOD
# ================================================================================
# Problem: Solve dy/dx = x*y, y(0) = 1
# Approximate y at x = 1.0
#
# Sample Input: x0=0, y0=1, h=0.25, x_target=1.0
# Sample Output: Approximate y(1.0) = 1.642286
#
# Method Formula:
# k1 = f(x_n, y_n)
# k2 = f(x_n + h, y_n + h*k1)
# y_(n+1) = y_n + h*(k1 + k2)/2
#
# Reference Python Solution:
# def f(x, y):
#     return x*y
# x = 0
# y = 1
# h = 0.25
# x_target = 1.0
# n = round((x_target - x) / h)
# for _ in range(n):
#     k1 = f(x, y)
#     k2 = f(x+h, y+h*k1)
#     y = y + h*(k1+k2)/2
#     x = x + h
# print(f"Approximate y(1.0) = {y:.6f}")
#
# Computed Result: y(1.0) ≈ 1.642286
# Reference Exact Solution: y = e^(x^2/2)
#
# Answer Key:
# 1. Number of steps: n = (1.0 - 0) / 0.25 = 4 steps
# 2. First update: k1=0.000000, predictor=1.000000, k2=0.250000; y1=1.031250
# 3. Loop Control: Use exactly n=4 iterations
# 4. Global Accuracy: Second-order, error reduction ~4x
# 5. Programming Check: Standard validation

# ================================================================================
# PROBLEM 10: RUNGE-KUTTA 2ND ORDER - HEUN'S METHOD
# ================================================================================
# Problem: Solve dy/dx = 1 + x - y, y(0) = 0
# Approximate y at x = 1.0
#
# Sample Input: x0=0, y0=0, h=0.2, x_target=1.0
# Sample Output: Approximate y(1.0) = 1.000000
#
# Method Formula:
# k1 = f(x_n, y_n)
# k2 = f(x_n + h, y_n + h*k1)
# y_(n+1) = y_n + h*(k1 + k2)/2
#
# Reference Python Solution:
# def f(x, y):
#     return 1+x-y
# x = 0
# y = 0
# h = 0.2
# x_target = 1.0
# n = round((x_target - x) / h)
# for _ in range(n):
#     k1 = f(x, y)
#     k2 = f(x+h, y+h*k1)
#     y = y + h*(k1+k2)/2
#     x = x + h
# print(f"Approximate y(1.0) = {y:.6f}")
#
# Computed Result: y(1.0) ≈ 1.000000
# Reference Exact Solution: y = x
#
# Answer Key:
# 1. Number of steps: n = (1.0 - 0) / 0.2 = 5 steps
# 2. First update: k1=1.000000, predictor=0.200000, k2=1.000000; y1=0.200000
# 3. Loop Control: Use exactly n=5 iterations
# 4. Global Accuracy: Second-order, error reduction ~4x
# 5. Programming Check: Validation checks

# ================================================================================
# PROBLEM 11: RUNGE-KUTTA 2ND ORDER - MIDPOINT METHOD
# ================================================================================
# Problem: Solve dy/dx = x + y, y(0) = 1
# Estimate y at x = 0.5 using Midpoint RK2
#
# Sample Input: x0=0, y0=1, h=0.1, x_target=0.5
# Sample Output: Approximate y(0.5) = 1.794894
#
# Method Formula:
# k1 = f(x_n, y_n)
# k2 = f(x_n + h/2, y_n + h*k1/2)
# y_(n+1) = y_n + h*k2
#
# Pseudocode:
# read inputs; compute n; set x=x0, y=y0
# repeat n times:
#     k1 <- f(x,y)
#     k2 <- f(x+h/2, y+h*k1/2)
#     y <- y + h*k2; x <- x+h
# print y
#
# Reference Python Solution:
# def f(x, y):
#     return x + y
# x = 0
# y = 1
# h = 0.1
# x_target = 0.5
# n = round((x_target - x) / h)
# for _ in range(n):
#     k1 = f(x, y)
#     k2 = f(x+h/2, y+h*k1/2)
#     y = y + h*k2
#     x = x + h
# print(f"Approximate y(0.5) = {y:.6f}")
#
# Computed Result: y(0.5) ≈ 1.794894
# Reference Exact Solution: y = 2*e^x - x - 1
#
# Answer Key:
# 1. Number of steps: n = (0.5 - 0) / 0.1 = 5 steps
# 2. First update: k1=1.000000; midpoint=(0.050000, 1.050000); k2=1.100000; y1=1.110000
# 3. Loop Control: Use exactly n=5 iterations
# 4. Global Accuracy: Second-order, error reduction ~4x
# 5. Programming Check: h > 0, x_target >= x0, divisibility, finite values

# ================================================================================
# PROBLEM 12: RUNGE-KUTTA 2ND ORDER - MIDPOINT METHOD
# ================================================================================
# Problem: Solve dy/dx = y - x^2 + 1, y(0) = 0.5
# Approximate y at x = 1.0
#
# Sample Input: x0=0, y0=0.5, h=0.2, x_target=1.0
# Sample Output: Approximate y(1.0) = 2.633167
#
# Method Formula:
# k1 = f(x_n, y_n)
# k2 = f(x_n + h/2, y_n + h*k1/2)
# y_(n+1) = y_n + h*k2
#
# Reference Python Solution:
# def f(x, y):
#     return y - x**2 + 1
# x = 0
# y = 0.5
# h = 0.2
# x_target = 1.0
# n = round((x_target - x) / h)
# for _ in range(n):
#     k1 = f(x, y)
#     k2 = f(x+h/2, y+h*k1/2)
#     y = y + h*k2
#     x = x + h
# print(f"Approximate y(1.0) = {y:.6f}")
#
# Computed Result: y(1.0) ≈ 2.633167
# Reference Exact Solution: y = (x+1)^2 - 0.5*e^x
#
# Answer Key:
# 1. Number of steps: n = (1.0 - 0) / 0.2 = 5 steps
# 2. First update: k1=1.500000; midpoint=(0.100000, 0.650000); k2=1.640000; y1=0.828000
# 3. Loop Control: Use exactly n=5 iterations
# 4. Global Accuracy: Second-order, error reduction ~4x
# 5. Programming Check: Validation checks

# ================================================================================
# PROBLEM 13: RUNGE-KUTTA 2ND ORDER - MIDPOINT METHOD
# ================================================================================
# Problem: Solve dy/dx = cos(x) + y, y(0) = 0
# Approximate y at x = 1.0
#
# Sample Input: x0=0, y0=0, h=0.2, x_target=1.0
# Sample Output: Approximate y(1.0) = 1.501375
#
# Method Formula:
# k1 = f(x_n, y_n)
# k2 = f(x_n + h/2, y_n + h*k1/2)
# y_(n+1) = y_n + h*k2
#
# Reference Python Solution:
# import math
# def f(x, y):
#     return math.cos(x)+y
# x = 0
# y = 0
# h = 0.2
# x_target = 1.0
# n = round((x_target - x) / h)
# for _ in range(n):
#     k1 = f(x, y)
#     k2 = f(x+h/2, y+h*k1/2)
#     y = y + h*k2
#     x = x + h
# print(f"Approximate y(1.0) = {y:.6f}")
#
# Computed Result: y(1.0) ≈ 1.501375
#
# Answer Key:
# 1. Number of steps: n = (1.0 - 0) / 0.2 = 5 steps
# 2. First update: k1=1.000000; midpoint=(0.100000, 0.100000); k2=1.095004; y1=0.219001
# 3. Loop Control: Use exactly n=5 iterations
# 4. Global Accuracy: Second-order, error reduction ~4x
# 5. Programming Check: Standard validation

# ================================================================================
# PROBLEM 14: RUNGE-KUTTA 2ND ORDER - MIDPOINT METHOD
# ================================================================================
# Problem: Solve dy/dx = -x*y, y(0) = 2
# Approximate y at x = 1.0
#
# Sample Input: x0=0, y0=2, h=0.25, x_target=1.0
# Sample Output: Approximate y(1.0) = 1.205441
#
# Method Formula:
# k1 = f(x_n, y_n)
# k2 = f(x_n + h/2, y_n + h*k1/2)
# y_(n+1) = y_n + h*k2
#
# Reference Python Solution:
# def f(x, y):
#     return -x*y
# x = 0
# y = 2
# h = 0.25
# x_target = 1.0
# n = round((x_target - x) / h)
# for _ in range(n):
#     k1 = f(x, y)
#     k2 = f(x+h/2, y+h*k1/2)
#     y = y + h*k2
#     x = x + h
# print(f"Approximate y(1.0) = {y:.6f}")
#
# Computed Result: y(1.0) ≈ 1.205441
# Reference Exact Solution: y = 2*e^(-x^2/2)
#
# Answer Key:
# 1. Number of steps: n = (1.0 - 0) / 0.25 = 4 steps
# 2. First update: k1=0.000000; midpoint=(0.125000, 2.000000); k2=-0.250000; y1=1.937500
# 3. Loop Control: Use exactly n=4 iterations
# 4. Global Accuracy: Second-order, error reduction ~4x
# 5. Programming Check: Validation checks

# ================================================================================
# PROBLEM 15: RUNGE-KUTTA 2ND ORDER - MIDPOINT METHOD
# ================================================================================
# Problem: Solve dy/dx = x/(1+y), y(0) = 0
# Approximate y at x = 1.0
#
# Sample Input: x0=0, y0=0, h=0.2, x_target=1.0
# Sample Output: Approximate y(1.0) = 0.416142
#
# Method Formula:
# k1 = f(x_n, y_n)
# k2 = f(x_n + h/2, y_n + h*k1/2)
# y_(n+1) = y_n + h*k2
#
# Reference Python Solution:
# def f(x, y):
#     return x/(1+y)
# x = 0
# y = 0
# h = 0.2
# x_target = 1.0
# n = round((x_target - x) / h)
# for _ in range(n):
#     k1 = f(x, y)
#     k2 = f(x+h/2, y+h*k1/2)
#     y = y + h*k2
#     x = x + h
# print(f"Approximate y(1.0) = {y:.6f}")
#
# Computed Result: y(1.0) ≈ 0.416142
# Reference Exact Solution: y = sqrt(1+x^2) - 1
#
# Answer Key:
# 1. Number of steps: n = (1.0 - 0) / 0.2 = 5 steps
# 2. First update: k1=0.000000; midpoint=(0.100000, 0.000000); k2=0.100000; y1=0.020000
# 3. Loop Control: Use exactly n=5 iterations
# 4. Global Accuracy: Second-order, error reduction ~4x
# 5. Programming Check: Standard validation

# ================================================================================
# PROBLEM 16: RUNGE-KUTTA 2ND ORDER - RALSTON'S METHOD
# ================================================================================
# Problem: Solve dy/dx = x + y, y(0) = 1
# Estimate y at x = 0.5 using Ralston's RK2
#
# Sample Input: x0=0, y0=1, h=0.1, x_target=0.5
# Sample Output: Approximate y(0.5) = 1.794894
#
# Method Formula:
# k1 = f(x_n, y_n)
# k2 = f(x_n + 2h/3, y_n + 2h*k1/3)
# y_(n+1) = y_n + h*(k1/4 + 3*k2/4)
#
# Pseudocode:
# read inputs; compute n; set x=x0, y=y0
# repeat n times:
#     k1 <- f(x,y)
#     k2 <- f(x+2h/3, y+2h*k1/3)
#     y <- y + h*(k1/4 + 3*k2/4); x <- x+h
# print y
#
# Reference Python Solution:
# def f(x, y):
#     return x + y
# x = 0
# y = 1
# h = 0.1
# x_target = 0.5
# n = round((x_target - x) / h)
# for _ in range(n):
#     k1 = f(x, y)
#     k2 = f(x+2*h/3, y+2*h*k1/3)
#     y = y + h*(k1/4 + 3*k2/4)
#     x = x + h
# print(f"Approximate y(0.5) = {y:.6f}")
#
# Computed Result: y(0.5) ≈ 1.794894
# Reference Exact Solution: y = 2*e^x - x - 1
#
# Answer Key:
# 1. Number of steps: n = (0.5 - 0) / 0.1 = 5 steps
# 2. First update: k1=1.000000; second-stage=(0.066667, 1.066667); k2=1.133333; y1=1.110000
# 3. Loop Control: Use exactly n=5 iterations
# 4. Global Accuracy: Second-order, error reduction ~4x
# 5. Programming Check: h > 0, x_target >= x0, divisibility, finite values

# ================================================================================
# PROBLEM 17: RUNGE-KUTTA 2ND ORDER - RALSTON'S METHOD
# ================================================================================
# Problem: Solve dy/dx = y - x^2 + 1, y(0) = 0.5
# Approximate y at x = 1.0
#
# Sample Input: x0=0, y0=0.5, h=0.2, x_target=1.0
# Sample Output: Approximate y(1.0) = 2.628007
#
# Method Formula:
# k1 = f(x_n, y_n)
# k2 = f(x_n + 2h/3, y_n + 2h*k1/3)
# y_(n+1) = y_n + h*(k1/4 + 3*k2/4)
#
# Reference Python Solution:
# def f(x, y):
#     return y - x**2 + 1
# x = 0
# y = 0.5
# h = 0.2
# x_target = 1.0
# n = round((x_target - x) / h)
# for _ in range(n):
#     k1 = f(x, y)
#     k2 = f(x+2*h/3, y+2*h*k1/3)
#     y = y + h*(k1/4 + 3*k2/4)
#     x = x + h
# print(f"Approximate y(1.0) = {y:.6f}")
#
# Computed Result: y(1.0) ≈ 2.628007
# Reference Exact Solution: y = (x+1)^2 - 0.5*e^x
#
# Answer Key:
# 1. Number of steps: n = (1.0 - 0) / 0.2 = 5 steps
# 2. First update: k1=1.500000; second-stage=(0.133333, 0.700000); k2=1.682222; y1=0.827333
# 3. Loop Control: Use exactly n=5 iterations
# 4. Global Accuracy: Second-order, error reduction ~4x
# 5. Programming Check: Validation checks

# ================================================================================
# PROBLEM 18: RUNGE-KUTTA 2ND ORDER - RALSTON'S METHOD
# ================================================================================
# Problem: Solve dy/dx = x - y, y(0) = 1
# Approximate y at x = 1.0
#
# Sample Input: x0=0, y0=1, h=0.2, x_target=1.0
# Sample Output: Approximate y(1.0) = 0.741480
#
# Method Formula:
# k1 = f(x_n, y_n)
# k2 = f(x_n + 2h/3, y_n + 2h*k1/3)
# y_(n+1) = y_n + h*(k1/4 + 3*k2/4)
#
# Reference Python Solution:
# def f(x, y):
#     return x-y
# x = 0
# y = 1
# h = 0.2
# x_target = 1.0
# n = round((x_target - x) / h)
# for _ in range(n):
#     k1 = f(x, y)
#     k2 = f(x+2*h/3, y+2*h*k1/3)
#     y = y + h*(k1/4 + 3*k2/4)
#     x = x + h
# print(f"Approximate y(1.0) = {y:.6f}")
#
# Computed Result: y(1.0) ≈ 0.741480
# Reference Exact Solution: y = x - 1 + 2*e^(-x)
#
# Answer Key:
# 1. Number of steps: n = (1.0 - 0) / 0.2 = 5 steps
# 2. First update: k1=-1.000000; second-stage=(0.133333, 0.866667); k2=-0.733333; y1=0.840000
# 3. Loop Control: Use exactly n=5 iterations
# 4. Global Accuracy: Second-order, error reduction ~4x
# 5. Programming Check: Standard validation

# ================================================================================
# PROBLEM 19: RUNGE-KUTTA 2ND ORDER - RALSTON'S METHOD
# ================================================================================
# Problem: Solve dy/dx = x*y + 1, y(0) = 0
# Approximate y at x = 1.0
#
# Sample Input: x0=0, y0=0, h=0.25, x_target=1.0
# Sample Output: Approximate y(1.0) = 1.400210
#
# Method Formula:
# k1 = f(x_n, y_n)
# k2 = f(x_n + 2h/3, y_n + 2h*k1/3)
# y_(n+1) = y_n + h*(k1/4 + 3*k2/4)
#
# Reference Python Solution:
# def f(x, y):
#     return x*y+1
# x = 0
# y = 0
# h = 0.25
# x_target = 1.0
# n = round((x_target - x) / h)
# for _ in range(n):
#     k1 = f(x, y)
#     k2 = f(x+2*h/3, y+2*h*k1/3)
#     y = y + h*(k1/4 + 3*k2/4)
#     x = x + h
# print(f"Approximate y(1.0) = {y:.6f}")
#
# Computed Result: y(1.0) ≈ 1.400210
#
# Answer Key:
# 1. Number of steps: n = (1.0 - 0) / 0.25 = 4 steps
# 2. First update: k1=1.000000; second-stage=(0.166667, 0.166667); k2=1.027778; y1=0.255208
# 3. Loop Control: Use exactly n=4 iterations
# 4. Global Accuracy: Second-order, error reduction ~4x
# 5. Programming Check: Validation checks

# ================================================================================
# PROBLEM 20: RUNGE-KUTTA 2ND ORDER - RALSTON'S METHOD
# ================================================================================
# Problem: Solve dy/dx = y/(1+x^2), y(0) = 1
# Approximate y at x = 1.0
#
# Sample Input: x0=0, y0=1, h=0.2, x_target=1.0
# Sample Output: Approximate y(1.0) = 2.190439
#
# Method Formula:
# k1 = f(x_n, y_n)
# k2 = f(x_n + 2h/3, y_n + 2h*k1/3)
# y_(n+1) = y_n + h*(k1/4 + 3*k2/4)
#
# Reference Python Solution:
# def f(x, y):
#     return y/(1+x**2)
# x = 0
# y = 1
# h = 0.2
# x_target = 1.0
# n = round((x_target - x) / h)
# for _ in range(n):
#     k1 = f(x, y)
#     k2 = f(x+2*h/3, y+2*h*k1/3)
#     y = y + h*(k1/4 + 3*k2/4)
#     x = x + h
# print(f"Approximate y(1.0) = {y:.6f}")
#
# Computed Result: y(1.0) ≈ 2.190439
# Reference Exact Solution: y = e^(arctan(x))
#
# Answer Key:
# 1. Number of steps: n = (1.0 - 0) / 0.2 = 5 steps
# 2. First update: k1=1.000000; second-stage=(0.133333, 1.133333); k2=1.113537; y1=1.217031
# 3. Loop Control: Use exactly n=5 iterations
# 4. Global Accuracy: Second-order, error reduction ~4x
# 5. Programming Check: Standard validation

# ================================================================================
# PROBLEM 21: RUNGE-KUTTA 4TH ORDER METHOD
# ================================================================================
# Problem: Solve dy/dx = x + y, y(0) = 1
# Estimate y at x = 0.5 using classical RK4
#
# Sample Input: x0=0, y0=1, h=0.1, x_target=0.5
# Sample Output: Approximate y(0.5) = 1.797441
#
# Method Formula:
# k1 = f(x_n, y_n)
# k2 = f(x_n + h/2, y_n + h*k1/2)
# k3 = f(x_n + h/2, y_n + h*k2/2)
# k4 = f(x_n + h, y_n + h*k3)
# y_(n+1) = y_n + h*(k1 + 2*k2 + 2*k3 + k4)/6
#
# Pseudocode:
# read inputs; compute n; set x=x0, y=y0
# repeat n times:
#     k1 <- f(x,y)
#     k2 <- f(x+h/2, y+h*k1/2)
#     k3 <- f(x+h/2, y+h*k2/2)
#     k4 <- f(x+h, y+h*k3)
#     y <- y + h*(k1+2*k2+2*k3+k4)/6; x <- x+h
# print y
#
# Reference Python Solution:
# def f(x, y):
#     return x + y
# x = 0
# y = 1
# h = 0.1
# x_target = 0.5
# n = round((x_target - x) / h)
# for _ in range(n):
#     k1 = f(x, y)
#     k2 = f(x+h/2, y+h*k1/2)
#     k3 = f(x+h/2, y+h*k2/2)
#     k4 = f(x+h, y+h*k3)
#     y = y + h*(k1+2*k2+2*k3+k4)/6
#     x = x + h
# print(f"Approximate y(0.5) = {y:.6f}")
#
# Computed Result: y(0.5) ≈ 1.797441
# Reference Exact Solution: y = 2*e^x - x - 1
#
# Answer Key:
# 1. Number of steps: n = (0.5 - 0) / 0.1 = 5 steps
# 2. First update: k1=1.000000, k2=1.100000, k3=1.105000, k4=1.210500; y1=1.110342
# 3. Loop Control: Use exactly n=5 iterations
# 4. Global Accuracy: RK4 is fourth-order. Halving h reduces error by ~16x
# 5. Programming Check: h > 0, x_target >= x0, divisibility, finite values

# ================================================================================
# PROBLEM 22: RUNGE-KUTTA 4TH ORDER METHOD
# ================================================================================
# Problem: Solve dy/dx = y - x^2 + 1, y(0) = 0.5
# Approximate y at x = 1.0
#
# Sample Input: x0=0, y0=0.5, h=0.2, x_target=1.0
# Sample Output: Approximate y(1.0) = 2.640823
#
# Method Formula:
# k1 = f(x_n, y_n)
# k2 = f(x_n + h/2, y_n + h*k1/2)
# k3 = f(x_n + h/2, y_n + h*k2/2)
# k4 = f(x_n + h, y_n + h*k3)
# y_(n+1) = y_n + h*(k1 + 2*k2 + 2*k3 + k4)/6
#
# Reference Python Solution:
# def f(x, y):
#     return y - x**2 + 1
# x = 0
# y = 0.5
# h = 0.2
# x_target = 1.0
# n = round((x_target - x) / h)
# for _ in range(n):
#     k1 = f(x, y)
#     k2 = f(x+h/2, y+h*k1/2)
#     k3 = f(x+h/2, y+h*k2/2)
#     k4 = f(x+h, y+h*k3)
#     y = y + h*(k1+2*k2+2*k3+k4)/6
#     x = x + h
# print(f"Approximate y(1.0) = {y:.6f}")
#
# Computed Result: y(1.0) ≈ 2.640823
# Reference Exact Solution: y = (x+1)^2 - 0.5*e^x
#
# Answer Key:
# 1. Number of steps: n = (1.0 - 0) / 0.2 = 5 steps
# 2. First update: k1=1.500000, k2=1.640000, k3=1.654000, k4=1.790800; y1=0.829293
# 3. Loop Control: Use exactly n=5 iterations
# 4. Global Accuracy: Fourth-order, error reduction ~16x
# 5. Programming Check: Validation checks

# ================================================================================
# PROBLEM 23: RUNGE-KUTTA 4TH ORDER METHOD
# ================================================================================
# Problem: Solve dy/dx = sin(x) + y, y(0) = 0
# Approximate y at x = 1.0
#
# Sample Input: x0=0, y0=0, h=0.2, x_target=1.0
# Sample Output: Approximate y(1.0) = 0.668228
#
# Method Formula:
# k1 = f(x_n, y_n)
# k2 = f(x_n + h/2, y_n + h*k1/2)
# k3 = f(x_n + h/2, y_n + h*k2/2)
# k4 = f(x_n + h, y_n + h*k3)
# y_(n+1) = y_n + h*(k1 + 2*k2 + 2*k3 + k4)/6
#
# Reference Python Solution:
# import math
# def f(x, y):
#     return math.sin(x)+y
# x = 0
# y = 0
# h = 0.2
# x_target = 1.0
# n = round((x_target - x) / h)
# for _ in range(n):
#     k1 = f(x, y)
#     k2 = f(x+h/2, y+h*k1/2)
#     k3 = f(x+h/2, y+h*k2/2)
#     k4 = f(x+h, y+h*k3)
#     y = y + h*(k1+2*k2+2*k3+k4)/6
#     x = x + h
# print(f"Approximate y(1.0) = {y:.6f}")
#
# Computed Result: y(1.0) ≈ 0.668228
#
# Answer Key:
# 1. Number of steps: n = (1.0 - 0) / 0.2 = 5 steps
# 2. First update: k1=0.000000, k2=0.099833, k3=0.109817, k4=0.220633; y1=0.021331
# 3. Loop Control: Use exactly n=5 iterations
# 4. Global Accuracy: Fourth-order, error reduction ~16x
# 5. Programming Check: Standard validation

# ================================================================================
# PROBLEM 24: RUNGE-KUTTA 4TH ORDER METHOD
# ================================================================================
# Problem: Solve dy/dx = -2xy + x, y(0) = 1
# Approximate y at x = 1.0
#
# Sample Input: x0=0, y0=1, h=0.25, x_target=1.0
# Sample Output: Approximate y(1.0) = 0.683967
#
# Method Formula:
# k1 = f(x_n, y_n)
# k2 = f(x_n + h/2, y_n + h*k1/2)
# k3 = f(x_n + h/2, y_n + h*k2/2)
# k4 = f(x_n + h, y_n + h*k3)
# y_(n+1) = y_n + h*(k1 + 2*k2 + 2*k3 + k4)/6
#
# Reference Python Solution:
# def f(x, y):
#     return -2*x*y+x
# x = 0
# y = 1
# h = 0.25
# x_target = 1.0
# n = round((x_target - x) / h)
# for _ in range(n):
#     k1 = f(x, y)
#     k2 = f(x+h/2, y+h*k1/2)
#     k3 = f(x+h/2, y+h*k2/2)
#     k4 = f(x+h, y+h*k3)
#     y = y + h*(k1+2*k2+2*k3+k4)/6
#     x = x + h
# print(f"Approximate y(1.0) = {y:.6f}")
#
# Computed Result: y(1.0) ≈ 0.683967
#
# Answer Key:
# 1. Number of steps: n = (1.0 - 0) / 0.25 = 4 steps
# 2. First update: k1=0.000000, k2=-0.125000, k3=-0.121094, k4=-0.234863; y1=0.969706
# 3. Loop Control: Use exactly n=4 iterations
# 4. Global Accuracy: Fourth-order, error reduction ~16x
# 5. Programming Check: Validation checks

# ================================================================================
# PROBLEM 25: RUNGE-KUTTA 4TH ORDER METHOD
# ================================================================================
# Problem: Solve dy/dx = (x - y)/2, y(0) = 2
# Approximate y at x = 1.0
#
# Sample Input: x0=0, y0=2, h=0.2, x_target=1.0
# Sample Output: Approximate y(1.0) = 1.426124
#
# Method Formula:
# k1 = f(x_n, y_n)
# k2 = f(x_n + h/2, y_n + h*k1/2)
# k3 = f(x_n + h/2, y_n + h*k2/2)
# k4 = f(x_n + h, y_n + h*k3)
# y_(n+1) = y_n + h*(k1 + 2*k2 + 2*k3 + k4)/6
#
# Reference Python Solution:
# def f(x, y):
#     return (x-y)/2
# x = 0
# y = 2
# h = 0.2
# x_target = 1.0
# n = round((x_target - x) / h)
# for _ in range(n):
#     k1 = f(x, y)
#     k2 = f(x+h/2, y+h*k1/2)
#     k3 = f(x+h/2, y+h*k2/2)
#     k4 = f(x+h, y+h*k3)
#     y = y + h*(k1+2*k2+2*k3+k4)/6
#     x = x + h
# print(f"Approximate y(1.0) = {y:.6f}")
#
# Computed Result: y(1.0) ≈ 1.426124
#
# Answer Key:
# 1. Number of steps: n = (1.0 - 0) / 0.2 = 5 steps
# 2. First update: k1=-1.000000, k2=-0.900000, k3=-0.905000, k4=-0.809500; y1=1.819350
# 3. Loop Control: Use exactly n=5 iterations
# 4. Global Accuracy: Fourth-order, error reduction ~16x
# 5. Programming Check: Standard validation

# ================================================================================
# END OF DOCUMENT
# ================================================================================
# This file contains all 25 ODE numerical method problems with:
# - Problem descriptions
# - Method formulas
# - Reference Python code
# - Sample inputs and outputs
# - Exact solutions
# - Answer keys to assessment questions
#
# Methods covered:
# - Problems 1-5: Euler's Method (First-order)
# - Problems 6-10: Runge-Kutta 2nd Order - Heun's Method
# - Problems 11-15: Runge-Kutta 2nd Order - Midpoint Method
# - Problems 16-20: Runge-Kutta 2nd Order - Ralston's Method
# - Problems 21-25: Runge-Kutta 4th Order Method (Classical RK4)
# ================================================================================