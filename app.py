import streamlit as st
from supabase import create_client
from datetime import datetime, timedelta
import pandas as pd

# 🛠️ Configura tus claves de Supabase
SUPABASE_URL = "https://tu-url.supabase.co"
SUPABASE_KEY = "tu-api-key"
supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

st.set_page_config(page_title="Futbol Rankings App", layout="wide")
st.title("⚽ Futbol Rankings App")
st.markdown("### 📊 Análisis predictivo y resultados validados en tiempo real")

# ===============================
# Función: Mostrar predicciones
# ===============================
def mostrar_predicciones():
    st.subheader("📅 Partidos Próximos con Predicciones")
    predicciones = supabase.table("partidos").select("*").order("fixture_date").execute().data

    if not predicciones:
        st.warning("No hay predicciones disponibles.")
        return

    df = pd.DataFrame(predicciones)
    df['fixture_date'] = pd.to_datetime(df['fixture_date'])
    df = df[df['status'] == "NS"]
    grouped = df.groupby(['country', 'league_id'])

    for (pais, liga), group in grouped:
        st.markdown(f"#### {pais} - {group['league_id'].iloc[0]}")
        st.dataframe(group[[
            'home_team', 'away_team', 'fixture_date',
            'marcador_probable', 'prob_btts', 'recomendacion'
        ]].rename(columns={
            'home_team': 'Local',
            'away_team': 'Visitante',
            'fixture_date': 'Fecha',
            'marcador_probable': 'Marcador Probable',
            'prob_btts': 'Probabilidad BTTS',
            'recomendacion': 'Recomendación'
        }), use_container_width=True)

# ===============================
# Función: Mostrar rankings
# ===============================
def mostrar_rankings():
    st.subheader("🏆 Rankings de Apuestas (TOP 10)")
    tipos = ['BTTS', 'LOCAL', 'VISITA']

    for tipo in tipos:
        st.markdown(f"##### {tipo}")
        data = supabase.table("rankings_apuestas").select("*").eq("tipo", tipo).order("probabilidad", desc=True).limit(10).execute().data
        if not data:
            st.info("Sin datos disponibles.")
            continue

        df = pd.DataFrame(data)
        st.dataframe(df[[
            'home_team', 'away_team', 'fixture_date',
            'probabilidad', 'marcador_probable', 'recomendacion'
        ]].rename(columns={
            'home_team': 'Local',
            'away_team': 'Visitante',
            'fixture_date': 'Fecha',
            'probabilidad': 'Probabilidad',
            'marcador_probable': 'Marcador',
            'recomendacion': 'Recomendación'
        }), use_container_width=True)

# ===============================
# Función: Mostrar resultados validados
# ===============================
def mostrar_resultados_validados():
    st.subheader("✅ Resultados de Predicciones (últimos 3 días)")
    fecha_limite = (datetime.now() - timedelta(days=3)).isoformat()
    data = supabase.table("resultados_validados").select("*").gte("fecha", fecha_limite).execute().data

    if not data:
        st.warning("No hay resultados validados disponibles.")
        return

    df = pd.DataFrame(data)
    resumen = {
        "aciertos": df[df["acierto"] == True].shape[0],
        "errores": df[df["acierto"] == False].shape[0]
    }

    st.markdown(f"**✅ Aciertos:** {resumen['aciertos']}  |  **❌ Errores:** {resumen['errores']}")

    for (pais, liga), group in df.groupby(['pais', 'liga']):
        st.markdown(f"#### {pais} - {liga}")
        st.dataframe(group[[
            'fecha', 'local', 'visitante',
            'marcador_real', 'prediccion', 'acierto'
        ]].rename(columns={
            'fecha': 'Fecha',
            'local': 'Local',
            'visitante': 'Visitante',
            'marcador_real': 'Marcador',
            'prediccion': 'Predicción',
            'acierto': '¿Acierto?'
        }), use_container_width=True)

# ===============================
# Navegación
# ===============================
menu = st.sidebar.radio("📌 Navegación", ["🏠 Inicio", "📅 Predicciones", "🏆 Rankings", "📈 Resultados"])

if menu == "🏠 Inicio":
    st.image("banner.png", use_column_width=True)
    st.markdown("Automatiza tu estrategia de apuestas con estadísticas reales y predicciones inteligentes.")
elif menu == "📅 Predicciones":
    mostrar_predicciones()
elif menu == "🏆 Rankings":
    mostrar_rankings()
elif menu == "📈 Resultados":
    mostrar_resultados_validados()
