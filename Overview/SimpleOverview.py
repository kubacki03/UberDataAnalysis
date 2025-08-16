
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator
# Wczytanie pliku
df = pd.read_csv("../data.csv")

count = df["Booking ID"].count()

completed = df["Booking Status"].where(df["Booking Status"] == "Completed").count()
print("Ukończone kursy stanowią "+str(100*completed/count)+"% wszystkich kursów")

print("Średni czas przyjazdu kierowcy na miejsce: "+str(round(df["Avg VTAT"].mean(),2))+" minut")

print("Średni czas przejazdu: "+str(round(df["Avg CTAT"].mean(),2))+" minut")

vehicle_count = df["Vehicle Type"].value_counts()
vehicle_percentage = df["Vehicle Type"].value_counts()/len(df["Vehicle Type"])
print(vehicle_count)

print(vehicle_percentage)

vehicle_percentage.plot.pie(autopct='%1.1f%%', startangle=90, figsize=(6,6))
plt.title("Udział środków transportu w UBER")
plt.ylabel('')
plt.show()


customer_canceled = df["Reason for cancelling by Customer"].value_counts()
driver_canceled = df["Driver Cancellation Reason"].value_counts()


print("Łącznie anulowano kursów "+str(df["Reason for cancelling by Customer"].count()+df["Driver Cancellation Reason"].count()))

print(customer_canceled)
print(driver_canceled)


# Wykres słupkowy dla anulacji przez klienta
plt.figure(figsize=(8, 5))
customer_canceled.plot(kind='bar', color='skyblue')
plt.title("Powody anulacji przez klienta")
plt.xlabel("Powód anulacji")
plt.ylabel("Liczba kursów")
plt.xticks(rotation=45, ha='right')

plt.gca().yaxis.set_major_locator(MultipleLocator(200))

plt.tight_layout()
plt.show()

# Wykres słupkowy dla anulacji przez kierowcę
plt.figure(figsize=(8, 5))
driver_canceled.plot(kind='bar', color='salmon')
plt.title("Powody anulacji przez kierowcę")
plt.xlabel("Powód anulacji")
plt.ylabel("Liczba kursów")
plt.xticks(rotation=45, ha='right')

plt.gca().yaxis.set_major_locator(MultipleLocator(500))

plt.tight_layout()
plt.show()
