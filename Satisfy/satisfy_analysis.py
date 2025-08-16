import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from sklearn.preprocessing import LabelEncoder

# Wybieramy tylko interesujące kolumny

df= pd.read_csv('../data.csv')
subset = df[['Ride Distance', 'Vehicle Type', 'Booking Value','Booking Status']].copy()

# Zamiana Vehicle Type (string) na liczby
le = LabelEncoder()
subset['Vehicle Type'] = le.fit_transform(subset['Vehicle Type'])
subset['Booking Status'] = le.fit_transform(subset['Booking Status'])
# Obliczenie korelacji
corr = subset.corr()

# Korelogram
plt.figure(figsize=(12,4))
sns.heatmap(corr, annot=True, cmap='coolwarm', center=0)
plt.title("Korelogram")
plt.show()