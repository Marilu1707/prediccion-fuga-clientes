
# Predicción de Fuga de Clientes

Este proyecto permite predecir la probabilidad de que un cliente abandone una empresa utilizando un modelo de machine learning entrenado en Python y desplegado con Django. El usuario puede subir un archivo `.csv` y ver los resultados de las predicciones directamente en el navegador.

## Características

- Carga de archivos CSV vía interfaz web.
- Predicción de fuga usando un modelo entrenado previamente.
- Visualización de resultados en tabla HTML.
- Interfaz minimalista y clara.

## Requisitos

- Python 3.10 o superior
- pip (gestor de paquetes de Python)
- Virtualenv (opcional pero recomendado)

## Instalación y ejecución

### 1. Clonar el repositorio

```bash
git clone https://github.com/tu_usuario/Prediccion_Fuga_Clientes.git
cd Prediccion_Fuga_Clientes
```

### 2. Crear y activar un entorno virtual (opcional pero recomendado)

```bash
python -m venv venv
# En Windows
venv\Scripts\activate
# En Mac/Linux
source venv/bin/activate
```

### 3. Instalar las dependencias

```bash
pip install -r requirements.txt
```

### 4. Verificar que el modelo exista

La aplicación busca el modelo en la carpeta `modelo` ubicada en la raíz del proyecto. Si no existe `modelo/modelo_churn.pkl`, generalo ejecutando:

```bash
python entrenar_modelo.py
```

### 5. Ejecutar el servidor de desarrollo

```bash
python manage.py runserver
```

Abre tu navegador y accede a [http://127.0.0.1:8000](http://127.0.0.1:8000)

## Estructura del proyecto

```
Prediccion_Fuga_Clientes/
├── churn_project/
│   ├── churn_dashboard/
│   └── prediccion/
│       ├── templates/
│       │   └── home.html
│       └── static/
│           └── prediccion/
│               └── styles.css
├── modelo/
│   └── modelo_churn.pkl
├── entrenar_modelo.py
├── requirements.txt
└── manage.py
```

## Autor

Maria Lujan Massironi 
