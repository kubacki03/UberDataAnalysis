import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("../data.csv")
# Konwersja kolumny Time na obiekt datetime i wyciągnięcie godzin
df['Hour'] = pd.to_datetime(df['Time'], format='%H:%M:%S').dt.hour

# Funkcja przypisująca przedziały godzinowe
def categorize_hour(h):
    if 6 <= h < 14:
        return '6-14'
    elif 14 <= h < 22:
        return '14-22'
    else:
        return '22-6'

df['HourRange'] = df['Hour'].apply(categorize_hour)

# Zliczenie kursów w przedziałach
counts = df['HourRange'].value_counts()

# Wykres kołowy
counts.plot.pie(autopct='%1.1f%%', startangle=90, figsize=(6,6))
plt.title("Rozkład kursów w przedziałach godzinowych")
plt.ylabel('')
plt.show()

# Wypisanie przedziału z największą liczbą kursów
max_range = counts.idxmax()
max_value = counts.max()
print(f"Najwięcej kursów zamówiono w przedziale {max_range} – {max_value} kursów.")
