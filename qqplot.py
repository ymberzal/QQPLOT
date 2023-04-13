import numpy as np
import matplotlib.pyplot as plt

# Load p-values from input file
pvals = []
with open('gwas_results.txt', 'r') as f:
    next(f)  # Skip header row
    for line in f:
        cols = line.split()
        if len(cols) >= 2:
            pvals.append(float(cols[1]))

# Calculate expected p-values
n = len(pvals)
expected = -np.log10(np.arange(1, n+1)/n)

# Plot observed vs expected p-values
plt.scatter(expected, -np.log10(sorted(pvals)), s=5)
plt.plot([0, max(expected)], [0, max(expected)], color='gray', linestyle='--')
plt.xlabel('Expected $-$log$_{10}$($p$)')
plt.ylabel('Observed $-$log$_{10}$($p$)')
plt.title('QQ Plot')
plt.show()


