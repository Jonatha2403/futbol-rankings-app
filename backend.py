# -*- coding: utf-8 -*-
"""
Futbol Rankings App - Backend Profesional
Versión: 1.0
Funcionalidad: Conectar con API-Football, calcular estadísticas y guardar predicciones en Supabase
Autor: Jonathan Rosado
"""

import requests
import time
import schedule
import os
from dotenv import load_dotenv
from datetime import datetime
from supabase import create_client, Client

# =============================
# 🔐 CARGAR CLAVES DESDE .env
# =============================
load_dotenv()  # Cargar variables desde .env

API_KEY = os.getenv("API_KEY")
SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

HEADERS = {
    "x-rapidapi-host": "v3.football.api-sports.io",
    "x-rapidapi-key": API_KEY
}

supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

# =============================
# 📦 FUNCIONES DE LA API
# =============================

def buscar_id_equipo(nombre_equipo):
    url = f"https://v3.football.api-sports.io/teams?search={nombre_equipo}"
    response = requests.get(url, headers=HEADERS).json()
    if response.get("results", 0) > 0:
        return response["response"][0]["team"]["id"]
    return None

def obtener_ultimos_partidos(id_equipo, cantidad=10):
    url = f"https://v3.football.api-sports.io/fixtures?team={id_equipo}&last={cantidad}"
    return requests.get(url, headers=HEADERS).json().get("response", [])

# =============================
# 📊 CÁLCULO DE ESTADÍSTICAS
# =============================

def calcular_prediccion(local, visitante):
    try:
        id_local = buscar_id_equipo(local)
        id_visitante = buscar_id_equipo(visitante)
        if not id_local or not id_visitante:
            return None

        partidos_local = obtener_ultimos_partidos(id_local)
        partidos_visitante = obtener_ultimos_partidos(id_visitante)

        total = len(partidos_local) + len(partidos_visitante)
        if total == 0:
            return None

        home_goals = sum(p["goals"]["home"] for p in partidos_local)
        away_goals = sum(p["goals"]["away"] for p in partidos_visitante)

        marcador_probable = f"{round(home_goals / len(partidos_local))}-{round(away_goals / len(partidos_visitante))}"
        btts = sum(1 for p in partidos_local + partidos_visitante if p["goals"]["home"] > 0 and p["goals"]["away"] > 0)

        return {
            "avg_home_goals": round(home_goals / len(partidos_local), 2),
            "avg_away_goals": round(away_goals / len(partidos_visitante), 2),
            "marcador_probable": marcador_probable,
            "prob_btts": round((btts / total) * 100, 2)
        }

    except Exception as e:
        print("⚠️ Error al calcular predicción:", e)
        return None

# =============================
# 🧠 GENERADOR DE RECOMENDACIÓN
# =============================

def generar_recomendacion(prob_btts):
    if prob_btts >= 70:
        return "Ambos Marcan (BTTS)"
    elif prob_btts >= 50:
        return "Posible BTTS"
    return "No recomendable"

# =============================
# 📤 GUARDAR PREDICCIÓN
# =============================

def guardar_prediccion(fixture_id, local, visitante, liga, pais, fecha):
    resultado = calcular_prediccion(local, visitante)
    if not resultado:
        print(f"❌ Sin predicción para {local} vs {visitante}")
        return

    data = {
        "fixture_id": fixture_id,
        "local": local,
        "visitante": visitante,
        "liga": liga,
        "pais": pais,
        "fecha": fecha,
        "marcador_probable": resultado["marcador_probable"],
        "avg_home_goals": resultado["avg_home_goals"],
        "avg_away_goals": resultado["avg_away_goals"],
        "prob_btts": resultado["prob_btts"],
        "recomendacion": generar_recomendacion(resultado["prob_btts"]),
        "creado_en": datetime.now().isoformat()
    }

    ya = supabase.table("predicciones").select("*").eq("fixture_id", fixture_id).execute()
    if not ya.data:
        supabase.table("predicciones").insert(data).execute()
        print(f"✅ Guardado: {local} vs {visitante} → {data['recomendacion']}")
    else:
        print(f"⚠️ Ya existe: {local} vs {visitante}")

# =============================
# 🔁 EJECUCIÓN AUTOMÁTICA
# =============================

def ejecutar_predicciones():
    partidos_ejemplo = [
        {"id": 1, "local": "Barcelona", "visitante": "Real Madrid", "liga": "La Liga", "pais": "España", "fecha": "2025-05-11"},
        {"id": 2, "local": "Arsenal", "visitante": "Liverpool", "liga": "Premier League", "pais": "Inglaterra", "fecha": "2025-05-11"}
    ]
    for p in partidos_ejemplo:
        guardar_prediccion(p["id"], p["local"], p["visitante"], p["liga"], p["pais"], p["fecha"])

# Ejecutar una vez al día a las 2:00 AM
schedule.every().day.at("02:00").do(ejecutar_predicciones)

print("🕒 Esperando tareas programadas...")
while True:
    schedule.run_pending()
    time.sleep(60)
