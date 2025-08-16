import pandas as pd


df = pd.read_csv('../data.csv')

distance_info = df['Ride Distance'].describe()

most_pop_pickup = df['Pickup Location'].mode()[0]
most_pop_drop = df['Drop Location'].mode()[0]

print(f"Najczęstsze miejsce odbioru {most_pop_pickup}")
print(f"Najczęstsze miejsce docelowe {most_pop_drop}")

most_pop_pair = df[['Pickup Location', 'Drop Location']].value_counts().idxmax()
pair_count = df[['Pickup Location', 'Drop Location']].value_counts().max()
print(df['Ride Distance'].describe())
print(f"Najczęściej występująca para to {most_pop_pair} – {pair_count} razy.")

# Konwersja kolumny na datę
df['Date'] = pd.to_datetime(df['Date'])

# Wyciągnięcie nazw dni tygodnia
df['DayOfWeek'] = df['Date'].dt.day_name()

# Zliczenie kursów per dzień tygodnia
counts = df['DayOfWeek'].value_counts()

days_order = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
counts = counts.reindex(days_order)

