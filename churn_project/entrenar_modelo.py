# Importamos las librerías necesarias
import pandas as pd # type: ignore
from sklearn.ensemble import RandomForestClassifier  # type: ignore
from sklearn.model_selection import train_test_split  # type: ignore
import joblib  # type: ignore
import os

# Cargamos el dataset desde un archivo CSV
df = pd.read_csv("churn_data.csv")

# Definimos las variables independientes (X) y la variable objetivo (y)
# Eliminamos 'CustomerID' porque no aporta a la predicción
X = df.drop(columns=["CustomerID", "Churn"])
y = df["Churn"]

# Dividimos los datos en conjunto de entrenamiento (80%) y prueba (20%)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Inicializamos el modelo Random Forest y lo entrenamos
modelo = RandomForestClassifier()
modelo.fit(X_train, y_train)

# Creamos la carpeta 'modelo' si no existe
os.makedirs("modelo", exist_ok=True)

# Guardamos el modelo entrenado como archivo .pkl para su posterior uso
joblib.dump(modelo, "modelo/modelo_churn.pkl")

# Confirmamos por consola que el modelo fue guardado correctamente
print("Modelo entrenado y guardado en /modelo/modelo_churn.pkl")
