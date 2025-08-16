import pandas as pd
import numpy as np
import sns
from matplotlib import pyplot as plt
from matplotlib.ticker import MultipleLocator
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import LabelEncoder
df = pd.read_csv('../data.csv')

print(df['Booking Value'].describe())

counts = df["Payment Method"].value_counts()

plt.figure(figsize=(8,5))
counts.plot(kind='bar', color='skyblue', edgecolor='black')
plt.title("Rozkład metod płatności")
plt.xlabel("Metoda płatności")
plt.ylabel("Liczba kursów")
plt.xticks(rotation=45, ha='right')

plt.gca().yaxis.set_major_locator(MultipleLocator(5000))
plt.ylim(10000, counts.max() + 5000)
plt.tight_layout()
plt.show()



subset = df[['Ride Distance', 'Vehicle Type', 'Booking Value']].copy()

# Zamiana Vehicle Type (string) na liczby
le = LabelEncoder()
subset['Vehicle Type'] = le.fit_transform(subset['Vehicle Type'])

# Obliczenie korelacji
corr = subset.corr()

# Korelogram
plt.figure(figsize=(6,4))
sns.heatmap(corr, annot=True, cmap='coolwarm', center=0)
plt.title("Korelogram: Ride Distance, Vehicle Type, Booking Value")
plt.show()
