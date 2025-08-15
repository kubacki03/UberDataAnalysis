import pandas as pd

# Wczytanie pliku
df = pd.read_csv("data.csv")

# Dane o danych
print(df.info())

#Liczba wierszy i kolumn
print(df.shape)

# Procent wierszy z brakami
procent_pustych_wierszy = (df.isnull().any(axis=1).sum() / len(df)) * 100
print(f"{procent_pustych_wierszy:.2f}% wierszy ma co najmniej jedną pustą komórkę")


#Wyznaczenie najcześćiej nullowej kolumny
najczesciej_pusta = df.isnull().sum().idxmax()
liczba_pustych = df.isnull().sum().max()

print(f"Najczęściej pusta kolumna: '{najczesciej_pusta}' ({liczba_pustych} braków)")

end = input("Czy kontynuować? t lub n\n")
if end == "n" :
    exit(0)


#Usunięcie wierszy jeśli mają pustą komórkę
df = df.dropna(how="any")

#Zapisanie do nowego pliku
df.to_csv("cleaned_data.csv", index=False)
