# score_stats.py - quiz score summary
import numpy as np

x = np.array([87.5, 91.0, 78.5, 84.0, 95.5, 88.0])  # quiz scores
print(f"mean score: {x.mean():.4f}")

print(f"std dev: {x.std(ddof=1):.4f}")
print(f"max score: {x.max():.4f}")