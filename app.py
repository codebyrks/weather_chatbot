import streamlit as st
import requests
import os
from dotenv import load_dotenv
from datetime import datetime

st.set_page_config(
    page_title="Weather Bot",
    page_icon="🌦️",
    layout="wide"
)

load_dotenv()
API_KEY = os.getenv("OPENWEATHER_API_KEY")

if not API_KEY:
    st.error("❌ API key not found. Check your .env file.")
    st.stop()

# UI design 
st.markdown("""
<style>
.weather-card {
    background: linear-gradient(135deg, #74ebd5, #acb6e5);
    padding: 25px;
    border-radius: 15px;
    color: black;
    margin-bottom: 20px;
}

.forecast-card {
    background-color: #ffffff20;
    padding: 15px;
    border-radius: 12px;
    text-align: center;
    margin-bottom: 15px;
}
            
footer{
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        text-align: center;  
      }
</style>
""", unsafe_allow_html=True)

# Title
st.markdown("<h1 style='text-align:center;'>🌦️ Weather Bot</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center;'>Real-time weather & 5-day forecast</p>", unsafe_allow_html=True)

city = st.text_input("🔍 Enter city name")

if city:
    weather_url = (
        f"https://api.openweathermap.org/data/2.5/weather"
        f"?q={city}&appid={API_KEY}&units=metric"
    )

    forecast_url = (
        f"https://api.openweathermap.org/data/2.5/forecast"
        f"?q={city}&appid={API_KEY}&units=metric"
    )

    weather_res = requests.get(weather_url)
    forecast_res = requests.get(forecast_url)

    if weather_res.status_code == 200:
        data = weather_res.json()

        city_name = data["name"]
        country = data["sys"]["country"]
        temp = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        wind = data["wind"]["speed"]
        condition = data["weather"][0]["description"].capitalize()

        # Current weather details
        st.markdown(f"""
        <div class="weather-card">
            <h2>🌍 {city_name}, {country}</h2>
            <h3>🌡️ {temp} °C</h3>
            <p>☁️ Condition: {condition}</p>
            <p>💧 Humidity: {humidity}%</p>
            <p>🌬️ Wind Speed: {wind} m/s</p>
        </div>
        """, unsafe_allow_html=True)

        # Forecast Details
        st.subheader("📅 5-Day Forecast")

        if forecast_res.status_code == 200:
            forecast_data = forecast_res.json()
            shown_days = set()

            for item in forecast_data["list"]:
                date = item["dt_txt"].split(" ")[0]

                if date not in shown_days:
                    shown_days.add(date)

                    day = datetime.strptime(date, "%Y-%m-%d").strftime("%A")
                    temp = item["main"]["temp"]
                    desc = item["weather"][0]["description"].capitalize()

                    st.markdown(f"""
                    <div class="forecast-card">
                        <h4>{day}</h4>
                        <p>🌡️ {temp}°C</p>
                        <p>{desc}</p>
                    </div>
                    """, unsafe_allow_html=True)

                    if len(shown_days) == 5:
                        break
    else:
        st.error("❌ City not found or API error.")

st.markdown(f"""
<footer><p>Made By Rohit Kumar Shah</p></footer>""", unsafe_allow_html=True)