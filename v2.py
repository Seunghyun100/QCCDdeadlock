import math
import matplotlib.pyplot as plt


def calculate_prob(n, s):
    prob = math.comb(n, 2*s)*math.factorial(2*s)/n**(2*s)
    prob = prob*math.factorial(s)*(2**s)/math.factorial(2*s)
    return prob


def check_shuttling_limit(n, prob_lower_bound):
    number_of_shuttling = 0
    while 1:
        number_of_shuttling += 1
        prob = calculate_prob(n, number_of_shuttling)
        if prob < prob_lower_bound:
            return number_of_shuttling - 1


def plot_prob(n, s_upper_bound):
    try:
        if n <= 3:
            raise ValueError
    except ValueError:
        print("n have to larger than 3")

    number_of_shuttling = list(range(2, s_upper_bound+1))
    prob = []
    for i in range(2, s_upper_bound+1):
        prob.append(calculate_prob(n, i))

    plt.plot(number_of_shuttling, prob, label=n)
    plt.xlabel("number of shuttling")
    plt.ylabel("probability")
    plt.legend()
    plt.show()


def plot_no_shuttling(n_upper_bound, prob_lower_bound):
    try:
        if n_upper_bound <= 3:
            raise ValueError
    except ValueError:
        print("n have to larger than 3")

    number_of_core = list(range(2, n_upper_bound+1))
    number_of_shuttling = []
    for i in range(2, n_upper_bound+1):
        number_of_shuttling.append(check_shuttling_limit(i, prob_lower_bound))

    l1 = str(prob_lower_bound*100) + "%"
    plt.plot(number_of_core, number_of_shuttling, label=l1)
    plt.xlabel("number of core")
    plt.ylabel("number of shuttling")
    plt.legend()
    plt.show()


"""
plot probability
"""
# print("n:")
# ans = int(input())
# print("upper_s: ")
# ans2 = int(input())
# plot_prob(ans, ans2)


"""
plot number of shuttling
"""
print("core number:")
ans = int(input())
print("probability limit: ")
ans2 = float(input())
plot_no_shuttling(ans, ans2)


"""
calculate specific n and #shuttling
"""
# print("Number of Core:")
# number_of_core = int(input())
# print("Number of Shuttling:")
# sh = int(input())
# print(calculate_prob(number_of_core, sh))
