from scipy.stats import norm

#Cold has an 18 day recovery time mean, 1.5 std dev
mean = 18
std_dev = 1.5

#95% probability recovery time takes between 15 and 21 days.
x = norm.cdf(21, mean, std_dev) - norm.cdf(15, mean, std_dev)

print(x)