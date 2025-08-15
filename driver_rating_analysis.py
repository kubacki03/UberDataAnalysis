import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import shapiro, normaltest, norm

# Wczytanie pliku
df = pd.read_csv("data.csv")

col ="Driver Ratings"
data = df[col].dropna()
#Statystyki opisowe
print(df[col].describe())
print("\n")
# Moda
print("Moda:", data.mode()[0])
print("\n")
# Procentowo
print(data.value_counts(normalize=True) )
print("\n")

# Liczba braków
print("Braki:", data.isnull().sum())
print("\n")




# Histogram + KDE danych
plt.figure(figsize=(8,5))
sns.histplot(data, bins=10, kde=True, stat="density", color="skyblue", label="Dane")

# Parametry rozkładu normalnego
mu = data.mean()
sigma = data.std()

# Wygenerowanie „dzwonu” dla porównania
x = np.linspace(data.min(), data.max(), 100)
plt.plot(x, norm.pdf(x, mu, sigma), color='red', linestyle='--', label='Normalny dzwon')

plt.title("Rozkład ocen kierowców z porównaniem do normalnego dzwonu")
plt.xlabel(col)
plt.ylabel("Gęstość")
plt.legend()
plt.show()


stat, p = normaltest(data)
print('stat=%.3f, p=%.3f' % (stat, p))
print("\n")
if p > 0.05:
    print('Dane  normalne '+str(p))
else:
    print('Dane nie są normalne '+str(p))