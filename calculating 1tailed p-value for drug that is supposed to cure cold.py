from scipy.stats import norm

#same stats for cold
mean = 18
std_dev = 1.5

# new drug reduced recovery to <=16 days
p_value = norm.cdf(16, mean, std_dev)

print(p_value)