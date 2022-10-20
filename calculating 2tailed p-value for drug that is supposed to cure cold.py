from scipy.stats import norm

#Cold has an 18 day recovery time mean, 1.5 std dev
mean = 18
std_dev = 1.5

#probability of 16 or less days
p1 = norm.cdf(16, mean, std_dev)

#probability of 20 or more days
p2 = 1.0 - norm.cdf(20, mean, std_dev)

#p-value of both tails
p_value = p1 + p2

print(p_value)