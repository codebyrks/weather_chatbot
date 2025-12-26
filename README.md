# 🌦️ Weather Chatbot

A simple and interactive web application built with **Streamlit** to fetch and display real-time weather and a 5-day forecast using the **OpenWeatherMap API**.

## 🌟 Features

* **Real-time Weather:** Fetches current temperature, humidity, wind speed, and condition.
* **5-Day Forecast:** Displays daily weather summaries.
* **Interactive UI:** Powered by Streamlit for a fast, user-friendly experience.
* **Secure API Handling:** Uses environment variables and Streamlit Secrets for key management.

## 🛠️ Tech Stack

* **Python 3.10+**
* **Streamlit** (Web App Framework)
* **Requests** (HTTP Library for API calls)
* **Python-dotenv** (Local environment management)
* **OpenWeatherMap API** (Data source)

## 📂 Project Structure

```plaintext
weather_chatbot/
├── .gitignore           # Ignores local secrets (.env) and environment folders (.venv)
├── app.py               # Main application logic and Streamlit UI
├── requirements.txt     # List of all Python dependencies
└── README.md            # Project documentation
```
## ⚙️ Local Setup

Follow these steps to run the application on your local machine.

### 1. Clone the Repository and Set Up Environment

```bash
git clone(https://github.com/codebyrks/weather_chatbot.git)
```
### 2. Create and Activate a Virtual Environment

```bash
# Example for Mac/Linux
python3 -m venv venv
source venv/bin/activate

# Example for Windows
python -m venv venv
.\venv\Scripts\activate
```

### 3. Install Dependencies
```bash
#Install all necessary libraries:
pip install -r requirements.txt
```
### 4. Configure API Key
You must have a key from OpenWeatherMap.
  1.Create a file named .env in the root directory (where app.py is located).
  2.Add your API key using the exact variable name expected by app.py:
```bash
# .env file content
OPENWEATHER_API_KEY="your-open-weather-api-key-here"
```
### 5. Run the Application
```bash
streamlit run app.py
```
The app should open automatically in your web browser.
