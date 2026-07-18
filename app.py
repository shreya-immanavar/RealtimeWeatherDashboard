import streamlit as st
import requests
import pandas as pd
from datetime import datetime, timedelta
import os
import io

# -----------------------------
# Configuration & Setup
# -----------------------------
st.set_page_config(
    page_title="Weather Analytics Dashboard",
    page_icon="🌤️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# -----------------------------
# Weather-Themed CSS Injection
# -----------------------------
st.markdown("""
<style>
    /* Google Fonts */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap');

    /* Global Theme */
    html, body {
        font-family: 'Inter', sans-serif;
        color: #E2E8F0;
    }
    * {
        box-sizing: border-box;
    }

    /* ============================================
       ANIMATED SKY BACKGROUND
    ============================================ */
    .stApp {
        background: linear-gradient(135deg, #0a0f1e 0%, #0d1b35 25%, #0f2444 50%, #0a1628 75%, #060d1a 100%) !important;
        min-height: 100vh;
    }

    /* ============================================
       HIDE DEFAULT ELEMENTS
    ============================================ */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {background-color: transparent !important;}
    [data-testid="stHeaderActionElements"] {display: none;}
    [data-testid="stDecoration"] {display: none;}

    /* ============================================
       LAYOUT
    ============================================ */
    .block-container {
        padding-top: 1.5rem !important;
        padding-bottom: 3rem !important;
        max-width: 98% !important;
    }

    /* ============================================
       GLASSMORPHISM KPI CARDS
    ============================================ */
    [data-testid="metric-container"] {
        background: linear-gradient(135deg, rgba(30,41,59,0.9) 0%, rgba(15,23,42,0.9) 100%) !important;
        border: 1px solid rgba(56,189,248,0.25) !important;
        border-top: 2px solid rgba(56,189,248,0.6) !important;
        border-radius: 16px !important;
        padding: 1.2rem 1.4rem !important;
        box-shadow: 0 8px 32px rgba(0,0,0,0.4) !important;
        transition: transform 0.3s ease !important;
    }
    [data-testid="metric-container"]:hover {
        transform: translateY(-4px);
        box-shadow: 0 16px 40px rgba(0,0,0,0.5) !important;
    }
    [data-testid="stMetricLabel"] { color: #94A3B8 !important; font-size: 0.78rem !important; font-weight: 600 !important; text-transform: uppercase !important; letter-spacing: 1px !important; }
    [data-testid="stMetricValue"] { color: #38BDF8 !important; font-size: 1.7rem !important; font-weight: 800 !important; }
    [data-testid="stMetricDelta"] { color: #22C55E !important; }

    /* ============================================
       SECTION HEADERS
    ============================================ */
    .section-title {
        font-size: 0.85rem;
        font-weight: 700;
        color: #38BDF8;
        text-transform: uppercase;
        letter-spacing: 2px;
        padding: 0.6rem 1rem;
        background: linear-gradient(90deg, rgba(56,189,248,0.12) 0%, transparent 100%);
        border-left: 3px solid #38BDF8;
        border-radius: 0 8px 8px 0;
        margin-top: 2rem;
        margin-bottom: 1.2rem;
        display: flex;
        align-items: center;
        gap: 0.6rem;
    }
    hr {
        border: none;
        border-top: 1px solid rgba(51,65,85,0.5) !important;
        margin: 1.5rem 0;
    }

    /* ============================================
       ALERT CARDS
    ============================================ */
    .alert-card {
        background: linear-gradient(135deg, rgba(30,41,59,0.9) 0%, rgba(15,23,42,0.9) 100%);
        border: 1px solid rgba(51,65,85,0.5);
        border-radius: 14px;
        padding: 1.2rem 1.5rem;
        display: flex;
        align-items: center;
        gap: 1rem;
        box-shadow: 0 4px 16px rgba(0,0,0,0.3);
        transition: transform 0.2s ease;
        margin-bottom: 0.5rem;
    }
    .alert-card:hover { transform: translateY(-2px); }
    .alert-card.error   { border-left: 4px solid #EF4444; }
    .alert-card.warning { border-left: 4px solid #F59E0B; }
    .alert-card.success { border-left: 4px solid #22C55E; }
    .alert-card.info    { border-left: 4px solid #38BDF8; }

    /* ============================================
       INSIGHT CARDS
    ============================================ */
    .insight-card {
        background: linear-gradient(135deg, rgba(30,41,59,0.9) 0%, rgba(15,23,42,0.9) 100%);
        border: 1px solid rgba(56,189,248,0.18);
        border-radius: 14px;
        padding: 1.2rem 1.4rem;
        color: #CBD5E1;
        font-size: 0.95rem;
        font-weight: 500;
        display: flex;
        align-items: flex-start;
        gap: 0.9rem;
        height: 100%;
        box-shadow: 0 4px 16px rgba(0,0,0,0.2);
        transition: transform 0.2s ease;
    }
    .insight-card:hover { transform: translateY(-2px); }
    .insight-icon { font-size: 1.6rem; min-width: 2rem; text-align: center; }

    /* ============================================
       CHART CONTAINERS
    ============================================ */
    .chart-container {
        background: linear-gradient(135deg, rgba(30,41,59,0.9) 0%, rgba(15,23,42,0.9) 100%);
        padding: 1.5rem;
        border-radius: 16px;
        border: 1px solid rgba(56,189,248,0.15);
        box-shadow: 0 8px 24px rgba(0,0,0,0.3);
        margin-bottom: 1rem;
    }

    /* ============================================
       SIDEBAR
    ============================================ */
    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, #0a0f1e 0%, #0d1b35 50%, #0a1628 100%) !important;
        border-right: 1px solid rgba(56,189,248,0.15) !important;
    }

    /* ============================================
       INPUTS & SELECTBOXES
    ============================================ */
    [data-testid="stTextInput"] input {
        background-color: rgba(15,23,42,0.9) !important;
        color: #F1F5F9 !important;
        border: 1px solid rgba(56,189,248,0.25) !important;
        border-radius: 8px !important;
    }
    [data-testid="stTextInput"] input:focus {
        border-color: #38BDF8 !important;
        box-shadow: 0 0 0 2px rgba(56,189,248,0.2) !important;
    }

    /* ============================================
       BUTTONS
    ============================================ */
    .stButton > button {
        background: linear-gradient(135deg, #0284C7, #0EA5E9) !important;
        color: #F8FAFC !important;
        border: none !important;
        border-radius: 8px !important;
        font-weight: 600 !important;
        font-size: 0.875rem !important;
        width: 100%;
        box-shadow: 0 4px 12px rgba(14,165,233,0.3);
        transition: all 0.25s ease;
    }
    .stButton > button:hover {
        background: linear-gradient(135deg, #0369A1, #0284C7) !important;
        transform: translateY(-2px);
        box-shadow: 0 8px 20px rgba(14,165,233,0.4);
    }

    /* ============================================
       DOWNLOAD BUTTONS
    ============================================ */
    .stDownloadButton > button {
        background: linear-gradient(135deg, rgba(30,41,59,0.9), rgba(15,23,42,0.9)) !important;
        color: #38BDF8 !important;
        border: 1px solid rgba(56,189,248,0.35) !important;
        border-radius: 8px !important;
        font-weight: 600 !important;
        width: 100%;
        transition: all 0.2s ease;
    }
    .stDownloadButton > button:hover {
        background: rgba(56,189,248,0.12) !important;
        border-color: #38BDF8 !important;
        transform: translateY(-1px);
    }

    /* ============================================
       BANNER ALERT
    ============================================ */
    .banner-alert {
        border-radius: 12px;
        margin-bottom: 1.5rem;
        display: flex;
        align-items: center;
        gap: 1.2rem;
        padding: 1rem 1.5rem;
        box-shadow: 0 8px 24px rgba(0,0,0,0.3);
        backdrop-filter: blur(16px);
        -webkit-backdrop-filter: blur(16px);
        animation: slideDown 0.5s ease-out;
    }
    @keyframes slideDown {
        from { opacity: 0; transform: translateY(-20px); }
        to   { opacity: 1; transform: translateY(0); }
    }

    /* ============================================
       WEATHER STAT BADGE
    ============================================ */
    .weather-badge {
        display: inline-flex;
        align-items: center;
        gap: 6px;
        background: rgba(56,189,248,0.1);
        border: 1px solid rgba(56,189,248,0.25);
        border-radius: 20px;
        padding: 4px 12px;
        font-size: 0.8rem;
        font-weight: 600;
        color: #38BDF8;
    }

    /* ============================================
       TOAST POPUP
    ============================================ */
    div[data-testid="stToastContainer"] {
        top: 30px !important;
        bottom: auto !important;
        left: 50% !important;
        transform: translateX(-50%) !important;
        right: auto !important;
        display: flex;
        flex-direction: column;
        align-items: center;
        z-index: 999999 !important;
        width: auto !important;
        max-width: 800px !important;
    }
    div[data-testid="stToast"] {
        background: linear-gradient(135deg, #1a0a00, #2d1200) !important;
        border: 3px solid #F59E0B !important;
        border-radius: 16px !important;
        padding: 2rem 4rem !important;
        box-shadow: 0 0 40px rgba(245,158,11,0.5), 0 0 80px rgba(245,158,11,0.2) !important;
        min-width: 600px !important;
        backdrop-filter: blur(20px);
    }
    div[data-testid="stToast"] .stMarkdown p {
        font-size: 1.8rem !important;
        font-weight: 800 !important;
        color: #FCD34D !important;
        text-align: center !important;
    }
    /* ============================================
       ANIMATIONS
    ============================================ */
    @keyframes fadeInUp {
        from { opacity: 0; transform: translateY(20px); }
        to   { opacity: 1; transform: translateY(0); }
    }
    div.block-container {
        animation: fadeInUp 0.5s ease-out;
    }

    /* Headers */
    h1, h2, h3, h4, h5 {
        color: #F1F5F9 !important;
        font-weight: 700 !important;
    }
</style>
""", unsafe_allow_html=True)

API_KEY = "abf8b703de5958ddf864cbd489f66ee3"
DATA_FILE = "weather_data.csv"

# Initialize Session State
if "missing_values_prevented" not in st.session_state:
    st.session_state.missing_values_prevented = 0
if "duplicates_removed" not in st.session_state:
    st.session_state.duplicates_removed = 0
if "last_updated" not in st.session_state:
    st.session_state.last_updated = "Never"

# -----------------------------
# Helper Functions (Backend strictly intact)
# -----------------------------
@st.cache_data(ttl=60)
def fetch_weather_data(city: str, api_key: str):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    try:
        response = requests.get(url, timeout=10)
        if response.status_code == 200:
            return response.json(), None
        elif response.status_code == 404:
            return None, f"City '{city}' not found."
        else:
            return None, f"API Error: {response.status_code}"
    except requests.exceptions.RequestException as e:
        return None, f"Network Error: {e}"

def process_weather_data(data, city: str) -> dict:
    main_data = data.get("main", {})
    wind_data = data.get("wind", {})
    weather_data = data.get("weather", [{}])[0] if data.get("weather") else {}

    temp = round(float(main_data.get("temp", 0.0)), 2)
    humidity = round(float(main_data.get("humidity", 0.0)), 2)
    pressure = round(float(main_data.get("pressure", 0.0)), 2)
    wind_speed = round(float(wind_data.get("speed", 0.0)), 2)
    feels_like = round(float(main_data.get("feels_like", 0.0)), 2)

    visibility_m = data.get("visibility", 0)
    visibility_km = round(float(visibility_m) / 1000.0, 2)

    weather_desc = str(weather_data.get("main", "Unknown")).title()
    std_city = str(city).strip().title()
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    return {
        "Timestamp": timestamp,
        "City": std_city,
        "Temperature": temp,
        "Humidity": humidity,
        "Pressure": pressure,
        "Wind Speed": wind_speed,
        "Weather": weather_desc,
        "Feels Like": feels_like,
        "Visibility (km)": visibility_km
    }

def save_weather_data(record, file_path):
    df = pd.DataFrame([record])
    numeric_cols = ["Temperature", "Humidity", "Pressure", "Wind Speed", "Feels Like", "Visibility (km)"]
    for col in numeric_cols:
        df[col] = pd.to_numeric(df[col], errors="coerce")

    initial_len = len(df)
    df = df.dropna()
    st.session_state.missing_values_prevented += (initial_len - len(df))

    if os.path.exists(file_path):
        try:
            old_df = pd.read_csv(file_path)
            df = pd.concat([old_df, df], ignore_index=True)
        except Exception:
            pass

    len_before_dedup = len(df)
    df = df.drop_duplicates(subset=["Timestamp", "City"], keep="last")
    st.session_state.duplicates_removed += (len_before_dedup - len(df))

    df.to_csv(file_path, index=False)
    st.session_state.last_updated = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def load_history(file_path: str) -> pd.DataFrame:
    if not os.path.exists(file_path):
        return pd.DataFrame()
    try:
        return pd.read_csv(file_path)
    except Exception:
        return pd.DataFrame()

def apply_filters(df: pd.DataFrame, city_filter, date_filter, weather_filter) -> pd.DataFrame:
    if df.empty:
        return df
    df["Timestamp"] = pd.to_datetime(df["Timestamp"], errors="coerce")
    if city_filter != "All Cities":
        df = df[df["City"].str.lower() == city_filter.lower()]
    if weather_filter != "All Conditions":
        df = df[df["Weather"] == weather_filter]

    now = datetime.now()
    if date_filter == "Today":
        df = df[df["Timestamp"].dt.date == now.date()]
    elif date_filter == "Last 24 Hours":
        df = df[df["Timestamp"] >= (now - timedelta(hours=24))]
    elif date_filter == "Last 7 Days":
        df = df[df["Timestamp"] >= (now - timedelta(days=7))]
    return df

def get_excel_download(df):
    output = io.BytesIO()
    with pd.ExcelWriter(output, engine='openpyxl') as writer:
        df.to_excel(writer, index=False, sheet_name='Weather Data')
    return output.getvalue()

def get_weather_emoji(condition: str) -> str:
    condition = condition.lower()
    if "thunder" in condition: return "⛈️"
    if "rain" in condition or "drizzle" in condition: return "🌧️"
    if "snow" in condition: return "❄️"
    if "cloud" in condition: return "☁️"
    if "mist" in condition or "fog" in condition or "haze" in condition: return "🌫️"
    if "clear" in condition: return "☀️"
    return "🌤️"

# -----------------------------
# Main Application UI
# -----------------------------
def main():
    raw_history_df = load_history(DATA_FILE)

    # ============================================================
    # WEATHER-THEMED SIDEBAR
    # ============================================================
    with st.sidebar:
        st.markdown("""
        <div style='text-align:center; padding: 1rem 0 0.5rem 0;'>
            <div style='font-size:3rem; filter: drop-shadow(0 0 10px rgba(56,189,248,0.5));'>🌤️</div>
            <div style='color: #F1F5F9; font-size: 1.1rem; font-weight: 700; letter-spacing: 1px;'>Weather Analytics</div>
            <div style='color: #64748B; font-size: 0.75rem; margin-top: 2px;'>Real-Time Intelligence</div>
        </div>
        <hr style='border-color: rgba(56,189,248,0.15); margin: 0.8rem 0;'>
        """, unsafe_allow_html=True)

        with st.expander("🔍 Search & Settings", expanded=True):
            city_input = st.text_input("City Search", "London", help="Enter a city name to fetch live weather")
            st.selectbox("Country", ["Global", "US", "UK", "IN", "JP"])
            st.selectbox("Temperature Unit", ["Celsius (°C)", "Fahrenheit (°F)"])
            refresh_interval = st.selectbox("Auto-Refresh", ["60 seconds", "2 minutes", "5 minutes"])

        refresh_ms = 60000
        if "2" in refresh_interval: refresh_ms = 120000
        if "5" in refresh_interval: refresh_ms = 300000
        # JS-based auto-refresh (compatible with all Streamlit versions)
        st.markdown(f"""
        <script>
            setTimeout(function() {{ window.location.reload(); }}, {refresh_ms});
        </script>
        """, unsafe_allow_html=True)

        with st.expander("🎛️ Filters", expanded=True):
            available_cities = ["All Cities"] + sorted(raw_history_df["City"].dropna().unique().tolist()) if not raw_history_df.empty else ["All Cities"]
            available_weather = ["All Conditions"] + sorted(raw_history_df["Weather"].dropna().unique().tolist()) if not raw_history_df.empty else ["All Conditions"]

            city_filter = st.selectbox("Filter by City", available_cities,
                index=available_cities.index(city_input.title()) if city_input.title() in available_cities else 0)
            date_filter = st.selectbox("Date Range", ["All Data", "Today", "Last 24 Hours", "Last 7 Days"])
            weather_filter = st.selectbox("Condition", available_weather)

        with st.expander("💾 Export Data", expanded=False):
            filtered_export_df = apply_filters(raw_history_df, city_filter, date_filter, weather_filter)
            if not filtered_export_df.empty:
                filtered_export_df["Timestamp"] = filtered_export_df["Timestamp"].dt.strftime("%Y-%m-%d %H:%M:%S")
                st.download_button(label="📄 Export as CSV",
                    data=filtered_export_df.to_csv(index=False),
                    file_name="weather_data.csv", mime="text/csv")
                st.markdown("<div style='height:6px;'></div>", unsafe_allow_html=True)
                st.download_button(label="📊 Export as Excel",
                    data=get_excel_download(filtered_export_df),
                    file_name="weather_data.xlsx",
                    mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")
            else:
                st.markdown("<div style='color:#64748B; font-size:0.85rem; text-align:center; padding:0.5rem;'>No data to export.</div>", unsafe_allow_html=True)

        # Sidebar footer
        st.markdown(f"""
        <div style='position:absolute; bottom:1rem; left:0; right:0; text-align:center;'>
            <div style='color: #1E3A5F; font-size: 0.7rem;'>Last Sync: {st.session_state.last_updated}</div>
        </div>
        """, unsafe_allow_html=True)

    # ============================================================
    # TOP HEADER
    # ============================================================
    h1, h2, h3 = st.columns([2, 1, 1])
    with h1:
        st.markdown("""
        <div style='padding-top: 4px;'>
            <div style='color: #94A3B8; font-size: 0.75rem; font-weight: 600; text-transform: uppercase; letter-spacing: 2px; margin-bottom: 4px;'>Real-Time Analytics Platform</div>
            <h1 style='color: #F8FAFC; font-weight: 800; font-size: 2rem; margin: 0; line-height: 1;'>
                🌍 Weather Intelligence Hub
            </h1>
        </div>
        """, unsafe_allow_html=True)
    with h2:
        now = datetime.now()
        st.markdown(f"""
        <div style='text-align:right; padding-top: 14px;'>
            <div style='color: #F1F5F9; font-size: 1.4rem; font-weight: 700;'>{now.strftime('%I:%M %p')}</div>
            <div style='color: #64748B; font-size: 0.8rem;'>{now.strftime('%A, %B %d, %Y')}</div>
        </div>
        """, unsafe_allow_html=True)
    with h3:
        st.markdown(f"""
        <div style='display:flex; justify-content:flex-end; align-items:center; gap:12px; padding-top:12px;'>
            <div style='text-align:right;'>
                <div style='color: #64748B; font-size: 0.7rem; text-transform:uppercase; letter-spacing:1px;'>Last Updated</div>
                <div style='color: #CBD5E1; font-size: 0.85rem; font-weight:600;'>{st.session_state.last_updated}</div>
            </div>
            <div style='background: rgba(34,197,94,0.12); color: #22C55E; border: 1px solid rgba(34,197,94,0.3); padding: 8px 14px; border-radius: 20px; font-size: 0.75rem; font-weight: 700; display:flex; align-items:center; gap:6px;'>
                <div style='width:8px; height:8px; background:#22C55E; border-radius:50%; box-shadow: 0 0 8px #22C55E; animation: pulse 2s infinite;'></div>
                LIVE
            </div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("<hr>", unsafe_allow_html=True)

    if not city_input.strip():
        st.warning("⚡ Enter a city name in the sidebar to begin live weather tracking.")
        return

    # Fetch Data
    with st.spinner(f"🛰️ Fetching live weather data for {city_input}..."):
        raw_data, error_msg = fetch_weather_data(city_input, API_KEY)

    if error_msg:
        st.error(f"🌐 {error_msg}")
        return

    if raw_data:
        record = process_weather_data(raw_data, city_input)
        save_weather_data(record, DATA_FILE)
        raw_history_df = load_history(DATA_FILE)

        temp = record['Temperature']
        weather = record['Weather']
        weather_emoji = get_weather_emoji(weather)

        # ============================================================
        # BANNER + TOAST ALERTS
        # ============================================================
        banner_msg = None
        banner_color = None
        banner_bg = None
        banner_icon = None

        if temp > 35:
            banner_msg = f"EXTREME HEAT WARNING — Temperatures in {record['City']} exceed 35°C. Stay hydrated and avoid direct sunlight."
            banner_color = "#EF4444"
            banner_bg = "rgba(239,68,68,0.08)"
            banner_icon = "🔥"
        elif weather == "Thunderstorm":
            banner_msg = f"SEVERE THUNDERSTORM WARNING — Dangerous conditions detected in {record['City']}. Seek shelter immediately."
            banner_color = "#EF4444"
            banner_bg = "rgba(239,68,68,0.08)"
            banner_icon = "⛈️"
        elif temp < 0:
            banner_msg = f"FREEZING CONDITIONS — Temperatures in {record['City']} are below 0°C. Black ice and frost hazard."
            banner_color = "#38BDF8"
            banner_bg = "rgba(56,189,248,0.08)"
            banner_icon = "❄️"

        if banner_msg:
            st.toast(banner_msg, icon=banner_icon)
            st.markdown(f"""
            <div style='background:{banner_bg}; border:1px solid {banner_color}30; border-left:5px solid {banner_color};
                        padding:1rem 1.5rem; border-radius:12px; margin-bottom:1.5rem;
                        display:flex; align-items:center; gap:1.2rem;
                        box-shadow: 0 4px 20px {banner_color}20;
                        animation: slideDown 0.5s ease-out;'>
                <div style='font-size:2.2rem; filter:drop-shadow(0 0 8px {banner_color});'>{banner_icon}</div>
                <div>
                    <div style='color:{banner_color}; font-weight:800; font-size:0.8rem; text-transform:uppercase; letter-spacing:2px; margin-bottom:4px;'>⚠️ Active Weather Alert</div>
                    <div style='color:#F1F5F9; font-weight:600; font-size:1rem;'>{banner_msg}</div>
                </div>
            </div>
            """, unsafe_allow_html=True)

        # ============================================================
        # SECTION 1 — CURRENT WEATHER HERO CARD
        # ============================================================
        st.markdown(f"""
        <div style='background: linear-gradient(135deg, rgba(14,36,64,0.7) 0%, rgba(7,18,32,0.7) 100%);
                    backdrop-filter: blur(20px); border:1px solid rgba(56,189,248,0.2); border-radius:20px;
                    padding:2rem; margin-bottom:0.5rem; position:relative; overflow:hidden;
                    box-shadow: 0 16px 40px rgba(0,0,0,0.4);'>
            <div style='position:absolute; top:-30px; right:-30px; font-size:8rem; opacity:0.07; transform:rotate(-15deg);'>{weather_emoji}</div>
            <div style='display:flex; align-items:center; gap:1.5rem; flex-wrap:wrap;'>
                <div style='font-size:4rem; filter:drop-shadow(0 0 12px rgba(56,189,248,0.4));'>{weather_emoji}</div>
                <div>
                    <div style='color:#64748B; font-size:0.75rem; font-weight:600; text-transform:uppercase; letter-spacing:2px;'>Currently in</div>
                    <div style='color:#F8FAFC; font-size:2rem; font-weight:800; line-height:1;'>{record['City']}</div>
                    <div style='color:#38BDF8; font-size:1rem; font-weight:600; margin-top:4px;'>{weather}</div>
                </div>
                <div style='margin-left:auto; text-align:right;'>
                    <div style='font-size:3.5rem; font-weight:800; background:linear-gradient(135deg,#F8FAFC,#38BDF8); -webkit-background-clip:text; -webkit-text-fill-color:transparent; background-clip:text; line-height:1;'>{temp}°C</div>
                    <div style='color:#94A3B8; font-size:0.9rem; margin-top:4px;'>Feels like {record["Feels Like"]}°C</div>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)

        # ============================================================
        # SECTION 1 — EXECUTIVE KPI CARDS
        # ============================================================
        st.markdown("<div class='section-title'>📊 Live Metrics</div>", unsafe_allow_html=True)
        kpi1, kpi2, kpi3, kpi4, kpi5, kpi6 = st.columns(6)
        kpi1.metric("🌡️ Temperature", f"{record['Temperature']}°C", delta="Live")
        kpi2.metric("🤔 Feels Like", f"{record['Feels Like']}°C")
        kpi3.metric("💧 Humidity", f"{record['Humidity']}%")
        kpi4.metric("🌬️ Wind Speed", f"{record['Wind Speed']} m/s")
        kpi5.metric("⚖️ Pressure", f"{record['Pressure']} hPa")
        kpi6.metric("👁️ Visibility", f"{record['Visibility (km)']} km")

        # ============================================================
        # SECTION 2 — OPERATIONAL ALERTS
        # ============================================================
        st.markdown("<div class='section-title'>⚠️ Operational Alerts</div>", unsafe_allow_html=True)
        alert_col1, alert_col2 = st.columns(2)
        with alert_col1:
            if temp > 35:
                st.markdown("""<div class='alert-card error'>
                    <div style='font-size:2rem; filter:drop-shadow(0 0 6px #EF4444);'>🔥</div>
                    <div><div style='font-weight:700; color:#FCA5A5; font-size:1rem;'>High Temperature Alert</div>
                    <div style='color:#94A3B8; font-size:0.875rem; margin-top:3px;'>Extreme heat — Stay cool and hydrated.</div></div>
                </div>""", unsafe_allow_html=True)
            elif temp < 10:
                st.markdown("""<div class='alert-card info'>
                    <div style='font-size:2rem; filter:drop-shadow(0 0 6px #38BDF8);'>🥶</div>
                    <div><div style='font-weight:700; color:#BAE6FD; font-size:1rem;'>Cold Weather Advisory</div>
                    <div style='color:#94A3B8; font-size:0.875rem; margin-top:3px;'>Bundle up — Freezing temperatures ahead.</div></div>
                </div>""", unsafe_allow_html=True)
            else:
                st.markdown("""<div class='alert-card success'>
                    <div style='font-size:2rem; filter:drop-shadow(0 0 6px #22C55E);'>✅</div>
                    <div><div style='font-weight:700; color:#86EFAC; font-size:1rem;'>Comfortable Conditions</div>
                    <div style='color:#94A3B8; font-size:0.875rem; margin-top:3px;'>Temperature is pleasant and stable.</div></div>
                </div>""", unsafe_allow_html=True)

        with alert_col2:
            if weather in ["Rain", "Drizzle"]:
                st.markdown("""<div class='alert-card warning'>
                    <div style='font-size:2rem; filter:drop-shadow(0 0 6px #F59E0B);'>🌧️</div>
                    <div><div style='font-weight:700; color:#FDE68A; font-size:1rem;'>Rain Alert</div>
                    <div style='color:#94A3B8; font-size:0.875rem; margin-top:3px;'>Precipitation detected — Carry an umbrella.</div></div>
                </div>""", unsafe_allow_html=True)
            elif weather == "Thunderstorm":
                st.markdown("""<div class='alert-card error'>
                    <div style='font-size:2rem; filter:drop-shadow(0 0 6px #EF4444);'>⛈️</div>
                    <div><div style='font-weight:700; color:#FCA5A5; font-size:1rem;'>Thunderstorm Warning</div>
                    <div style='color:#94A3B8; font-size:0.875rem; margin-top:3px;'>Severe storm — Seek shelter immediately.</div></div>
                </div>""", unsafe_allow_html=True)
            else:
                st.markdown("""<div class='alert-card success'>
                    <div style='font-size:2rem; filter:drop-shadow(0 0 6px #22C55E);'>☀️</div>
                    <div><div style='font-weight:700; color:#86EFAC; font-size:1rem;'>Skies Clear</div>
                    <div style='color:#94A3B8; font-size:0.875rem; margin-top:3px;'>No severe weather alerts active.</div></div>
                </div>""", unsafe_allow_html=True)

        # Apply Filters
        df_filtered = apply_filters(raw_history_df, city_filter, date_filter, weather_filter)

        if not df_filtered.empty:
            # ============================================================
            # SECTION 3 — ANALYTICS OVERVIEW
            # ============================================================
            st.markdown("<div class='section-title'>📈 Analytics Overview</div>", unsafe_allow_html=True)
            a1, a2, a3, a4, a5, a6, a7 = st.columns(7)
            a1.metric("Avg Temp", f"{df_filtered['Temperature'].mean():.1f}°C")
            a2.metric("Max Temp 🔺", f"{df_filtered['Temperature'].max():.1f}°C")
            a3.metric("Min Temp 🔻", f"{df_filtered['Temperature'].min():.1f}°C")
            a4.metric("Avg Humidity", f"{df_filtered['Humidity'].mean():.1f}%")
            a5.metric("Max Wind", f"{df_filtered['Wind Speed'].max():.1f} m/s")
            a6.metric("Avg Pressure", f"{df_filtered['Pressure'].mean():.0f} hPa")
            most_common = df_filtered["Weather"].mode()[0] if not df_filtered["Weather"].mode().empty else "N/A"
            a7.metric("Top Condition", f"{get_weather_emoji(most_common)} {most_common}")

            # ============================================================
            # SECTION 5 — SMART INSIGHTS
            # ============================================================
            st.markdown("<div class='section-title'>💡 Atmospheric Insights</div>", unsafe_allow_html=True)
            avg_t = df_filtered['Temperature'].mean()
            avg_h = df_filtered['Humidity'].mean()
            humidity_text = "consistently high — expect muggy conditions" if avg_h > 70 else "relatively stable and comfortable"

            i1, i2, i3 = st.columns(3)
            with i1:
                st.markdown(f"""
                <div class='insight-card'>
                    <div class='insight-icon'>🌡️</div>
                    <div>Average temperature tracked at <span style='color:#38BDF8; font-weight:700;'>{avg_t:.1f}°C</span> during the selected period.</div>
                </div>""", unsafe_allow_html=True)
            with i2:
                st.markdown(f"""
                <div class='insight-card'>
                    <div class='insight-icon'>💧</div>
                    <div>Atmospheric humidity was {humidity_text} at <span style='color:#38BDF8; font-weight:700;'>{avg_h:.1f}%</span>.</div>
                </div>""", unsafe_allow_html=True)
            with i3:
                st.markdown(f"""
                <div class='insight-card'>
                    <div class='insight-icon'>{get_weather_emoji(most_common)}</div>
                    <div><span style='color:#38BDF8; font-weight:700;'>{most_common}</span> conditions were the most dominant weather pattern recorded.</div>
                </div>""", unsafe_allow_html=True)

            # ============================================================
            # SECTION 4 — CHARTS
            # ============================================================
            st.markdown("<div class='section-title'>📊 Visual Intelligence</div>", unsafe_allow_html=True)
            df_chart = df_filtered.copy().set_index("Timestamp")

            c1, c2 = st.columns(2)
            with c1:
                st.markdown("<div class='chart-container'><div class='chart-title'>🌡️ Temperature Trend (°C)</div>", unsafe_allow_html=True)
                st.line_chart(df_chart["Temperature"], use_container_width=True)
                st.markdown("</div>", unsafe_allow_html=True)
            with c2:
                st.markdown("<div class='chart-container'><div class='chart-title'>🌬️ Wind Speed Trend (m/s)</div>", unsafe_allow_html=True)
                st.line_chart(df_chart["Wind Speed"], use_container_width=True)
                st.markdown("</div>", unsafe_allow_html=True)

            c3, c4 = st.columns(2)
            with c3:
                st.markdown("<div class='chart-container'><div class='chart-title'>☁️ Weather Condition Distribution</div>", unsafe_allow_html=True)
                st.bar_chart(df_filtered["Weather"].value_counts(), use_container_width=True)
                st.markdown("</div>", unsafe_allow_html=True)
            with c4:
                st.markdown("<div class='chart-container'><div class='chart-title'>💧 Humidity Trend (%)</div>", unsafe_allow_html=True)
                st.area_chart(df_chart["Humidity"], use_container_width=True)
                st.markdown("</div>", unsafe_allow_html=True)

            st.markdown("<div class='chart-container'><div class='chart-title'>📅 Daily Temperature Summary (°C)</div>", unsafe_allow_html=True)
            df_daily = df_chart.resample('D').mean(numeric_only=True)
            if not df_daily.empty:
                st.bar_chart(df_daily["Temperature"], use_container_width=True)
            st.markdown("</div>", unsafe_allow_html=True)

            # ============================================================
            # SECTION 6 — HISTORICAL DATA
            # ============================================================
            st.markdown("<div class='section-title'>📄 Master Data Table</div>", unsafe_allow_html=True)
            st.dataframe(
                df_filtered.sort_values(by="Timestamp", ascending=False),
                use_container_width=True
            )

if __name__ == "__main__":
    main()