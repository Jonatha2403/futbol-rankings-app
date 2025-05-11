# -*- coding: utf-8 -*-
"""
Actualiza los resultados validados de predicciones y los guarda como JSON.
Se usa para mostrar en la web (index.html).
"""

import json
from datetime import datetime, timedelta
from supabase import create_client
from dotenv import load_dotenv
import os

# =============================
# 🔐 CARGAR VARIABLES .env
# =============================
load_dotenv()
SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

# =============================
# 📤 DESCARGAR Y GUARDAR JSON
# =============================

def generar_json_resultados():
    print("🔄 Generando resultados_validados.json...")

    fecha_limite = (datetime.now() - timedelta(days=3)).strftime("%Y-%m-%d")
    
    try:
        data = supabase.table("resultados_validados") \
            .select("*") \
            .gte("fecha", fecha_limite) \
            .execute().data

        if not data:
            print("⚠️ No se encontraron resultados validados.")
            return

        with open("resultados_validados.json", "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4, ensure_ascii=False)

        print("✅ Archivo actualizado correctamente.")

    except Exception as e:
        print("❌ Error al generar JSON:", e)

# =============================
# ▶️ EJECUCIÓN DIRECTA
# =============================
if __name__ == "__main__":
    generar_json_resultados()
