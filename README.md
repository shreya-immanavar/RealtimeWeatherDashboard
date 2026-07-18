# Real-Time Weather Analytics Dashboard

## Project Overview

The Real-Time Weather Analytics Dashboard is a Streamlit-based web application that collects, processes, stores, and visualizes live weather data using the OpenWeatherMap API.

The project demonstrates the complete data analytics workflow, including API integration, real-time data collection, data preprocessing, historical data storage, KPI generation, interactive visualization, filtering, data export, and cloud deployment using Streamlit Community Cloud.

The application provides live weather monitoring along with historical weather analysis through an interactive dashboard.

---

## Live Demo

https://realtime-weather-dashboard.streamlit.app/

---

## GitHub Repository

https://github.com/shreya-immanavar/RealtimeWeatherDashboard

---

# Features

## Real-Time Weather Monitoring

- Fetches live weather data from the OpenWeatherMap API.
- Search weather information by city name.
- Displays:
  - Temperature
  - Feels Like Temperature
  - Humidity
  - Atmospheric Pressure
  - Wind Speed
  - Visibility
  - Weather Condition

---

## Automatic Refresh

The dashboard automatically refreshes weather data based on the selected refresh interval.

Available options:

- 60 Seconds
- 2 Minutes
- 5 Minutes

---

## Data Processing

Incoming weather data is processed before storage by:

- Standardizing city names
- Converting numeric values into appropriate data types
- Removing missing values
- Removing duplicate records
- Creating timestamps for each observation

---

## Historical Data Storage

Weather information is stored locally in:

```
weather_data.csv
```

Each successful API request is saved, allowing users to analyze historical weather trends.

---

## Interactive Filters

Users can filter historical weather data using:

- City
- Date Range
  - All Data
  - Today
  - Last 24 Hours
  - Last 7 Days
- Weather Condition

---

## KPI Dashboard

The application displays real-time weather metrics including:

- Temperature
- Feels Like Temperature
- Humidity
- Wind Speed
- Pressure
- Visibility

Historical analytics include:

- Average Temperature
- Maximum Temperature
- Minimum Temperature
- Average Humidity
- Maximum Wind Speed
- Average Pressure
- Most Frequent Weather Condition

---

## Weather Alerts

The dashboard generates alerts for different weather situations, including:

- High Temperature Warning (Above 35°C)
- Freezing Temperature Alert (Below 0°C)
- Thunderstorm Warning
- Rain Alert
- Cold Weather Advisory
- Comfortable Weather Indicator

---

## Data Visualization

Interactive charts include:

- Temperature Trend
- Wind Speed Trend
- Humidity Trend
- Weather Condition Distribution
- Daily Temperature Summary

---

## Data Export

Filtered weather data can be exported as:

- CSV
- Excel (.xlsx)

---

# Technologies Used

- Python
- Streamlit
- Pandas
- Requests
- OpenWeatherMap API
- OpenPyXL

---

# Project Structure

```
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

# Installation

## Clone the Repository

```bash
git clone https://github.com/shreya-immanavar/RealtimeWeatherDashboard.git
```

## Navigate to the Project Directory

```bash
cd RealtimeWeatherDashboard
```

## Install Dependencies

```bash
pip install -r requirements.txt
```

## Run the Application

```bash
streamlit run app.py
```

The application will automatically open in your default web browser.

---

# Deployment

The application is deployed using **Streamlit Community Cloud**.

### Live Application

https://realtime-weather-dashboard.streamlit.app/

### Deployment Platform

- Streamlit Community Cloud
- GitHub Repository Integration
- Automatic deployment from the `main` branch

Whenever new changes are pushed to the GitHub repository, the application can be redeployed directly from Streamlit Community Cloud.

---

# API Configuration

This project uses the OpenWeatherMap API.

Create a free API key from:

https://openweathermap.org/api

Replace the API key inside `app.py`:

```python
API_KEY = "YOUR_API_KEY"
```

For production deployment, it is recommended to store the API key using **Streamlit Secrets** instead of hardcoding it.

---

# Data Storage

Weather records are stored locally in:

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

Before storage, the application automatically:

- Removes duplicate records
- Prevents missing values
- Converts numeric fields to the correct data types

---

# Screenshots

Add screenshots of the following sections inside the **screenshots/** folder.

- Home Dashboard
- Current Weather Dashboard
- Live KPI Cards
- Weather Alerts
- Analytics Dashboard
- Charts and Visualizations
- Historical Data Table

---

# Future Enhancements

- SQLite or PostgreSQL database integration
- Machine Learning-based weather prediction
- Multi-city comparison dashboard
- Interactive weather maps
- User authentication
- Cloud database integration
- Predictive weather analytics
- Email or SMS weather notifications

---

# Author

**Shreya Immanavar**

GitHub

https://github.com/shreya-immanavar

Live Application

https://realtime-weather-dashboard.streamlit.app/
