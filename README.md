# Real-Time Weather Analytics Dashboard

## Project Overview

The Real-Time Weather Analytics Dashboard is an interactive data analytics application that collects, processes, analyzes, and visualizes live weather information using the OpenWeatherMap API.

The project demonstrates an end-to-end data analytics workflow including:

- Data collection from an external API
- Data cleaning and validation
- Missing value handling
- Duplicate removal
- Historical data storage
- KPI generation
- Interactive visualizations
- Data filtering
- CSV and Excel export

The dashboard is built using Python, Streamlit, and Pandas to provide real-time weather monitoring with an intuitive user interface.

---

## Live Demo

https://realtime-weather-dashboard.streamlit.app/

---

## GitHub Repository

https://github.com/shreya-immanavar/RealtimeWeatherDashboard

---

## Features

- Fetches live weather data using the OpenWeatherMap API
- Automatically refreshes weather information every 60 seconds
- Cleans and validates incoming weather data
- Prevents missing values and duplicate records
- Stores historical weather observations locally
- Displays live weather metrics including:
  - Temperature
  - Feels Like Temperature
  - Humidity
  - Wind Speed
  - Atmospheric Pressure
  - Visibility
- Generates weather alerts for extreme conditions
- Produces analytical insights from collected data
- Interactive filtering by:
  - City
  - Date Range
  - Weather Condition
- Interactive charts for weather analysis
- Export processed data as CSV or Excel

---

## Technologies Used

- Python
- Streamlit
- Pandas
- Requests
- OpenWeatherMap API
- OpenPyXL

---

## Dashboard Modules

### 1. Current Weather

Displays real-time weather information including:

- Temperature
- Feels Like Temperature
- Humidity
- Wind Speed
- Pressure
- Visibility
- Weather Condition

---

### 2. Analytics Dashboard

Shows summary statistics such as:

- Average Temperature
- Maximum Temperature
- Minimum Temperature
- Average Humidity
- Maximum Wind Speed
- Average Pressure
- Most Frequent Weather Condition

---

### 3. Weather Visualizations

The dashboard includes:

- Temperature Trend
- Wind Speed Trend
- Humidity Trend
- Weather Condition Distribution
- Daily Temperature Summary

---

### 4. Smart Insights

Automatically generates insights based on collected weather data, including:

- Average weather statistics
- Humidity analysis
- Dominant weather condition
- Weather alerts

---

### 5. Data Management

- Automatic data cleaning
- Missing value prevention
- Duplicate removal
- Historical data storage
- CSV Export
- Excel Export

---

## Project Structure

```text
RealTimeWeatherDashboard/
│
├── app.py
├── requirements.txt
├── README.md
├── weather_data.csv
├── .gitignore
└── screenshots/
```

---

## Installation

### Clone the Repository

```bash
git clone https://github.com/shreya-immanavar/RealtimeWeatherDashboard.git
```

### Navigate to the Project Folder

```bash
cd RealtimeWeatherDashboard
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run the Application

```bash
streamlit run app.py
```

The application will open automatically in your default web browser.

---

## API Configuration

This project uses the OpenWeatherMap API.

Create a free API key from:

https://openweathermap.org/api

Replace the API key in the application:

```python
API_KEY = "YOUR_API_KEY"
```

For production deployment, it is recommended to store the API key securely using Streamlit Secrets instead of hardcoding it.

---

## Data Storage

The application stores weather records in a local CSV file named:

```
weather_data.csv
```

Each record contains:

- Timestamp
- City
- Temperature
- Feels Like Temperature
- Humidity
- Pressure
- Wind Speed
- Visibility
- Weather Condition

The application automatically:

- Removes duplicate records
- Prevents missing values
- Updates the historical dataset after every successful API request

---

## Screenshots

Add screenshots of:

- Home Dashboard
- Current Weather Metrics
- Analytics Dashboard
- Weather Charts
- Historical Data Table
- Weather Alerts

Store the images inside the `screenshots` folder.

---

## Future Enhancements

- SQLite or PostgreSQL database integration
- Machine Learning-based weather forecasting
- Multi-city comparison dashboard
- Interactive weather maps
- User authentication
- Notification system
- Cloud database integration
- Advanced predictive analytics

---

## Author

**Shreya Immanavar**

GitHub: https://github.com/shreya-immanavar

Live Application: https://realtime-weather-dashboard.streamlit.app/
