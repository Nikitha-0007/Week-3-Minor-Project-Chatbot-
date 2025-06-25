# 🤖 VirtuNexa: Virtual Assistant in Python

A simple yet powerful virtual assistant that can:
- Set reminders
- Perform basic arithmetic calculations
- Provide real-time weather updates using OpenWeather API
- Store and log user activity
- Support both **console** and **GUI (Tkinter)** interfaces

## 🛠 Technologies Used

- **Python** – Core programming language  
- **VS Code** – Development environment  
- **Tkinter** – (Optional) GUI support  
- **requests** – API integration (weather)  
- **sqlite3** – Local database for history logging  
- **pandas** – (Optional) Data analysis and export  
- **threading.Timer** – For scheduling reminders  
- **OpenWeatherMap API** – For real-time weather data  

## 🚀 Features

- 💬 Console-based or GUI interface
- 🔢 Calculate expressions like `calculate 2 + 3 * (4 - 1)`
- ⏰ Set simple reminders (auto alert after few seconds)
- 🌦 Get current weather info for your city
- 🧾 Log queries and responses in SQLite
- 📊 Export history to CSV with Pandas

## 📦 Installation

```bash
pip install -r requirements.txt
```

## 🔑 API Key Setup

1. Sign up at [OpenWeatherMap](https://openweathermap.org/)
2. Get your API key
3. Replace `"YOUR_API_KEY"` in `weather.py`

## 🧪 Run the Assistant

Console Mode:
```bash
python main.py
```

GUI Mode:
```bash
python gui.py
```

## 📃 Sample Commands

```
hello
calculate 10 + 5
remind drink water
weather
exit
```

## 📌 Author

Developed by **Bandaru Nikitha** as part of an internship project.
