## Number of pets each person has

sample = [0, 1, 5, 7, 3, 9, 10, 14]

def median(values):
    ordered = sorted(values)
    print(ordered)
    n = len(ordered)
    mid = int(n / 2) - 1 if n % 2 == 0 else int(n / 2)
    
    if n % 2 == 0:
        return (ordered[mid] + ordered[mid + 1]) / 2
    else:
        return ordered[mid]
print(median(sample)) 