from scipy.stats import norm

#mean and std dev values
mean = 10345
std_dev = 552

#new value under study
p1 = 1.0 - norm.cdf(11641, mean, std_dev)

#making use of symmetry
p2 = p1

#p-value of both tails
p_value = p1 + p2

print("2-tailed P-value",p_value)
if p_value <= .05:
    print("Passes 2-tailed test")
else:
    print("Fails 2-tailed test")