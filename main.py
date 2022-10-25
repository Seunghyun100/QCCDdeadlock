import pandas as pd
import matplotlib.pyplot as plt


def calculate_fraction(n):
    fraction = (n-3)*(n-2)/(3*n*(n-1))
    return fraction


def calculate_expectation(n):
    if n == 0:
        return 0
    return n*calculate_fraction(n)


def iterate_calculation(n, number_of_shuttling):
    for _ in range(number_of_shuttling-1):
        n = calculate_expectation(n)
        if n < 3:
            return 0
    return n


def check_iteration(n):
    c = 0
    while 1:
        c += 1
        expectation_value = iterate_calculation(n, c)
        if expectation_value < 3:
            return c


def check_iterate_expectation(n):
    c = 0
    while 1:
        c += 1
        expectation_value = iterate_calculation(n, c)
        if expectation_value < 3:
            return c + 1


def plot_iteration(upper_n):
    try:
        if upper_n <= 3:
            raise ValueError
    except ValueError:
        print("upper_n have to larger than 3")

    number_of_core = list(range(4, upper_n+1))
    number_of_iteration = []
    for i in range(4, upper_n+1):
        number_of_iteration.append(check_iteration(i))

    plt.plot(number_of_core, number_of_iteration)
    plt.xlabel("number of core")
    plt.ylabel("number of shuttling")
    plt.show()


"""
plot iterations
"""
print("upper_n:")
ans = int(input())
plot_iteration(ans)


"""
calculate specific n and #shuttling
"""
# print("Number of Core:")
# number_of_core = int(input())
# print("Number of Shuttling:")
# sh = int(input())
# print(iterate_calculation(number_of_core, sh))
