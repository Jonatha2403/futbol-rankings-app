# -*- coding: utf-8 -*-
"""
Verifica la conexión a Supabase usando las claves de .env
"""

from supabase import create_client
from dotenv import load_dotenv
import os

# =============================
# 🔐 CARGAR VARIABLES .env
# =============================
load_dotenv()
SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

# =============================
# 🔌 CONEXIÓN Y VERIFICACIÓN
# =============================

def probar_conexion():
    try:
        supabase = create_client(SUPABASE_URL, SUPABASE_KEY)
        resultado = supabase.table("ligas").select("*").limit(1).execute()
        
        if resultado.data:
            print("✅ Conexión exitosa a Supabase. Datos obtenidos:")
            print(resultado.data)
        else:
            print("⚠️ Conexión realizada, pero no hay datos en la tabla 'ligas'.")

    except Exception as e:
        print("❌ Error al conectar con Supabase:")
        print(e)

# =============================
# ▶️ EJECUCIÓN
# =============================
if __name__ == "__main__":
    probar_conexion()
