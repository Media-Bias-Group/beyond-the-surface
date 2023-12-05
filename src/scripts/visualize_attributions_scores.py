"""
File to create both figures on the attribution scores
"""

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd


# Load the data
file_path = "data/biased_attributions.csv"
data = pd.read_csv(file_path)

sns.set_style("whitegrid")

# Plot the distribution of attribution scores
plt.figure(figsize=(12, 6))
sns.histplot(data["attribution"], bins=50, kde=True)
plt.title("Distribution of Attribution Scores")
plt.xlabel("Attribution Score")
plt.ylabel("Frequency")
plt.show()

# Plot the relationship between word occurrence and attribution score
plt.figure(figsize=(12, 6))
sns.scatterplot(data=data, x="count", y="attribution")
plt.title("Relationship Between Word Occurrence and Attribution Score")
plt.xlabel("Word Occurrence (Count)")
plt.ylabel("Attribution Score")
plt.show()
