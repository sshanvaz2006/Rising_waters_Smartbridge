import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
data = pd.read_excel("dataset/flood dataset.xlsx")

# Create histograms
data.hist(figsize=(14,10))

plt.suptitle("Histograms of Dataset", fontsize=16)

plt.tight_layout()

# Save graph
plt.savefig("images/histograms.png", dpi=300, bbox_inches="tight")

# Show graph
plt.show()