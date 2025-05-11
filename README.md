![Banner](banner.png)

# ⚽ Futbol Rankings App

Automatiza el análisis y predicción de partidos de fútbol en tiempo real utilizando datos estadísticos de [API-Football](https://www.api-football.com/) y almacenamiento dinámico en [Supabase](https://supabase.com/).

> 📍 Este proyecto está diseñado para ayudarte a tomar decisiones de apuestas más informadas, con rankings diarios, validación automática de resultados y visualización profesional en Streamlit y GitHub Pages.

---

## 🧰 Requisitos

- Python 3.8 o superior
- [API-Football](https://www.api-football.com/) (clave gratuita o de pago)
- Supabase (proyecto activo y tabla `partidos`, `rankings_apuestas`, `resultados_validados`)
- Git y GitHub Pages (para hosting del sitio web)
- Streamlit (para panel interactivo)

---

## 📁 Estructura del Proyecto

| Archivo                    | Descripción                                                                 |
|---------------------------|-----------------------------------------------------------------------------|
| `index.html`              | Página principal del proyecto para GitHub Pages con resultados en vivo     |
| `backend.py`              | Script que consulta API-Football, calcula probabilidades y sube a Supabase |
| `app.py`                  | Dashboard interactivo con Streamlit para visualización en tiempo real       |
| `actualizar_resultados.py`| Generador automático de archivo JSON para la web con resultados validados  |
| `resultados_validados.json`| Archivo generado con predicciones acertadas o fallidas                     |
| `requirements.txt`        | Lista de librerías necesarias para instalar el entorno                      |
| `test_supabase.py`        | Script de prueba para validar conexión a Supabase                           |
| `.env`                    | Claves privadas de API-Football y Supabase (NO subir al repositorio)       |
| `README.md`               | Instrucciones del proyecto                                                  |

---

## 🚀 Instrucciones de Uso

### 🔧 1. Clona el Repositorio

```bash
git clone https://github.com/Jonatha2403/futbol-rankings-app.git
cd futbol-rankings-app
```

### 🧪 2. Instala las Dependencias

```bash
pip install -r requirements.txt
```

### 🔐 3. Configura las claves en `.env`

```env
API_KEY=tu-api-key-de-api-football
SUPABASE_URL=https://tuproyecto.supabase.co
SUPABASE_KEY=clave-de-tu-proyecto-supabase
```

### ⚙️ 4. Ejecuta el Sistema

- **Para cargar partidos y subir predicciones:**
```bash
python backend.py
```

- **Para generar archivo JSON de resultados validados:**
```bash
python actualizar_resultados.py
```

- **Para ver el dashboard:**
```bash
streamlit run app.py
```

---

## 🌐 Web Pública

Puedes ver los resultados validados en tiempo real desde tu GitHub Pages:

📍 `https://[TU-USUARIO].github.io/futbol-rankings-app/`

---

## 🛡️ Licencia y Derechos de Autor

Este proyecto está protegido por derechos de autor.

- ❌ Prohibido copiar, redistribuir o modificar sin autorización escrita del autor.
- ❌ Prohibido usar este código para crear productos derivados o comerciales sin suscripción.
- ✅ Permitido para suscriptores con licencia activa.

© 2025 Jonathan Rosado. Todos los derechos reservados.

---

¿Dudas o sugerencias? [Contáctanos por WhatsApp](https://wa.me/593958757302)
