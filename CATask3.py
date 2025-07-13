import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("sample_quotes_dataset (1).csv")

print(" Sample Data:")
print(df.head())

author_counts = df['Author'].value_counts()

print("\n Number of Quotes by Each Author:")
print(author_counts)

plt.figure(figsize=(8, 5))
sns.barplot(x=author_counts.index, y=author_counts.values, palette="Set2")

plt.title("Number of Quotes per Author")
plt.xlabel("Author")
plt.ylabel("Quote Count")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
