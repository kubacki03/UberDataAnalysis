import numpy as np
import pandas as pd
import statsmodels.api as sm
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

import matplotlib.pyplot as plt

df = pd.read_csv("../data.csv")

df_clean = df[['Customer Rating', 'Driver Ratings']].replace([np.inf, -np.inf], np.nan).dropna()

X = df_clean[['Customer Rating']]
y = df_clean['Driver Ratings']

# Usuwamy NaN/inf
X = X.replace([np.inf, -np.inf], np.nan).dropna()
y = y[X.index]


#Wyznaczamy korelację
corr = df['Customer Rating'].corr(df['Driver Ratings'])
print(corr)

if corr < 0.3 :
    decision = input("Korelacja zbyt niska, czy kontynuować? t ? n")
    if decision == "n" :
        exit(0)


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LinearRegression()
model.fit(X_train, y_train)



# Predykcje
y_pred = model.predict(X_test)





# Linia regresji
plt.plot(X_test, y_pred, color='red', linewidth=2, label='Linia regresji')
plt.title("Regresja liniowa: Driver Ratings vs Customer Ratings")
plt.xlabel("Customer Ratings")
plt.ylabel("Driver Ratings")
plt.legend()
plt.show()


# Tworzenie modelu
X = sm.add_constant(X)
model = sm.OLS(y, X).fit()

# Pełny raport ze współczynnikami i p-value
print(model.summary())