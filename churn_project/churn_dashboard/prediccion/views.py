from django.shortcuts import render
import pandas as pd
import joblib
import os

# Vista principal de la aplicación
def home(request):
    # Si el usuario envía el formulario (método POST)
    if request.method == "POST":
        # Obtenemos el archivo CSV enviado por el usuario
        archivo = request.FILES.get("archivo")

        # Verificamos que se haya subido un archivo
        if not archivo:
            return render(request, "home.html", {
                "error": "Por favor, subí un archivo CSV."
            })

        try:
            # Leemos el CSV en un DataFrame de pandas
            df = pd.read_csv(archivo)

            # Eliminamos columnas que no se usaron para entrenar el modelo
            # (evita errores al predecir)
            df = df.drop(columns=["CustomerID", "Churn"], errors="ignore")

            # Definimos la ruta donde se encuentra el modelo previamente entrenado
            modelo_path = os.path.join("modelo", "modelo_churn.pkl")

            # Verificamos que el archivo del modelo exista
            if not os.path.exists(modelo_path):
                return render(request, "home.html", {
                    "error": "El modelo no fue encontrado. Verificá que exista en /modelo/modelo_churn.pkl"
                })

            # Cargamos el modelo con joblib
            modelo = joblib.load(modelo_path)

            # Hacemos la predicción sobre los datos cargados
            predicciones = modelo.predict(df)

            # Agregamos la columna de predicción al DataFrame
            df["Fuga_Predicha"] = predicciones

            # Convertimos el resultado a HTML para mostrarlo en la web
            resultados_html = df.to_html(index=False)

            # Enviamos los resultados a la plantilla
            return render(request, "home.html", {
                "resultados": resultados_html
            })

        except Exception as e:
            # Si ocurre un error en el proceso, lo mostramos en pantalla
            return render(request, "home.html", {
                "error": f"Ocurrió un error procesando el archivo: {e}"
            })

    # Si no es un POST (solo se carga la página), renderizamos la plantilla vacía
    return render(request, "home.html")
