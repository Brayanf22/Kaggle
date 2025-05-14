
from pymongo import MongoClient
import pandas as pd
from urllib.parse import quote_plus

# Construir URI de conexión
URI = f"mongodb+srv://Brayan:1033684238Bf@cluster0.m3o27.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

try:
    # Crear cliente con timeout
    client = MongoClient(URI, serverSelectionTimeoutMS=5000)

    # Verificar conexión
    client.server_info()  # Esto lanzará una excepción si falla la conexión
    print("✅ Conexión exitosa a MongoDB Atlas")

    db = client['Kaggle']
    collection = db['ETL']

except Exception as e:
    print(f"❌ Error de conexión: {e}")
    exit()

def transform_and_load(csv_path):
    """
    Lee un CSV, aplica transformaciones y carga los datos en MongoDB Atlas.
    Todas las fechas se establecen en 24/02/2025.
    """
    try:
        # Leer los datos
        try:
            df = pd.read_csv(csv_path, encoding='utf-8')
        except UnicodeDecodeError:
            df = pd.read_csv(csv_path, encoding='utf-8-sig')

        # Limpieza básica
        df.dropna(how='all', inplace=True)
        df.columns = [col.strip().lower().replace(' ', '_') for col in df.columns]

        # Transformación de fechas
        fecha_fija = '24/02/2025'

        # Actualizar cualquier campo que pueda contener fecha
        date_columns = [col for col in df.columns if 'date' in col.lower() or 'fecha' in col.lower()]
        if date_columns:
            for col in date_columns:
                df[col] = fecha_fija
        else:
            df['date'] = fecha_fija

        # Insertar en MongoDB
        records = df.to_dict('records')

        # Usar insert_many con ordered=False para evitar fallos por duplicados
        result = collection.insert_many(records, ordered=False)
        print(f"📊 Insertados {len(result.inserted_ids)} documentos correctamente")

    except Exception as e:
        print(f"⚠️ Error en el proceso ETL: {e}")

if __name__ == '__main__':
    # Verifica que la ruta sea accesible
    csv_path = "/content/drive/MyDrive/Colab Notebooks/ciencias de datos /Dataset_Malawi_National_Football_Team_Matches.csv"  # Archivo en el mismo directorio

    # Alternativa para Colab:
    # from google.colab import files
    # uploaded = files.upload()
    # csv_path = next(iter(uploaded.keys()))

    transform_and_load(csv_path)
