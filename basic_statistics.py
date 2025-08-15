import pandas as pd

# Wczytanie pliku
df = pd.read_csv("data.csv")

# Statystyki dla wszystkich kolumn liczbowych
with pd.option_context('display.max_columns', None):
    print(df.describe())