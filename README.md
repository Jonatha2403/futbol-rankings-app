![Banner](banner.png)

# ⚽ Futbol Rankings App

Automatiza el análisis y predicción de partidos de fútbol en tiempo real con datos estadísticos de [API-Football](https://www.api-football.com/) y almacenamiento en [Supabase](https://supabase.com/).

> 📍 Este proyecto está diseñado para ayudarte a tomar decisiones de apuestas más informadas, basadas en probabilidades reales, rankings diarios y validación automática de resultados.

---

## 🧰 Requisitos

- Python 3.8 o superior
- Streamlit
- Supabase (proyecto activo)
- Clave de API-Football (plan gratuito o de pago)

---

## 📁 Estructura del Proyecto

| Archivo                    | Descripción                                                                 |
|----------------------------|-----------------------------------------------------------------------------|
| `index.html`               | Página web alojada con los resultados organizados                          |
| `backend.py`               | Script principal: descarga, calcula y guarda predicciones                   |
| `actualizar_resultados.py` | Genera archivo `resultados_validados.json` con partidos de los últimos 3 días |
| `resultados_validados.json`| Datos validados que se muestran en la web                                   |
| `app.py`                   | Panel interactivo con Streamlit                                             |
| `requirements.txt`         | Dependencias necesarias para ejecutar el sistema                            |
| `README.md`                | Esta documentación                                                          |

---

## 🚀 Instrucciones de Uso

### 🔧 1. Clona el Repositorio

```bash
git clone https://github.com/Jonatha2403/futbol-rankings-app.git
cd futbol-rankings-app
