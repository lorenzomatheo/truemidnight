import psycopg2
from decouple import config, UndefinedValueError

# Tente imprimir as variáveis do ambiente
try:
    print("DB_NAME:", config('DB_NAME'))
    print("DB_USER:", config('DB_USER'))
    print("DB_PASSWORD:", config('DB_PASSWORD'))
    print("DB_HOST:", config('DB_HOST'))
    print("DB_PORT:", config('DB_PORT'))
except UndefinedValueError as e:
    print(f"Erro: {e}")

conn = None  # Inicializa conn como None
try:
    conn = psycopg2.connect(
        dbname=config('DB_NAME'),
        user=config('DB_USER'),
        password=config('DB_PASSWORD'),
        host=config('DB_HOST'),
        port=config('DB_PORT')
    )
    print("Conexão bem-sucedida!")
except Exception as e:
    print(f"Erro na conexão: {e}")
finally:
    if conn is not None:
        conn.close()
        print("Conexão fechada.")
